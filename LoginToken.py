# -*- coding: utf-8 -*-

import LINET
from LINET.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,os,codecs,threading,glob,re
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from ttypes import LoginRequest
import json, requests, LineService

with open('token.json', 'r') as fp:
    akun = json.load(fp)
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
cl = LINET.LINE()
if akun['token1'] == "":
    cl.login(qr=True)
else:
    cl.login(token=akun['token1'])
cl.loginResult()


ki = kk = kc = cl 

nama1 = 'WIN'
Headers = {
        'User-Agent': "Line/8.3.3",
        'X-Line-Application': "DESKTOPWIN\t8.3.0RFU-BOT\t18.99",
        "x-lal": "ja-US_US",
    }

nama2 = 'MAC'   
Headers2 = {
        'User-Agent': "Line/8.4.1 iPad4,1 9.0.2",
        'X-Line-Application': "DESKTOPMAC 10.10.5-YOSEMITE-x64    MAC 10.8.5",
        "x-lal": "ja-US_US",
    }
    
print ("login success")


helpMessage1 ="""╠══[Command Login]
╠══[Header 1 WIN ]
╠[1]loginwin [ no jumlah ]
╠══[Header 2 MAC ]
╠[2]loginmac [ no jumlah ]
╠══[Finish]

╠══[Command admin ]
╠[3] .staff
╠[4] .help
╠[5] .headers
╠[6] .groups
╠[7] .invite
╠[8] .@bye
╠[9] .ping
╠[10] .say 
╠══[Finish]

╠══[Command owner]
╠[11] .reboot
╠[12] .admin:on @
╠[13] .expel:on @
╠[14] .staff
╠[15] .headers
╠[16] .leave allgroups
╠══[Finish]
╠══[Bot Login v1.0]
"""

helpMessage2 ="""╠══[Headers]
╠[WIN header 1 ]
╠[UA = Line/8.3.3]
╠[LA = DESKTOPWIN\t8.3.0RFU-BOT\t18.99]
╠══[Finish]

╠[MAC  header 2 ]
╠[UA = Line/8.4.1 iPad4,1 9.0.2]
╠[LA = DESKTOPMAC 10.10.5-YOSEMITE-x64    MAC 10.8.5]
╠══[Finishi
"""
KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid]
creator =["u78643d09e42a36836a17cc918963a8b7"]
admin=["u78643d09e42a36836a17cc918963a8b7"]
wait = {

    'leaveRoom':True,
    'autoAdd':True,
    'autoJoin':True,
    'addadmin':False,
    'deladmin':False,
    'message':"Thanks for add me\n by TΣΔM SLΔCҜβΩT\nOwner: line.me/ti/p/~fuck.you__",
    "lang":"JP",
    }
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
                    
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in creator+admin:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print ("autoJoin is Off")
            
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
        if op.type == 26:
            msg = op.message
            if msg.text in [".help"]:
              if msg.from_ in creator+admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage1)
                    
        if op.type == 26:
            msg = op.message
            if msg.text in [".headers"]:
              if msg.from_ in creator+admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)    

                    
            #____________________REBOOT_________________________________
            elif msg.text.lower().startswith(".reboot"):
             if msg.from_ in creator+admin:
              print ("[Command]Reboot")
              try:
                 cl.sendText(msg.to,"I'Il come back later")
                 cl.sendText(msg.to,"Restarted done ")
                 restart_program()
              except:
                 cl.sendText(msg.to,"Please wait")
                 restart_program()
                 pass

#______________________________                             
            elif msg.text.lower().startswith(".admin:on "):
                if msg.from_ in creator:
                  if msg.toType == 2:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                     for target in targets:
                        try:
                            admin.append(target)
                            f=codecs.open('st2__admin.json','w','utf-8')
                            json.dump([admin], f, sort_keys=True, indent=4,ensure_ascii=False)
                            jp = cl.getContact(target).displayName
                            jp1 = cl.getContact(msg.from_).displayName
                            cl.sendText(msg.to,jp + " has been promoted admin by "+jp1)
                        except:
                             pass
                             
                             
   #______________________________                             
            elif msg.text.lower().startswith(".expel:on "):
                if msg.from_ in creator:
                  if msg.toType == 2:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                     for target in targets:
                        try:
                            admin.remove(target)
                            f=codecs.open('st2__admin.json','w','utf-8')
                            json.dump([admin], f, sort_keys=True, indent=4,ensure_ascii=False)
                            jp = cl.getContact(target).displayName
                            jp1 = cl.getContact(msg.from_).displayName
                            cl.sendText(msg.to,jp + " has been expelled admin by "+jp1)
                        except:
                             pass                          
                             
