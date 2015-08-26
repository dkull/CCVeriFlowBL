import tf_extractor
import bl_extractor
from blindex import WithIPIndex,WithDateIndex
from tfindex import WithPartyIndex

def attachBlIndex(bl_db):
    try:
        print "Adding BL_IP index"
        bl_db.add_index(WithIPIndex(bl_db.path, 'ip'), create=True)
    except Exception as e:
        print e

    try:
        print "Adding BL_Date index"
        bl_db.add_index(WithDateIndex(bl_db.path, 'date'), create=True)
    except Exception as e:
        print e

    try:
        print "Adding BL_DatesForIP index"
        bl_db.add_index(WithDateIndex(bl_db.path, 'date'), create=True)
    except Exception as e:
        print e

def attachTfIndex(tf_db):
    try:
        print "Adding TF_Party index"
        tf_db.add_index(WithPartyIndex(tf_db.path, 'srcip'), create=True)
    except Exception as e:
        print e

def populateBl(tf_db, bl_db, nfdumpFilterPath):
    print "Populating BL_DB"
    bl_extractor.extract(bl_db)

def populateTf(tf_db, bl_db, nfdumpFilterPath):
    print "Populating TF_DB"
    tf_extractor.extract(tf_db, bl_db, nfdumpFilterPath)

def generateNfdumpFilter(bl_db, filterPath):
    print "Generating nfdump filter"
    ipCount = 0
    string = ""
    string += "ip in ["

    usedIps = {}
    duplicateIps = 0

    for ip in bl_db.all('ip'):
        if ip["key"] in usedIps:
            duplicateIps += 1
            continue
        usedIps[ip["key"]] = True
        ipCount += 1
        string += ip["key"] + " "
    string += "]"

    f = open(filterPath, 'w')
    f.write(string)
    f.close()

    print "Wrote IPs to filter file: ", ipCount
    print "Duplicates dropped:", duplicateIps

