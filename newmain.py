from tables import *

import datetime
import time
import config
from CodernityDB.database import Database


def numToDottedQuad(n):
    "convert long int to dotted quad string"

    d = 256 * 256 * 256
    q = []
    while d > 0:
        m,n = divmod(n,d)
        q.append(str(m))
        d = d/256

    return '.'.join(q)

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

if True:
    pass
    """h5file = open_file("ccflow.db", mode="w", title="CC flows and BL")
    group = h5file.create_group("/", "group", "All things")
    table = h5file.create_table(group, "Blacklist", BlacklistEntry, "Blacklist entries")

    bl_db = Database(config.bldb)
    bl_db.open()
    for entry in bl_db.all('ip', with_doc=True):
        db_entry = table.row
        db_entry['ip'] = entry['doc']['ip']
        db_entry['date'] = entry['doc']['date']
        db_entry['msg'] = entry['doc']['msg']
        db_entry.append()
    table.cols.date.create_index()
    table.cols.ip.create_index()
    table.flush()
    # Flows
    table = h5file.create_table(group, "Flows", FlowEntry, "Flow entries")

    tf_db = Database(config.tfdb)
    tf_db.open()
    for entry in tf_db.all('srcip', with_doc=True):
        db_entry = table.row
        start_datetime = datetime.datetime.fromtimestamp(float(entry['doc']['timestamp_s']))
        db_entry['timestamp_s'] = int(entry['doc']['timestamp_s'])
        db_entry['duration'] = int(entry['doc']['timestamp_f']) - int(entry['doc']['timestamp_s'])
        db_entry['year'] = start_datetime.year
        db_entry['month'] = start_datetime.month
        db_entry['day'] = start_datetime.day
        db_entry['hour'] = start_datetime.hour
        db_entry['minute'] = start_datetime.minute
        db_entry['second'] = start_datetime.second

        db_entry['srcip'] = numToDottedQuad(int(entry['doc']['srcip']))
        db_entry['srcport'] = entry['doc']['srcport']
        db_entry['dstip'] = numToDottedQuad(int(entry['doc']['dstpip']))
        db_entry['dstport'] = entry['doc']['dstport']
        db_entry['bytes'] = entry['doc']['bytesy']
        db_entry['proto'] = entry['doc']['proto']
        db_entry.append()

    table.cols.timestamp_s.create_index()
    table.cols.duration.create_index()
    table.cols.year.create_index()
    table.cols.month.create_index()
    table.cols.day.create_index()
    table.cols.hour.create_index()
    table.cols.minute.create_index()
    table.cols.second.create_index()

    table.cols.srcip.create_index()
    table.cols.srcport.create_index()
    table.cols.dstip.create_index()
    table.cols.dstport.create_index()
    table.cols.bytes.create_index()
    table.cols.proto.create_index()

    table.flush()
    h5file.close()
    """

h5file = open_file("ccflow.db", mode="a")

print h5file
#bl_table = h5file.root.group.Blacklist.cols.msg.create_index()

for i in h5file.root.group.Blacklist.where("""msg == 'ET CNC Feodoo Tracker Reported CnC Serve'"""):
    i['msg'] = "ET CNC Feodo Tracker Reported CnC Server"
    i.update()
h5file.root.group.Blacklist.flush()
#fl_table = h5file.root.group.Flows

#print [x.fetch_all_fields() for x in fl_table.where("""(month == 5) & (srcport == 6667)""")][0]
#print x.table.colnames
# (93L, 1, '176.46.125.122', 58569, 0L, 0, 4, 5, 6, 24, '217.146.78.110', 6667, 1430427864L, 2015)
h5file.close()