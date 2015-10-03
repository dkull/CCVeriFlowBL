from dbwrapper import DBWrapper
from fingerprint import FingerPrintMaster
from util import update_progress,printLogBin
import time

class MainClass(object):
    def __init__(self, db):
        self.db = DBWrapper(db)
        self.fingerPrintMaster = []

    def __printGoodIps__(self):
        """
            nfdump -f victim.ips -R ~/Mount/Flows/ -w ~/Mount/victims.netflow -z
        """
        a = self.db.getAllVictimIpTrafficCount()
        print "Writing victim IPs to file"

        f = open("victim.ips","w")
        f.write("ip in [")
        for i,j in a.items():
            if j > 100:
                f.write(i+"\n")
        f.write("]")
        f.close()

    def printStats(self):
        now = time.time()
        print "Flow count: ", len(self.db.getAllFlow())
        print "Victim count: ", len(self.db.getAllVictimIpTrafficCount().keys())
        print "Blacklisted host count: ", len(self.db.getAllBlacklistIp())
        print "Blacklists for dates: ", len(self.db.getAllBlacklistDate())
        print "Flows for dates", len(self.db.getAllFlowDate())
        print "Different blacklist messages: "

        msgs = self.db.getAllBlacklistMsgCount()
        for msg,count in msgs.iteritems():
            print "  ", msg, ' - ', count

        printLogBin(self.db.getAllVictimIpTrafficCount().values(), label="Flows for victim")
        self.__printGoodIps__()
        print "Printing stats took: ", time.time() - now

    def fingerprint(self):
        print "Fingerprinting"
        self.fingerPrintMaster = FingerPrintMaster(self.db)

        """
        allIps = self.db.getAllBlacklistIp()
        ipCount = len(allIps)

        print "Fingerprinting blacklisted IPs"
        now = time.time()
        for index,data in enumerate(allIps):
            fingerprint = FingerPrint(data, self.db)
            # Discard fingerprint if not active, eg. not enough flows
            if fingerprint.active:
                self.fingerprints.append(fingerprint)
        print "\nHosts fit for fingerprinting: {0}".format(len(self.fingerprints))
        print "\nTook {0} seconds".format(time.time()-now)
        """


