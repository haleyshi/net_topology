

class NetworkElement():
    def __init__(self, name):
        self.name = name


class Interface(NetworkElement):
    def __init__(self, name, index, type, mtu, state, mac, ip, namespace, options={}):
        NetworkElement.__init__(self, name)
        self.index = index
        self.type = type
        self.mtu = mtu
        self.state = state
        self.mac = mac
        self.ip = ip
        self.namespace = namespace
        self.options = options

    def settype(self, type):
        self.type = type

    def updateoption(self, key, value):
        self.options[key] = value

    def __str__(self):
        return "Interface(name: %s, index: %s, type: %s, mtu: %s, state: %s, mac: %s, ip: %s, namespace: %s, options: %s)" \
               % (self.name, self.index, self.type, self.mtu, self.state, self.mac, self.ip, self.namespace, self.options)


class IpAddressInterface(NetworkElement):
    def __init__(self, name, index, mtu, state, mac=None, ip=None, namespace=None):
        NetworkElement.__init__(self, name)
        self.index = index
        self.mtu = mtu
        self.state = state
        self.mac = mac
        self.ip = ip
        self.namespace = namespace

    def setmac(self, mac):
        self.mac = mac

    def setip(self, ip):
        self.ip = ip

    def __str__(self):
        return "IpAddressInterface(name: %s, index: %s, mtu: %s, state: %s, mac: %s, ip: %s, namespace: %s)" \
               % (self.name, self.index, self.mtu, self.state, self.mac, self.ip, self.namespace)


class OVSInterface(NetworkElement):
    def __init__(self, name, options={}):
        NetworkElement.__init__(self, name)
        self.options = options

    def updateoption(self, key, value):
        self.options[key] = value

    def __str__(self):
        return "\t\tOVSInterface %s\n\t\t\t%s" % (self.name, self.options)


class OVSPort(NetworkElement):
    def __init__(self, name, interfaces=[], options={}):
        NetworkElement.__init__(self, name)
        self.interfaces = interfaces
        self.options = options

    def addinterface(self, interface):
        self.interfaces.append(interface)

    def updateoption(self, key, value):
        self.options[key] = value

    def __str__(self):
        interfaces_str = ""
        for interface in self.interfaces:
            interfaces_str += "\n" + interface.__str__()
        return "\tOVSPort %s\n\t\t%s%s" % (self.name, self.options, interfaces_str)


class OVSBridge(NetworkElement):
    def __init__(self, name, ports=[], options={}):
        NetworkElement.__init__(self, name)
        self.ports = ports
        self.options = options

    def addport(self, port):
        self.ports.append(port)

    def updateoption(self, key, value):
        self.options[key] = value

    def __str__(self):
        ports_str = ""
        for port in self.ports:
            ports_str += "\n" + port.__str__()
        return "OVSBridge %s\n\t%s%s" % (self.name, self.options, ports_str)


class LinuxBridge(NetworkElement):
    def __init__(self, name, id, stp, nics, namespace=None):
        NetworkElement.__init__(self, name)
        self.id = id
        self.stp = stp
        self.nics = nics
        self.namespace = namespace


class Route():
    def __init__(self, net, device, src):
        self.net = net
        self.device = device
        self.src = src

    def __str__(self):
        return "Route(net: %s, device %s, src: %s)" % (self.net, self.device, self.src)


class Tunnel():
    def __init__(self, tunId, fromIp, toIp, peerTunId, srcPort, destPort, namespace=None):
        self.tunId = tunId
        self.fromIp = fromIp
        self.toIp = toIp
        self.peerTunId = peerTunId
        self.srcPort = srcPort
        self.destPort = destPort
        self.namespace = namespace


class Session():
    def __init__(self, sessionId, tunId, peerSessionId, peerTunId, iface, namespace=None):
        self.sessionId = sessionId
        self.tunId = tunId
        self.peerSessionId = peerSessionId
        self.peerTunId = peerTunId
        self.iface = iface
        self.namespace = namespace
