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


def isPhysIface(iface):
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
        return iface in phys

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



def isLoopBack(iface):
    '''
    Check whether the iface is lo one
    :param iface: string, interface name
    :return: boolean, True or False
    '''

    return iface == 'lo'


def isOvsSystem(iface):
    '''
    Check whether the iface is ovs-system one
    :param iface: string, interface name
    :return: boolean, True or False
    '''

    return iface == 'ovs-system'


def getAllIfaces():
    '''
    Get all interfaces
    :return: list, list of interfaces
    '''
    #TODO

def getTunnels():
    '''
    Get the tunnels for all namespaces
    :return: list, list of Tunnel
    '''

    #TODO
    cmd = 'ip l2tp show tunnel'

    regc = re.compile('(?s)Tunnel (\d+).*?From (\S+).*?to (\S+)\s+Peer tunnel (\d+).*?ports: (\d+)/(\d+)')


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

                bridges.append(LinuxBridge(name, id, stp, nics, None))

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

    br_outputs = execInAllNamespaces(cmd)

    if not br_outputs:
        return bridges

    namespaces = br_outputs.keys()

    for namespace in namespaces:
        br_output = br_outputs[namespace]
        tuples = br_output.split('\n')
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
                    bridge.addPort(port)

            elif line.startswith("            Interface"):
                fields = line.strip().split(' ')
                interface_name = fields[1].replace('"', '')
                interface = OVSInterface(interface_name, {})
                if port is not None:
                    port.addInterface(interface)

            elif line.startswith("                "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if interface is not None:
                    interface.updateOption(key, value)

            elif line.startswith("            "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if port is not None:
                    port.updateOption(key, value)

            elif line.startswith("        "):
                fields = line.strip().split(' ')
                key = fields[0].replace(':', '')
                value = fields[1].replace('"', '')
                if bridge is not None:
                    bridge.updateOption(key, value)

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


