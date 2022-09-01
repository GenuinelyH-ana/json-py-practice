# commented lines are for debugging

import os
import json

# print(os.getcwd())
with open("information.json") as f:
    info = json.load(f)

memberList = set()

for i in info.keys():
    if i not in ["serverName", "population"]:
        #print(i)
        #print(info[i])
        #print()
        if type(info[i]) == list:
            # print(str(info[i]))
            for i2 in (info[i]):
                #print(i2)
                memberList.add(i2)
        else:
            memberList.add(str(info[i]))
#print()
# print(memberList)
#print()

memberList = list(memberList)
# print(memberList)

def vibeCheck(user):
    def onOfflineC(user):
        if user in info.get("Online"):
            return "is online, "
        elif user in info.get("Offline"):
            return "is offline, "
        else:
            return "is of unknown status, "
    def isViewer(user):
        if user in info.get("streamViewers"):
            return "is watching the stream right now, "
        if user == "genuinelyHana":
            return "is the person currently streaming right now, "
        else:
            return ""
    def isArtist(user):
        if user in info.get("Artist"):
            return "is an artist, "
        else: 
            return ""
    def roleStatus(user):
        if user in info.get("HROC"):
            return " is also part of the HRO Council."
        elif user in info.get("registeredMembers"):
            return " is a registered member."
        elif user in info.get("Visitors"):
            return " is a visitor."
        else:
            return ""
    return "Info on "+str(user)+".\nThis person "+str(onOfflineC(user))+str(isViewer(user))+str(isArtist(user))+"and"+str(roleStatus(user))

for person in memberList:
    print(vibeCheck(person))
    print()
