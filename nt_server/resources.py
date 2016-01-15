
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

