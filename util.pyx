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