#_______________STAFF_________
            elif msg.text.lower().startswith(".staff"):         
             if msg.from_ in creator+admin:
              if creator == []:
              	if admin == []:
                    cl.sendText(msg.to,"Not stafflist")	
              num=0
              mc1 = ""
              for mi_d in admin:
                          mc1 += "%i - %s\n" % (num, cl.getContact(mi_d).displayName)
                          num=(num+1)
              mc2 = ""
              for mi_d in creator:
                          mc2 += "%i - %s\n" % (num, cl.getContact(mi_d).displayName)
                          num=(num+1)
              cl.sendText(msg.to,"Admins :\n\n" + mc1 + "\nOwners :\n\n" + mc2 + "\n\nBot Login v1.0")
              print ("[Command]Stafflist executed")
                             
#______________LOGIN WIN ____________________
            elif msg.text.lower().startswith("loginwin"):
              if msg.from_ in creator+admin:
                separate = msg.text.split(" ")
                jmlh = int(separate[1])
                for x in range(jmlh):
                    Headers.update({'x-lpqs' : '/api/v4/TalkService.do'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName=nama1)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    cl.sendText(msg.to,"Starting white true")
                    cl.sendText(msg.to,"Except")
                    cl.sendText(msg.to,str(link))
                    Headers.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers).text)
                    Headers.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                else:
                    cl.sendText(msg.to, "The bot has been mmade with header 1")
                    cl.sendText(msg.to,str(res.authToken))
					
#______________LOGIN MAC____________________
            elif msg.text.lower().startswith("loginmac"):
              if msg.from_ in creator+admin:
                separate = msg.text.split(" ")
                jmlh = int(separate[1])
                for x in range(jmlh):
                    Headers2.update({'x-lpqs' : '/api/v4/TalkService.do'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName=nama2)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    cl.sendText(msg.to,"Starting white true")
                    cl.sendText(msg.to,"Except")
                    cl.sendText(msg.to,str(link))
                    Headers2.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers2).text)
                    Headers2.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                else:
                    cl.sendText(msg.to, "The bot has been mmade with header 2")
                    cl.sendText(msg.to,str(res.authToken))
                
#_________________BYE BOT________________________
            elif msg.text.lower().startswith(".@bye"):
              if msg.from_ in creator+admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye "  +  str(ginfo.name))
                        cl.leaveGroup(msg.to)
                    except:
                      pass
 #________________INVITE VIA NO ____________
            elif msg.text.lower().startswith(".invite "):
                  if msg.from_ in creator+admin:
                    nomor = msg.text.replace(".invite ","")
                    G = cl.getGroupIdsJoined()
                    cgroup = cl.getGroups(G)
                    for x in range(len(cgroup)):
                       try:
                          if nomor == str(x):
                           gid = cgroup[x].id
                           gname = cgroup[x].name
                           cl.inviteIntoGroup(gid, [msg.from_])
                           cl.sendText(msg.to,"Invited to %s"%(gname))
                           print (gid)
                       except Exception as error:     
                           cl.sendText(msg.to,"Failed")
                       except:
                           pass 

 #________________CEK GROUP____________________
            elif msg.text.lower().startswith(".groups"):
              if msg.from_ in creator+admin:
                    G = cl.getGroupIdsJoined()
                    cgroup = cl.getGroups(G)
                    ngroup = ""
                    for x in range(len(cgroup)):
                       ngroup += "\n"+ str(x) +" - " + cgroup[x].name + " ( " + str(len(cgroup[x].members)) + " )"
                    pass
                    cl.sendText(msg.to,"List Group:\n%s\n\nTotal Group: %s"%(ngroup,str(len(cgroup))))

#___________________MY GROUP______________________________        
            elif msg.text.lower().startswith(".mygroups"):
              if msg.from_ in creator:
                   gid = cl.getGroupIdsJoined()
                   num=1
                   h = ""
                   for i in gid:
                    h += " %i. %s\n" % (num, cl.getGroup(i).name +" ("+str(len(cl.getGroup(i).members))+")")
                    num=(num+1)
                    jp1 = cl.getContact(msg.from_).displayName
                   cl.sendText(msg.to,"Groups : " + jp1 +"\n\n"+ h +"\nTotal Groups  = " +""+str(len(gid))+"")
 
            elif msg.text.lower().startswith(".leave allgroups"):
             if msg.from_ in creator:
               gid = cl.getGroupIdsJoined()
               for i in gid:
               	cl.leaveGroup(i)
               
   #_________________SAY_____________________                
            elif msg.text.lower().startswith(".say "):
              if msg.from_ in creator+admin:
                bctxt = msg.text.replace(".say ","")
                cl.sendText(msg.to,(bctxt))

   #______________RESPONSENAME_________________________
            elif msg.text.lower().startswith(".ping"):
              if msg.from_ in creator+admin:
                cl.sendText(msg.to,"pong")  

        if op.type == 59:
            print (op)


    except Exception as error:
        print (error)

while True:
  try:
    try:
        Ops = cl.fetchOperation(cl.Poll.rev, 10)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
        
    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)      
         
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()  
