# ~/Desktop/Blacklists $ find ./ -name "emergingthreats_botcc.txt" | python ~/PycharmProjects/Flowy/bl_extractor.py

import fileinput
import re
import config
import os

def extract(db):
    print "Reading in blacklists"
    inputFiles = []
    insertCount = 0

    for root,dirs,files in os.walk(config.blacklistsPath):
        for includedFile in config.includedBlacklists:
            if includedFile not in files:
                continue
            inputFiles.append(root+"/"+includedFile)

    for blacklist in inputFiles:
        f = open(blacklist)
        content = f.read()
        f.close()

        # Parse date from path
        date = re.findall("\d\d\.\d\d", blacklist)[0]

        for fileline in content.split("\n"):
            if len(fileline) and fileline[0] == "#":
                continue

            msg = re.findall(r"msg:\"(.*?)\"", fileline)
            if not len(msg):
                continue
            msg = re.sub(r"\d", "X", msg[0])
            ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", fileline)
            for ip in ips:
                insertCount += 1
                db.insert({
                    "date":date,
                    "msg":msg,
                    "ip":ip
                })
    print "Parsed input files:", len(inputFiles)
    print "Inserted IPs: ", insertCount
