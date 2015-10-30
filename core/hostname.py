import os
import platform


# This script gets the ip code of the machine it is running on
# if it is connected to internet

def printl(l):
    for i in range(len(l)):
        print l[i]


# Mac-like systems
# noinspection PyShadowingNames
def get_darwin_ip():
    l = os.popen("ifconfig | grep inet").read().split('\n')
    inet_list = []
    for i in range(len(l)):
        l[i] = l[i].strip('\t')
        if (l[i][0:5] == 'inet ') and (l[i][5:8] != '127'):
            inet_list.append(l[i])
    if len(inet_list) == 1:
        inet = inet_list[0]
        inet = inet.split(' ')
        ip = inet[1]
        print "Found ip: {}".format(ip)
        return ip
    else:
        return None


# Linux systems
# noinspection PyShadowingNames
def get_linux_ip():
    l = os.popen("ifconfig | grep inet").read().split('\n')
    for i in range(len(l)):
        l[i] = l[i].strip(' ').split(' ')
        l[i].pop(0)
    l.pop(-1)
    inet = []
    for i in range(len(l)):
        if l[i][0][0:5] == 'inet:':
            inet.append(l[i])
    for i in range(len(inet)):
        ip = inet[i][0].split(':')
        if ip[1][0:3] != '127':
            print "Found ip: {}".format(ip[1])
            break
        return None
    return ip[1]


# noinspection PyShadowingNames
def find_ip():
    print "Looking for an ip..."
    if platform.system() == "Darwin":
        ip = get_darwin_ip()
    elif platform.system() == "Linux":
        ip = get_linux_ip()
    else:
        print "Platform not yet supported."
    if ip is None:
        print "No ip found."
        print "Either you are not online or there are some problems with your connection."
        return None
    return ip


# noinspection PyShadowingNames
def ip_encode(ip):
    if ip is not None:
        ip = ip.split('.')
        print ip
        ip_secure = []
        ip_pass = []
        for i in range(len(ip)):
            ip_secure.append(str(float(ip[i]) / float(ip[i][-1])))
            ip_pass.append(ip[i][-1])
        print "IP successfylly encoded: ", ip_secure, "with", ip_pass
        return [ip_secure, ip_pass]
    else:
        print "No ip to encode."
        return None


# noinspection PyShadowingNames,PyShadowingNames
def ip_decode(ip_secured):
    if ip_secured is not None:
        ip = ip_secured[0]
        ip_pass = ip_secured[1]
        ip_decoded = []
        for i in range(len(ip)):
            ip_decoded.append(str(int(round(float(ip[i]) * float(ip_pass[i]), 0))))
        print ip_decoded
    else:
        print "No ip to decode"
        return None


# noinspection PyNoneFunctionAssignment
if __name__ == '__main__':
    ip = raw_input("To test funcionality write a random ip, else just press enter: ") or find_ip()
    # noinspection PyNoneFunctionAssignment
    ip_encoded = ip_encode(ip)
    # noinspection PyNoneFunctionAssignment
    ip_decoded = ip_decode(ip_encoded)
