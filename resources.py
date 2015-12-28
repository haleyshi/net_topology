

class NetworkElement():
    def __init__(self, name):
        self.name = name


class Iface(NetworkElement):
    def __init__(self, name, type, state, mac, addrs, mtu, vlanTag, used, peer, namespace, idx, flags):
        NetworkElement.__init__(self, name)
        self.type = type
        self.state = state
        self.mac = mac
        self.addrs = addrs
        self.mtu = mtu
        self.vlanTag =vlanTag
        self.used = used
        self.peer = peer
        self.namespace = namespace
        self.idx = idx
        self.flags = flags

class OVSInterface(NetworkElement):
    def __init__(self, name, options={}):
        NetworkElement.__init__(self, name)
        self.options = options

    def updateOption(self, key, value):
        self.options[key] = value

    def __str__(self):
        return "\t\tOVSInterface %s\n\t\t\t%s" % (self.name, self.options)


class OVSPort(NetworkElement):
    def __init__(self, name, interfaces=[], options={}):
        NetworkElement.__init__(self, name)
        self.interfaces = interfaces
        self.options = options

    def addInterface(self, interface):
        self.interfaces.append(interface)

    def updateOption(self, key, value):
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

    def addPort(self, port):
        self.ports.append(port)

    def updateOption(self, key, value):
        self.options[key] = value

    def __str__(self):
        ports_str = ""
        for port in self.ports:
            ports_str += "\n" + port.__str__()
        return "OVSBridge %s\n\t%s%s" % (self.name, self.options, ports_str)


class LinuxBridge(NetworkElement):
    def __init__(self, name, id, stp, nics, namespace):
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
    def __init__(self, tunId, fromIp, toIp, peerTunId, srcPort, destPort, namespace):
        self.tunId = tunId
        self.fromIp = fromIp
        self.toIp = toIp
        self.peerTunId = peerTunId
        self.srcPort = srcPort
        self.destPort = destPort
        self.namespace = namespace


class Session():
    def __init__(self, sessionId, peerSessionId, tunId, peerTunId, iface, namespace):
        self.sessionId = sessionId
        self.peerSessionId = peerSessionId
        self.tunId = tunId
        self.peerTunId = peerTunId
        self.iface = iface
        self.namespace = namespace
