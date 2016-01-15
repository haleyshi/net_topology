import commands
import re
import json
from resources import *

def getOVSBridgeuuid(bridge):
    '''
    Get the _uuid string from bridge table
    :param iface: string, bridge name or _uuid
    :return: string, _uuid
    '''

    cmd = 'ovs-vsctl get bridge %s _uuid' % bridge

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return output
    else:
        print cmd, status, output
        return None


def getOVSBridgeports(bridge):
    '''
    Get the ports string from bridge table
    :param iface: string, bridge name or _uuid
    :return: string, _uuid
    '''

    cmd = 'ovs-vsctl get bridge %s ports' % bridge

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSBridgeflowtables(bridge):
    '''
    Get the flow_tables string from bridge table
    :param iface: string, bridge name or _uuid
    :return: string, flow_tables
    '''

    cmd = 'ovs-vsctl get bridge %s flow_tables' % bridge

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "{}":
            return None

        output = output.replace("{", "")
        output = output.replace("}", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortname(port):
    '''
    Get the name string from port table
    :param iface: string, port name or _uuid
    :return: string, name
    '''

    cmd = 'ovs-vsctl get port %s name' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        output = output.replace('"', '')
        return output
    else:
        print cmd, status, output
        return None


def getOVSPorttag(port):
    '''
    Get the tag string from port table
    :param iface: string, port name or _uuid
    :return: string, tag
    '''

    cmd = 'ovs-vsctl get port %s tag' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortlacp(port):
    '''
    Get the lacp string from port table
    :param iface: string, port name or _uuid
    :return: string, lacp
    '''

    cmd = 'ovs-vsctl get port %s lacp' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPorttag(port):
    '''
    Get the tag string from port table
    :param iface: string, port name or _uuid
    :return: string, tag
    '''

    cmd = 'ovs-vsctl get port %s tag' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPorttrunks(port):
    '''
    Get the trunks string from port table
    :param iface: string, port name or _uuid
    :return: string, trunks
    '''

    cmd = 'ovs-vsctl get port %s trunks' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortvlanmode(port):
    '''
    Get the vlan_mode string from port table
    :param iface: string, port name or _uuid
    :return: string, vlan_mode
    '''

    cmd = 'ovs-vsctl get port %s vlan_mode' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortbondmode(port):
    '''
    Get the bond_mode string from port table
    :param iface: string, port name or _uuid
    :return: string, bond_mode
    '''

    cmd = 'ovs-vsctl get port %s bond_mode' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortinterfaces(port):
    '''
    Get the interfaces string from port table
    :param iface: string, port name or _uuid
    :return: string, interfaces
    '''

    cmd = 'ovs-vsctl get port %s interfaces' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSPortstatistics(port):
    '''
    Get the statistics string from port table
    :param iface: string, port name or _uuid
    :return: string, statistics
    '''

    cmd = 'ovs-vsctl get port %s statistics' % port

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "{}":
            return None

        output = output.replace("{", "")
        output = output.replace("}", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacename(iface):
    '''
    Get the naem string from interface table
    :param iface: string, interface name or _uuid
    :return: string, name
    '''

    cmd = 'ovs-vsctl get interface %s name' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        output = output.replace('"', '')
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacetype(iface):
    '''
    Get the type string from interface table
    :param iface: string, interface name or _uuid
    :return: string, type
    '''

    cmd = 'ovs-vsctl get interface %s type' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == '""':
            return None

        output = output.replace('"', '')
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfaceofport(iface):
    '''
    Get the ofport int number from interface table
    :param iface: string, interface name or _uuid
    :return: int, ofport number
    '''

    cmd = 'ovs-vsctl get interface %s ofport' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "-1":
            return None
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacemac(iface):
    '''
    Get the mac string from interface table
    :param iface: string, interface name or _uuid
    :return: string, mac
    '''

    cmd = 'ovs-vsctl get interface %s mac' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None

def getOVSInterfacemacinuse(iface):
    '''
    Get the mac_in_use string from interface table
    :param iface: string, interface name or _uuid
    :return: string, mac_in_use
    '''

    cmd = 'ovs-vsctl get interface %s mac_in_use' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == '""':
            return None

        output = output.replace('"', '')
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacestatus(iface):
    '''
    Get the status string from interface table
    :param iface: string, interface name or _uuid
    :return: string, status
    '''

    cmd = 'ovs-vsctl get interface %s status' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "{}":
            return None

        output = output.replace("{", "")
        output = output.replace("}", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacemtu(iface):
    '''
    Get the mtu string from interface table
    :param iface: string, interface name or _uuid
    :return: string, mtu
    '''

    cmd = 'ovs-vsctl get interface %s mtu' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "[]":
            return None

        output = output.replace("[", "")
        output = output.replace("]", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfacestatistics(iface):
    '''
    Get the statistics string from interface table
    :param iface: string, interface name or _uuid
    :return: string, statistics
    '''

    cmd = 'ovs-vsctl get interface %s statistics' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "{}":
            return None

        output = output.replace("{", "")
        output = output.replace("}", "")
        return output
    else:
        print cmd, status, output
        return None


def getOVSInterfaceoptions(iface):
    '''
    Get the options string from interface table
    :param iface: string, interface name or _uuid
    :return: string, options
    '''

    cmd = 'ovs-vsctl get interface %s options' % iface

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        if output == "{}":
            return None

        output = output.replace("{", "")
        output = output.replace("}", "")
        output = output.replace('"', '')
        return output
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

        bridge = None

        for tuple in tuples:
            tuple = tuple.strip()
            tuple = re.sub(r'\s+', ' ', tuple)
            fields = tuple.split(' ')

            if len(fields) == 1:
                if bridge is not None:
                    if bridge.has_key("__interfaces"):
                        bridge["__interfaces"].append({"name":fields[0], "_type":"linux-bridge-interface"})
            if len(fields) >= 3:
                bridge = {}
                bridge["_type"] = "linux-bridge"
                bridge["name"] = fields[0]
                bridge["index"] = fields[1]
                bridge["stp"] = fields[2]

                if len(fields) == 4:
                    bridge["__interfaces"] = []
                    bridge["__interfaces"].append({"name":fields[3], "_type":"linux-bridge-interface"})

                bridges.append(bridge)

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

        bridge = None

        for tuple in tuples:
            tuple = tuple.strip()
            tuple = tuple.replace("\t\t", "\t")
            fields = tuple.split('\t')
            if len(fields) == 1:
                if bridge is not None:
                    bridge["__interfaces"].append({"name":fields[0], "_type":"linux-bridge-interface"})
            if len(fields) >= 3:
                bridge = {}
                bridge["_type"] = "linux-bridge"
                bridge["name"] = fields[0]
                bridge["index"] = fields[1]
                bridge["stp"] = fields[2]
                bridge["namespace"] = namespace

                if len(fields) == 4:
                    bridge["__interfaces"] = []
                    bridge["__interfaces"].append({"name":fields[3], "_type":"linux-bridge-interface"})

                bridges.append(bridge)

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

        for line in lines:
            if line.startswith("    Bridge"):
                fields = line.strip().split(' ')
                bridge = {}
                bridge["name"] = fields[1].replace('"', '')
                bridge["_type"] = "ovs-bridge"
                bridge["__uuid"] = getOVSBridgeuuid(bridge["name"])

                flow_tables = getOVSBridgeflowtables(bridge["name"])
                if flow_tables is not None:
                    bridge["__flow_tables"] = flow_tables

                bridges.append(bridge)

                port_uuids = getOVSBridgeports(bridge["name"])
                if port_uuids is not None:
                    ports = []
                    bridge["__ports"] = ports

                    port_uuid_list = port_uuids.split(", ")
                    for port_uuid in port_uuid_list:
                        port = {}
                        port["__uuid"] = port_uuid
                        port["name"] = getOVSPortname(port_uuid)
                        port["_type"] = "ovs-port"
                        port["ovs-bridge"] = bridge["name"]

                        tag = getOVSPorttag(port_uuid)
                        if tag is not None:
                            port["tag"] = tag

                        lacp = getOVSPortlacp(port_uuid)
                        if lacp is not None:
                            port["__lacp"] = lacp

                        bond_mode = getOVSPortbondmode(port_uuid)
                        if bond_mode is not None:
                            port["bond_mode"] = bond_mode

                        trunks = getOVSPorttrunks(port_uuid)
                        if trunks is not None:
                            port["__trunks"] = trunks

                        vlan_mode = getOVSPortvlanmode(port_uuid)
                        if vlan_mode is not None:
                            port["vlan_mode"] = vlan_mode

                        statistics = getOVSPortstatistics(port_uuid)
                        if statistics is not None:
                            statistic_pairs = statistics.split(", ")
                            for statistic_pair in statistic_pairs:
                                pair = statistic_pair.split("=")
                                if len(pair) == 2:
                                    port[pair[0]] = pair[1]

                        ports.append(port)

                        interface_uuids = getOVSPortinterfaces(port_uuid)
                        if interface_uuids is not None:
                            interfaces = []
                            port["__interfaces"] = interfaces

                            interface_uuid_list = interface_uuids.split(", ")
                            for interface_uuid in interface_uuid_list:
                                interface = {}
                                interface["__uuid"] = interface_uuid
                                interface["name"] = getOVSInterfacename(interface_uuid)
                                interface["ovs-port"] = port["name"]
                                interface["ovs-bridge"] = bridge["name"]
                                interface["_type"] = "ovs-interface"

                                mac = getOVSInterfacemac(interface_uuid)
                                if mac is not None:
                                    interface["mac"] = mac

                                mac_in_use = getOVSInterfacemacinuse(interface_uuid)
                                if mac_in_use is not None:
                                    interface["mac_in_use"] = mac_in_use

                                mtu = getOVSInterfacemtu(interface_uuid)
                                if mtu is not None:
                                    interface["mtu"] = mtu

                                status = getOVSInterfacestatus(interface_uuid)
                                if status is not None:
                                    interface["status"] = status

                                ofport = getOVSInterfaceofport(interface_uuid)
                                if ofport is not None:
                                    interface["__ofport"] = ofport

                                options = getOVSInterfaceoptions(interface_uuid)
                                if options is not None:
                                    option_pairs = options.split(", ")
                                    for option_pair in option_pairs:
                                        pair = option_pair.split("=")
                                        if len(pair) == 2:
                                            interface[pair[0]] = pair[1]

                                statistics = getOVSInterfacestatistics(interface_uuid)
                                if statistics is not None:
                                    statistic_pairs = statistics.split(", ")
                                    for statistic_pair in statistic_pairs:
                                        pair = statistic_pair.split("=")
                                        if len(pair) == 2:
                                            interface[pair[0]] = pair[1]

                                type = getOVSInterfacetype(interface_uuid)
                                if type is not None:
                                    interface["type"] = type

                                interfaces.append(interface)

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
        #print cmd, status, output
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
        #print cmd, status, output
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


def setMoreInfoFromIfConfig(iface, namespace=None):
    '''
    Read information from ifconfig and set to interface
    :param iface: dict, interface
    :return: None
    '''

    if iface is None:
        return

    if not iface.has_key("name"):
        return

    name = iface["name"]

    if namespace is None:
        cmd = 'ifconfig %s' % name
    else:
        cmd = 'ip netns exec %s ifconfig %s' % (namespace, name)

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regex_result = re.search(r'(?s)RX packets:(\d+) errors:(\d+) dropped:(\d+) overruns:(\d+) frame:(\d+)', output)

        if regex_result:
            iface["rx_packets"] = regex_result.group(1)
            iface["rx_errors"] = regex_result.group(2)
            iface["rx_dropped"] = regex_result.group(3)

        regex_result = re.search(r'(?s)TX packets:(\d+) errors:(\d+) dropped:(\d+) overruns:(\d+) carrier:(\d+)', output)

        if regex_result:
            iface["tx_packets"] = regex_result.group(1)
            iface["tx_errors"] = regex_result.group(2)
            iface["tx_dropped"] = regex_result.group(3)

        regex_result = re.search(r'(?s)collisions:(\d+) txqueuelen:(\d+)', output)
        if regex_result:
            iface["collisions"] = regex_result.group(1)

        regex_result = re.search(r'(?s)RX bytes:(\d+).*?TX bytes:(\d+)', output)
        if regex_result:
            iface["rx_bytes"] = regex_result.group(1)
            iface["tx_bytes"] = regex_result.group(2)
    else:
        return


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
                            iface["mac"] = regex_result.group(1)
                elif line.startswith("inet "):
                    regex_result = re.search(r'inet (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface["ip"] = regex_result.group(1)
            else:
                regex_result = re.search(r'(\d+): (\S+): \S+ mtu (\d+).*?state (\S+)', line)

                if regex_result:
                    iface = {}
                    iface["index"] = regex_result.group(1)
                    iface["name"] = regex_result.group(2)
                    iface["mtu"] = regex_result.group(3)
                    iface["state"] = regex_result.group(4)

                    setMoreInfoFromIfConfig(iface)

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
                            iface["mac"] = regex_result.group(1)
                elif line.startswith("inet "):
                    regex_result = re.search(r'inet (\S+)', line)

                    if regex_result:
                        if iface is not None:
                            iface["ip"] = regex_result.group(1)
            else:
                regex_result = re.search(r'(\d+): (\S+): \S+ mtu (\d+).*?state (\S+)', line)

                if regex_result:
                    if regex_result.group(2) == "lo":
                        iface = None
                        continue

                    iface = {}
                    iface["index"] = regex_result.group(1)
                    iface["name"] = regex_result.group(2)
                    iface["mtu"] = regex_result.group(3)
                    iface["state"] = regex_result.group(4)
                    iface["namespace"] = namespace

                    setMoreInfoFromIfConfig(iface, namespace)

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


def getInterface(ifaceName, ipAddrIfaces):
    if ipAddrIfaces is None:
        return None

    for iface in ipAddrIfaces:
        if iface.has_key("name"):
            if iface["name"] == ifaceName:
                return iface

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


'''
def isLinuxBrIface(ifaceName, namespace=None):

    cmd = 'ls /sys/devices/virtual/net/%s/bridge' %ifaceName
    if namespace is not None:
        cmd = "ip netns exec " + namespace + " " + cmd

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        return True
    else:
        #print cmd, status, output
        return False
'''

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


def setMoreInfo(iface, sessions, tunnels):
    if iface is None:
        return

    if not iface.has_key("name"):
        return

    name = iface["name"]
    if isOvsSystem(name):
        iface["__type"] = 'ovs-system'

    namespace = None
    if iface.has_key("namespace"):
        namespace = iface["namespace"]

    peer = getVethPeerIndex(name, namespace)
    if peer is not None:
        if peer.isdigit():
            iface["__type"] = 'veth-pair'
            iface["__peerIf"] = peer

    if isPhysIface(name):
        iface["__type"] = 'physical'

    if isLoopBack(name):
        iface["__type"] = 'loopback'

    if isTunTap(name):
        iface["__type"] = 'tuntap'

    session = getSession(name, sessions)
    if session is not None:
        iface["__type"] = 'l2tp'
        tunnel = getTunnel(session.tunId, tunnels)
        if tunnel is not None:
            ifaceUsed = findOutIface(tunnel.fromIp)

            if ifaceUsed is not None:
                iface["__ifaceUsed"] = ifaceUsed

    if isVlanAlias(name):
        regex_result = re.search(r'(\S+)\.(\d+)@(\S+)', name)
        if regex_result:
            if regex_result.group(1) == regex_result.group(3):
                iface["__type"] = 'vlan_alias'
                iface["__vlantag"] =  regex_result.group(2)
                iface["__ifaceUsed"] = regex_result.group(1)


def setInstanceInfo(instances):
    if instances is None:
        return

    for instance in instances:
        if instance.has_key("id"):
            id = instance["id"]

            cmd = 'virsh dumpxml %s' % id

            status, output = commands.getstatusoutput(cmd)

            in_interface = False

            if status == 0:
                interfaces = []
                lines = output.split('\n')

                for line in lines:
                    line = line.strip()

                    if line.startswith("<interface"):
                        in_interface = True
                    elif line.startswith("</interface>"):
                        in_interface = False
                    elif in_interface:
                        if line.startswith("<target dev="):
                            line = line.replace("<target dev='", "")
                            line = line.replace("'/>", "")

                            interfaces.append({"name":line})

                if len(interfaces) != 0:
                    instance["interfaces"] = interfaces
            #else:
                #print cmd, status, output


def getVirshInfo():

    cmd = 'virsh list'

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        tuples = output.split('\n')

        if tuples is None:
            return None

        if len(tuples) < 2:
            return None

        del tuples[0]
        del tuples[0]

        instances = []

        for tuple in tuples:
            tuple = tuple.strip()
            tuple = re.sub(r'\s+', ' ', tuple)
            fields = tuple.split(' ')

            if len(fields) == 3:
                instance = {}
                instance["id"] = fields[0]
                instance["name"] = fields[1]
                instance["state"] = fields[2]

                instances.append(instance)

        setInstanceInfo(instances)

        return instances
    else:
        #print cmd, status, output
        return None


def getAll():
    '''
    Return all the bridge/port/interface on given host
    :return: A dict of network topology
    '''

    ovsBridges = getOVSBridges()

    linuxBridges = getLinuxBridges()
    linuxBridgesInAllNS = getLinuxBridgesInAllNS()

    ipAddrIfaces = getIpAddrIfaces()
    ipAddrIfacesInAllNS = getIpAddrIfacesInAllNS()

    physIfaces = getPhysIfaces()

    sessions = getSessions()
    sessionsInAllNS = getSessionsInAllNS()

    tunnels = getTunnels()
    tunnelsInAllNS = getTunnelsInAllNS()

    instances = getVirshInfo()

    # Merge data for all namespaces
    if linuxBridgesInAllNS is not None:
        if linuxBridges is None:
            linuxBridges = linuxBridgesInAllNS
        else:
            for linuxBridge in linuxBridgesInAllNS:
                linuxBridges.append(linuxBridge)

    if ipAddrIfacesInAllNS is not None:
        if ipAddrIfaces is None:
            ipAddrIfaces = ipAddrIfacesInAllNS
        else:
            for ipAddrIface in ipAddrIfacesInAllNS:
                ipAddrIfaces.append(ipAddrIface)

    if sessionsInAllNS is not None:
        if sessions is None:
            sessions = sessionsInAllNS
        else:
            for session in sessionsInAllNS:
                sessions.append(session)

    if tunnelsInAllNS is not None:
        if tunnels is None:
            tunnels = tunnelsInAllNS
        else:
            for tunnel in tunnelsInAllNS:
                tunnels.append(tunnel)

    if ipAddrIfaces is not None:
        for ipAddrIface in ipAddrIfaces:
            setMoreInfo(ipAddrIface, sessions, tunnels)

    if ovsBridges is not None:
        for ovsBridge in ovsBridges:
            if ovsBridge.has_key("__ports"):
                ports = ovsBridge["__ports"]
                if ports is not None:
                    for port in ports:
                        if port.has_key("__interfaces"):
                            interfaces = port["__interfaces"]
                            if interfaces is not None:
                                for interface in interfaces:
                                    if interface is not None:
                                        if interface.has_key("name"):
                                            ifaceName = interface["name"]
                                            ipAddrIface = getInterface(ifaceName, ipAddrIfaces)
                                            if ipAddrIface is not None:
                                                for key in ipAddrIface.keys():
                                                    if not interface.has_key(key):
                                                        interface[key] = ipAddrIface[key]
                                                ipAddrIfaces.remove(ipAddrIface)

    if linuxBridges is not None:
        for linuxBridge in linuxBridges:
            if linuxBridge.has_key("__interfaces"):
                interfaces = linuxBridge["__interfaces"]
                if interfaces is not None:
                    for interface in interfaces:
                        if interface is not None:
                            if interface.has_key("name"):
                                ifaceName = interface["name"]
                                ipAddrIface = getInterface(ifaceName, ipAddrIfaces)
                                if ipAddrIface is not None:
                                    for key in ipAddrIface.keys():
                                        if not interface.has_key(key):
                                            interface[key] = ipAddrIface[key]
                                    ipAddrIfaces.remove(ipAddrIface)

    topo = {}

    if ovsBridges is not None:
        if len(ovsBridges) != 0:
            topo["ovs-bridges"] = ovsBridges

    if linuxBridges is not None:
        if len(linuxBridges) != 0:
            topo["linux-bridges"] = linuxBridges

    if ipAddrIfaces is not None:
        if len(ipAddrIfaces) != 0:
            topo["others"] = ipAddrIfaces

    if instances is not None:
        if len(instances) != 0:
            topo["instances"] = instances

    return topo


def printAll():
    print json.dumps(getAll())

