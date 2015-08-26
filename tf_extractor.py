from subprocess import Popen, PIPE
from lineParser import parseLine

def extract(tf_db, bl_db, filterPath):
    print "Reading in traffic"
    folders = [
        ""
    ]
    path = "/home/user/Mount/Flows/"

    pathCombo = []

    for folder in folders:
        pathCombo.append(path+folder)

    popenArgs = ["nfdump","-o","pipe","-f", filterPath, "-R"]
    popenArgs += pathCombo

    print popenArgs
    popen = Popen(popenArgs, stdout=PIPE)

    print "Running"
    flowCount = 0
    # Burn the header
    #print popen.stdout.readline()
    while True:
        nextLine = popen.stdout.readline()
        if nextLine == '' and popen.poll() != None:
            break
        flowCount += 1
        data = parseLine(nextLine)
        if data:
            tf_db.insert(data)
    print "Found matching flows:", flowCount
