import commands
import re
from resources import *

def getOFPort(iface):
    '''
    Get the ofport int number from interface table
    :param iface: string, interface name
    :return: int, of port number
    '''

    cmd = 'ovs-vsctl get interface %s ofport' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return output
    else:
        print cmd, status, output
        return -1


def dumpFlows(ovsbridge):
    '''
    Dump the flow table for one ovs bridge
    :param ovsbridge: string, ovs bridge name
    :return: list, Flow table tuples
    '''

    cmd = 'ovs-ofctl dump-flows %s' % ovsbridge

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return output.split('\n')
    else:
        print cmd, status, output
        return None


def getPhysIfaces():
    '''
    Get the physical interfaces on current host
    :return: list, List of physical interfaces
    '''

    cmd = 'ls -l /sys/class/net/ | egrep -v virtual'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regc = re.compile(r'([^\s]+) ->')
        return regc.findall(output)
    else:
        print cmd, status, output
        return None

def getNameSpaces():
    '''
    Get all NameSpaces on current host
    :return: list, namespace list
    '''

    cmd = 'ip netns list'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return output.split()
    else:
        print cmd, status, output
        return None


def execInAllNamespaces(cmd):
    '''
    Execute the given cmd in all namespaces and return the result
    :param cmd: given command
    :return: map, key is the namespace, value is the output of running the cmd in the key namespace
    '''
    namespaces = getNameSpaces()

    result = {}

    for namespace in namespaces:
        sub_cmd = 'ip netns exec %s %s' % (namespace, cmd)

        status, output = commands.getstatusoutput(sub_cmd)
        if status == 0:
            result[namespace] = output
        else:
            print sub_cmd, status, output

    return result


def getLinuxBridges():
    '''
    Get Linux bridges on current host without namespace
    :return: list, List of LinuxBridge
    '''

    cmd = 'brctl show'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        bridges = []

        tuples = output.split('\n')
        del tuples[0]

        for tuple in tuples:
            fields = tuple.split(' ')
            if len(fields) >= 3:
                name = fields[0]
                id = fields[1]
                stp = fields[2]
                nics = None

                if len(fields) >= 4:
                    nics = fields[3]

                bridges.append(LinuxBridge(name, id, stp, nics))

        return bridges
    else:
        print cmd, status, output
        return None


def getLinuxBridgesInAllNS():
    '''
    Get Linux Bridges in all namespaces
    :return: list, list of Linux Bridges
    '''

    cmd = 'brctl show'

    bridges = []

    all_ns_outputs = execInAllNamespaces(cmd)

    if not all_ns_outputs:
        return bridges

    namespaces = all_ns_outputs.keys()

    for namespace in namespaces:
        one_ns_output = all_ns_outputs[namespace]
        tuples = one_ns_output.split('\n')
        del tuples[0]

        for tuple in tuples:
            fields = tuple.split(' ')
            if len(fields) >= 3:
                name = fields[0]
                id = fields[1]
                stp = fields[2]
                nics = None

                if len(fields) >= 4:
                    nics = fields[3]

                bridges.append(LinuxBridge(name, id, stp, nics, namespace))

    return bridges


