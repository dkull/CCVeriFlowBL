from tables import *
import time
from operator import attrgetter

import pyximport
pyximport.install(pyimport=False)

import Classes

#generate.populateTf(tf_db, bl_db, config.filterPath)
#Skip corrupt data file '/home/user/Mount/Flows/2015-05-25/nfcapd.201505252306'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-29/nfcapd.201506291336'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-29/nfcapd.201506291351'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-29/nfcapd.201506291406'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-29/nfcapd.201506291421'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-29/nfcapd.201506291436'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-30/nfcapd.201506300036'
#Skip corrupt data file '/home/user/Mount/Flows/2015-06-30/nfcapd.201506300051'
#Skip corrupt data file '/home/user/Mount/Flows/2015-07-01/nfcapd.201507010006'
#Skip corrupt data file '/home/user/Mount/Flows/2015-07-02/nfcapd.201507020006'
#Skip corrupt data file '/home/user/Mount/Flows/2015-07-02/nfcapd.201507020021'
#Skip corrupt data file '/home/user/Mount/Flows/2015-07-02/nfcapd.201507020051'
#Skip corrupt data file '/home/user/Mount/Flows/2015-07-03/nfcapd.201507030006'

h5file = open_file("ccflow.db", mode="r")

now = time.time()
mainClass = Classes.MainClass(h5file)
mainClass.printStats()
mainClass.fingerprint()
print "Whole program ran for {0} seconds".format(time.time()-now)

fp = mainClass.fingerprints
fp = sorted(fp, key=attrgetter('flowCount'))
for i in fp:
    print i

h5file.close()