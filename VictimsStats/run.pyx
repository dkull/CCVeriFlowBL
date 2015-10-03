import fileinput
import sys

goodIps = {}

f = open("victim.ips", "r")
victimips = f.readlines()

for line in victimips:
    goodIps[line[0:-1]] = dict(map(lambda x: [x,0], xrange(0,24)))

print len(goodIps.keys())
count = 0
for line in fileinput.input():
    count += 1
    if count%1000000 == 0:
        print count/1000000, " ",
        sys.stdout.flush()
    splittedLine = filter(lambda x: len(x) > 0, line.split(r' '))
    try:
        hour = int(splittedLine[1].split(":")[0])
    except Exception:
        continue
    ip = None
    ip1 = splittedLine[4].split(":")[0]
    ip2 = splittedLine[6].split(":")[0]

    if ip1 in goodIps:
        ip = ip1
    elif ip2 in goodIps:
        ip = ip2
    else:
        print "NO:", ip1, ip2
    goodIps[ip][hour] += 1

f = open("victimtraffic", "w")

for i,j in goodIps.items():
    f.write(i + ">" + str(j) + "\n")
f.close()