def getOVSBridges():
    '''
    Get OVS Bridges
    :return: list, list of OVSBridge
    '''

    cmd = 'ovs-vsctl show'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        lines = output.split('\n')

        bridges = []
        bridge = None
        port = None
        interface = None

        for line in lines:
            if line.startswith("    Bridge"):
                fields = line.strip().split(' ')
                br_name = fields[1].replace('"', '')
                bridge = OVSBridge(br_name, [], {})
                bridges.append(bridge)

            elif line.startswith("        Port"):
                fields = line.strip().split(' ')
                port_name = fields[1].replace('"', '')
                port = OVSPort(port_name, [], {})
                if bridge is not None:
                    bridge.addport(port)

            elif line.startswith("            Interface"):
                fields = line.strip().split(' ')
                interface_name = fields[1].replace('"', '')
                interface = OVSInterface(interface_name, {})
                if port is not None:
                    port.addinterface(interface)

            elif line.startswith("                "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if interface is not None:
                    interface.updateoption(key, value)

            elif line.startswith("            "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if port is not None:
                    port.updateoption(key, value)

            elif line.startswith("        "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if bridge is not None:
                    bridge.updateoption(key, value)

        return bridges
    else:
        print cmd, status, output
        return None


def getRoutes():
    '''
    Get Routes
    :return: list, list of Route
    '''

    cmd = 'ip route show'

    status, output = commands.getstatusoutput(cmd)

    routes = []

    if status == 0:
        regc_default = re.compile(r'default via \b(.*)\b dev \b([^ ]*)\b ')
        default_routes = regc_default.findall(output)

        for default_route in default_routes:
            routes.append(Route("0.0.0.0/0", default_route[1], default_route[0]))

        regc_other = re.compile(r'(\S+) dev (\S+)  proto \S+  scope \S+  src (\S+)')
        other_routes = regc_other.findall(output)

        for other_route in other_routes:
            routes.append(Route(other_route[0], other_route[1], other_route[2]))

        return routes
    else:
        print cmd, status, output
        return None


def getTunnels():
    '''
    Get the tunnels for this host
    :return: list, list of Tunnel
    '''

    cmd = 'ip l2tp show tunnel'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regc = re.compile(r'(?s)Tunnel (\d+).*?From (\S+).*?to (\S+)\s+Peer tunnel (\d+).*?ports: (\d+)/(\d+)')
        tunnels = []
        regex_outputs = regc.findall(output)

        for regex_output in regex_outputs:
            tunnels.append(Tunnel(regex_output[0], regex_output[1], regex_output[2],
                                  regex_output[3], regex_output[4], regex_output[5]))

        return tunnels
    else:
        print cmd, status, output
        return None


def getTunnelsInAllNS():
    '''
    Get the tunnels for all namespaces
    :return: list, list of Tunnel
    '''

    cmd = 'ip l2tp show tunnel'

    regc = re.compile(r'(?s)Tunnel (\d+).*?From (\S+).*?to (\S+)\s+Peer tunnel (\d+).*?ports: (\d+)/(\d+)')

    tunnels = []

    all_ns_outputs = execInAllNamespaces(cmd)

    if not all_ns_outputs:
        return tunnels

    namespaces = all_ns_outputs.keys()

    for namespace in namespaces:
        one_ns_output = all_ns_outputs[namespace]

        regex_outputs = regc.findall(one_ns_output)

        for regex_output in regex_outputs:
            tunnels.append(Tunnel(regex_output[0], regex_output[1], regex_output[2],
                                  regex_output[3], regex_output[4], regex_output[5],
                                  namespace))

    return tunnels


def getSessions():
    '''
    Get the sessions for this host
    :return: list, list of Session
    '''

    cmd = 'ip l2tp show session'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regc = re.compile(r'(?s)Session (\d+) in tunnel (\d+)\s+Peer session (\d+), tunnel (\d+)\s+interface name: (\S+)')
        sessions = []
        regex_outputs = regc.findall(output)

        for regex_output in regex_outputs:
            sessions.append(Session(regex_output[0], regex_output[1], regex_output[2],
                                  regex_output[3], regex_output[4]))

        return sessions
    else:
        print cmd, status, output
        return None


def getSessionsInAllNS():
    '''
    Get the sessions for all namespaces
    :return: list, list of Session
    '''

    cmd = 'ip l2tp show session'

    regc = re.compile(r'(?s)Session (\d+) in tunnel (\d+)\s+Peer session (\d+), tunnel (\d+)\s+interface name: (\S+)')

    sessions = []

    all_ns_outputs = execInAllNamespaces(cmd)

    if not all_ns_outputs:
        return sessions

    namespaces = all_ns_outputs.keys()

    for namespace in namespaces:
        one_ns_output = all_ns_outputs[namespace]

        regex_outputs = regc.findall(one_ns_output)

        for regex_output in regex_outputs:
            sessions.append(Session(regex_output[0], regex_output[1], regex_output[2],
                                   regex_output[3], regex_output[4], namespace))

    return sessions


def getIpAddrIfaces():
    '''
    Get the interfaces list from 'ip address show' cmd
    :return: list, list of IpAddressInterface
    '''

    cmd = 'ip address show'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        ifaces = []

        lines = output.split('\n')
        iface = None

        for line in lines:
            if line.startswith(' '):
                line = line.strip()
                if line.startswith("link/"):
                    regex_result = re.search(r'link/\S+ (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface.setmac(regex_result.group(1))
                elif line.startswith("inet "):
                    regex_result = re.search(r'inet (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface.setip(regex_result.group(1))
            else:
                regex_result = re.search(r'(\d+): (\S+): \S+ mtu (\d+).*?state (\S+)', line)

                if regex_result:
                    iface = IpAddressInterface(regex_result.group(2), regex_result.group(1),
                                               regex_result.group(3), regex_result.group(4))
                    ifaces.append(iface)

        return ifaces
    else:
        print cmd, status, output
        return None


def getIpAddrIfacesInAllNS():
    '''
    Get the interfaces list from 'ip address show' cmd in all namepsaces
    :return: list, list of IpAddressInterface
    '''

    cmd = 'ip address show'

    ifaces = []

    all_ns_outputs = execInAllNamespaces(cmd)

    if not all_ns_outputs:
        return ifaces

    namespaces = all_ns_outputs.keys()

    for namespace in namespaces:
        one_ns_output = all_ns_outputs[namespace]

        lines = one_ns_output.split('\n')
        iface = None

        for line in lines:
            if line.startswith(' '):
                line = line.strip()
                if line.startswith("link/"):
                    regex_result = re.search(r'link/\S+ (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface.setmac(regex_result.group(1))
                elif line.startswith("inet "):
                    regex_result = re.search(r'inet (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface.setip(regex_result.group(1))
            else:
                regex_result = re.search(r'(\d+): (\S+): \S+ mtu (\d+).*?state (\S+)', line)

                if regex_result:
                    iface = IpAddressInterface(regex_result.group(2), regex_result.group(1),
                                               regex_result.group(3), regex_result.group(4), namespace=namespace)
                    ifaces.append(iface)

    return ifaces


def getVethPeerIndex(ifaceName, namespace=None):
    '''
    Get the Veth Peer Index for given interface
    :param ifaceName: string, name of interface
    :return: int, the index for the peer interface
    '''

    cmd = "ethtool -S %s | awk '/peer_ifindex/ {print $2}'" % ifaceName

    if namespace is not None:
        cmd = "ip netns exec " + namespace + " " + cmd

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        #print cmd, status, output
        return output
    else:
        print cmd, status, output
        return None


def getOVSOptions(ifaceName, ovsBridges):
    if ovsBridges is None:
        return None

    for bridge in ovsBridges:
        for port in bridge.ports:
            if ifaceName == port.name:
                for interface in port.interfaces:
                    if ifaceName == interface.name:
                        options = {}

                        for key in port.options.keys():
                            options[key] = port.options[key]

                        for key in interface.options.keys():
                            options[key] = interface.options[key]

                        return options

    return None


def isPhysIface(ifaceName):
    '''
    Whether this is an physical interface
    :param iface: string, interface name
    :return: boolean, True or False
    '''

    phys = getPhysIfaces()
    if phys is None:
        return False
    elif not phys:
        return False
    else:
        return ifaceName in phys

def isLoopBack(ifaceName):
    '''
    Check whether the iface is lo one
    :param iface: string, interface name
    :return: boolean, True or False
    '''

    return ifaceName == 'lo'


def isOvsSystem(ifaceName):
    '''
    Check whether the iface is ovs-system one
    :param iface: string, interface name
    :return: boolean, True or False
    '''

    return ifaceName == 'ovs-system'


def isLinuxBrIface(ifaceName, namespace=None):
    '''
    Check whether the given interface is a Linux Bridge Interface
    :param ifaceName: string, name of interface
    :return: boolean, True or False
    '''

    cmd = 'ls /sys/devices/virtual/net/%s/bridge' %ifaceName
    if namespace is not None:
        cmd = "ip netns exec " + namespace + " " + cmd

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return True
    else:
        #print cmd, status, output
        return False


def isTunTap(ifaceName, namespace=None):
    '''
    Check whether the given interface is a Tunnel Tap
    :param ifaceName: string, name of interface
    :return: boolean, True or False
    '''

    cmd = 'ls /sys/class/net/%s/tun_flags' %ifaceName
    if namespace is not None:
        cmd = "ip netns exec " + namespace + " " + cmd

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return True
    else:
        #print cmd, status, output
        return False


def isVlanAlias(ifaceName):
    '''
    Check whether this name is a vlan alias
    :param ifaceName: string, name of interface
    :return: boolean, True or False
    '''

    return ifaceName.find('@') != -1


def getSession(ifaceName, sessions):
    '''
    Get the session for the given interface
    :param ifaceName: string, name of interface
    :param sessions: list, list of Session
    :return: Session
    '''

    if sessions is None:
        return None

    for session in sessions:
        if session.iface == ifaceName:
            return session

    return None


def getTunnel(tunId, tunnels):
    '''
    Get the Tunnel from the given tunId
    :param tunId: int, tunnel Id
    :param tunnels: list, list of Tunnel
    :return: Tunnel
    '''

    if tunnels is None:
        return None

    for tunnel in tunnels:
        if tunnel.tunId == tunId:
            return tunnel

    return None


def findOutIface(ip):
    '''
    Find the interface used to send out the packet according to the given IP
    :param ip: string, 'ip/netmask' format or 'ip' format
    :return: string, interface name
    '''

    routes = getRoutes()
    if routes is not None:
        for route in routes:
            if ip.startswith(route.src):
                return route.device

    return None


def getAllInterfaces(allNs):
    '''
    Return all the interfaces on given host
    :param allNs: boolean, True or False, whether to exec in all NameSpaces
    :return: list, list of Interface
    '''

    ipAddrIfaces = []
    ovsBridges = getOVSBridges()
    physIfaces = getPhysIfaces()
    sessions = []
    tunnels = []

    if allNs:
        ipAddrIfaces = getIpAddrIfacesInAllNS()
        sessions = getSessionsInAllNS()
        tunnels = getTunnelsInAllNS()
    else:
        ipAddrIfaces = getIpAddrIfaces()
        sessions = getSessions()
        tunnels = getTunnels()

    ifaces = []

    if ipAddrIfaces is not None:
        for ipAddrIface in ipAddrIfaces:
            name = ipAddrIface.name
            iface = Interface(name, ipAddrIface.index, None, ipAddrIface.mtu, ipAddrIface.state,
                              ipAddrIface.mac, ipAddrIface.ip, ipAddrIface.namespace, options={})

            ifaces.append(iface)

            if isOvsSystem(name):
                iface.settype('ovs-system')

            peer = getVethPeerIndex(name, ipAddrIface.namespace)
            if peer is not None:
                if peer.isdigit():
                    iface.settype('veth-pair')
                    iface.updateoption('peerIf', peer)

            if isLinuxBrIface(name):
                iface.settype('LinuxBridgeInterface')

            options = getOVSOptions(name, ovsBridges)
            if options is not None:
                if options.has_key('type'):
                    if options['type'] == 'internal':
                        iface.settype('OVSInternal')
                    elif options['type'] == 'gre':
                        iface.settype('gre')
                    elif options['type'] == 'vxlan':
                        iface.settype('vxlan')

                for key in options.keys():
                    #print name, key, options[key]
                    iface.updateoption(key, options[key])

            if isPhysIface(name):
                iface.settype('physical')

            if isLoopBack(name):
                iface.settype('loopback')

            if isTunTap(name):
                iface.settype('tuntap')

            session = getSession(name, sessions)
            if session is not None:
                iface.settype('l2tp')
                tunnel = getTunnel(session.tunId, tunnels)

                if tunnel is not None:
                    ifaceUsed = findOutIface(tunnel.fromIp)

                    if ifaceUsed is not None:
                        iface.updateoption('ifaceUsed', ifaceUsed)

            if isVlanAlias(name):
                regex_result = re.search(r'(\S+)\.(\d+)@(\S+)', name)
                if regex_result:
                    if regex_result.group(1) == regex_result.group(3):
                        iface.settype('vlan_alias')
                        iface.updateoption('vlantag', regex_result.group(2))
                        iface.updateoption('ifaceUsed', regex_result.group(1))

    return ifaces


