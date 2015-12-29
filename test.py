from command_runner import *

print "getOFPort('s1-eth1')"
print getOFPort('s1-eth1')
print

print "dumpFlows('s1')"
print dumpFlows('s1')
print

print "getPhysIfaces()"
print getPhysIfaces()
print

print "getNameSpaces()"
print getNameSpaces()
print

print "isPhysIface('eth0')"
print isPhysIface('eth0')
print "isPhysIface('s1-eth1')"
print isPhysIface('s1-eth1')
print

print "isLoopBack('eth0')"
print isLoopBack('eth0')
print "isLoopBack('lo')"
print isLoopBack('lo')
print

print "getRoutes()"
routes = getRoutes()
for route in routes:
    print route
print

print "getLinuxBridges()"
print getLinuxBridges()
print

print "getLinuxBridgesInAllNS()"
print getLinuxBridgesInAllNS()
print

print "getOVSBridges()"
bridges = getOVSBridges()
for bridge in bridges:
    print bridge
print

print "getIpAddrIfaces()"
ifaces = getIpAddrIfaces()
for iface in ifaces:
    print iface
print

print "getIpAddrIfacesInAllNS()"
ifaces = getIpAddrIfacesInAllNS()
for iface in ifaces:
    print iface
print

print "getAllInterfaces(True)"
ifaces = getAllInterfaces(True)
for iface in ifaces:
    print iface
print

print "getAllInterfaces(False)"
ifaces = getAllInterfaces(False)
for iface in ifaces:
    print iface
print