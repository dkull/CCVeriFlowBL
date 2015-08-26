def update_progress(current, max):
    progress = int(current/float(max)*100)
    print '\r[{0}{1}] {2}%'.format('#'*(progress), ' '*(100-progress), progress),