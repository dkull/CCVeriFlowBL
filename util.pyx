from __future__ import division
from collections import Counter

def update_progress(current, max):
    progress = int(current/float(max)*100)
    print '\r[{0}{1}] {2}%'.format('#'*(progress), ' '*(100-progress), progress),

def plotTimeseries(values, log=False, lines=5, length=24):
    maxValue = max(values)
    minValue = min(values)
    yValues = []
    step = maxValue/lines

    for value in values:
        print "".format(str()),

def printLogBin(values, label="Unnamed", prop=None):
    print "Printing {0} with {1} values:".format(label, len(values))
    if prop is None:
        values = map(lambda x: len(str(x)), values)
    else:
        values = map(lambda x: len(str(x[prop])), values)

    counter = Counter(values)
    largest = counter.most_common()[0][1]
    maxTrellid = 20.0

    for i in counter.items():
        trellid = int(i[1]/largest*maxTrellid)*"#"
        print "10^{0:5d} => {1:5d} {2}".format(int(i[0])-1, i[1], trellid)
