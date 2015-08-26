class FingerPrint(object):
    def __init__(self, ip, db):
        self.active = False
        self.flowCount = -1
        self.ip = ip
        self.msgs = []
        self.contactPoints = []
        self.others = []
        self.largestExchange = 0
        self.dominantExchange = 0
        self.normalizedTraffic = []
        self.myPorts = []
        self.otherPorts = []
        # Via ports
        self.longRunningSessions = []

        self._toggleActive(db)
        if not self.active:
            return

        self._getMsgs(db)
        self._calcContactPoints(db)
        self._calcLargestExchange(db)
        self._calcDominantExchange(db)
        self._calcNormalizedTraffic(db)
        self._calcPorts(db)
        self._calcLongRunningSessions(db)

    def _toggleActive(self, db):
        myFlows = db.getIpFlows(self.ip)
        self.flowCount = len(myFlows)
        if self.flowCount > 100:
            self.active = True

    def _getMsgs(self, db):
        self.msgs = db.getMsgsForIp(self.ip)

    def _calcContactPoints(self, db):
        myIP = self.ip
        for entry in db.getIpFlows(self.ip):
            otherIp = None
            otherPort = None
            if entry['srcip'] == myIP:
                otherIp = entry['dstip']
                otherPort = entry['dstport']
            else:
                otherIp = entry['srcip']
                otherPort = entry['srcport']

            self.others.append(otherIp)
            self.contactPoints.append((otherIp,otherPort))
        self.others = set(self.others)
        self.contactPoints = set(self.contactPoints)

    def _calcLargestExchange(self, db):
        myIP = self.ip
        maxBytes = 0
        for entry in db.getIpFlows(self.ip):
            currBytes = entry['bytes']
            if currBytes > maxBytes:
                maxBytes = currBytes

    def _calcDominantExchange(self, db):
        byteOccurance = {-1: -1}
        for entry in db.getIpFlows(self.ip):
            currBytes = entry['bytes']
            if currBytes not in byteOccurance:
                byteOccurance[currBytes] = 1
            else:
                byteOccurance[currBytes] += 1

        mostUsedBytes = max(byteOccurance.values())

        self.dominantExchange = mostUsedBytes

    def _calcNormalizedTraffic(self, db):
        pass

    def _calcPorts(self, db):
        myIP = self.ip
        for entry in db.getIpFlows(self.ip):
            if entry['srcip'] == myIP:
                myPort = entry['srcport']
                otherPort = entry['dstport']
            else:
                myPort = entry['dstport']
                otherPort = entry['srcport']
            self.myPorts.append(myPort)
            self.otherPorts.append(otherPort)
        self.myPorts = set(self.myPorts)
        self.otherPorts = set(self.otherPorts)

    def _calcLongRunningSessions(self, db):
        pass

    def __repr__(self):
        return "cntcpt:{0: 7d} oth:{1: 7d} fls:{2: 7d} myp:{3: 7d} otp:{4: 7d} msg:{5}".format(len(self.contactPoints), len(self.others), self.flowCount, len(self.myPorts), len(self.otherPorts), self.msgs)
