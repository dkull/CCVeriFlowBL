import math
f = open("../victimtraffic", "r")
for line in f.readlines():
    ip,stats = line.split(">")
    stats = eval(stats)
    print ip,
    hasZero = 0 in stats.values()

    print "hasZero:", hasZero,
    print "hasDrop:", (min(stats.values())/float(max(stats.values()))) < 0.7,
    print "min:", min(stats.values()),
    print "max:", max(stats.values()),
    print "nightRatio:", sum(map(lambda x: stats[x], xrange(1,9)))/float(sum(stats.values())),

    wakeUp = None
    last = None
    for hour,count in stats.items():
        if last == None:
            last = count
            continue
        if count > last*1.5 and hour > 6:
            wakeUp = hour
            break

    print "wakeUp:", wakeUp

f.close()