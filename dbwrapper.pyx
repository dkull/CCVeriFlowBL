from tables import *

class BlacklistEntry(IsDescription):
    ip = StringCol(15)
    msg = StringCol(40)
    date = StringCol(10)

class FlowEntry(IsDescription):
    timestamp_s = UInt32Col()
    year = UInt16Col()
    month = UInt8Col()
    day = UInt8Col()
    hour = UInt8Col()
    minute = UInt8Col()
    second = UInt8Col()
    duration = UInt32Col()
    proto = UInt8Col()
    srcip = StringCol(15)
    srcport = UInt16Col()
    dstip = StringCol(15)
    dstport = UInt16Col()
    bytes = UInt32Col()

def collector(x, colnames, field):
    if type(field) == str:
        return x[field]
    elif type(field) == list:
        output = {}
        for i in field:
            output[i] = x[i]
        return output
    else:
        output = {}
        for i in colnames:
            output[i] = x[i]
        return output

class DBWrapper(object):
    def __init__(self, db):
        self._db = db
        self.db_group = db.root.group
        self.bl_db = self.db_group.Blacklist
        self.fl_db = self.db_group.Flows

    # Internal
    def _getQuery(self, db, query=None, field=None):
        if query:
            queryPart = db.where(query)
        else:
            queryPart = db.iterrows()
        columnNames = db.colnames[0:]
        result = [collector(x, columnNames, field) for x in queryPart]

        """if query:
            if field:
                return [x[field] for x in db.where(query)]
            else:
                return [x.fetch_all_fields() for x in db.where(query)]
        else:
            if field:
                return [x[field] for x in db.iterrows()]
            else:
                return [x.fetch_all_fields() for x in db.iterrows()]
        """

        return result

    # Internal
    def _getBlacklist(self, query=None, field=None):
        return self._getQuery(self.bl_db, query, field)

    # Internal
    def _getFlow(self, query=None, field=None):
        return self._getQuery(self.fl_db, query, field)

    #
    # These are for stats mostly
    #
    def getAllBlacklistIp(self):
        return set(self._getBlacklist(field='ip'))

    def getAllBlacklistDate(self):
        return set(self._getBlacklist(field='date'))

    def getAllBlacklistMsgCount(self):
        items = self._getBlacklist()
        dict = {}
        ipsused = {}
        for i in items:
            ip = i["ip"]
            msg = i["msg"]
            if ip in ipsused:
                continue
            else:
                ipsused[ip] = True

            if msg in dict:
                dict[msg] += 1
            else:
                dict[msg] = 1

        return dict

    def getAllFlow(self):
        return self._getFlow()

    def getAllFlowDate(self):
        date_data = self._getFlow(field=['year', 'month', 'day'])
        return set(map(lambda x: tuple(x.values()), date_data))

    #
    # These are for fingerprinting
    #

    def getIpFlows(self, ip):
        query = "(srcip == '{0}') | (dstip == '{0}')".format(ip)
        return self._getQuery(self.fl_db,query=query)

    def getMsgsForIp(self, ip):
        query = "ip == '{0}'".format(ip)
        return set(self._getBlacklist(field='msg',query=query))
