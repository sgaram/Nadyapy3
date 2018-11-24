# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

nadya = LINE()
#nadya = LINE("EzTm9lnDK8ZGq4AbTvIb.3Zg5eTOuWfkqtUnBzihrAW.TNsqP8/nmg67eG/WPI/ab7kjfqtNrTLbUAJrSrWfls4=')
#nadya = LINE("Email","Password")
nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))

ki = LINE()
#ki = LINE("Ez9sVJEKE2cqdmeqh7D8.9b6szpiJ3KHyLZhfedasIa.gZpzYm+MSNTjvsyMZPwL4Xx8apVippJLZ9QdigkJQ1k=')
#ki = LINE("Email","Password")
ki.log("Auth Token : " + str(ki.authToken))
channelToken = ki.getChannelResult()
ki.log("Channel Token : " + str(channelToken))

ki2 = LINE()
#ki2 = LINE("EzHz7KSuv3vCGDhzDXt7.45wCzREf2FA1zn5gJNirDW.MaQ42HIbhrD4OowPOdbJFnVzoMBuFpLMme9bS6zIEx4=")
#ki2 = LINE("Email","Password")
ki2.log("Auth Token : " + str(ki2.authToken))
channelToken = ki2.getChannelResult()
ki2.log("Channel Token : " + str(channelToken))

KAC = [nadya,ki,ki2]

nadyaMID = nadya.profile.mid
kiMID = ki.profile.mid
ki2MID = ki2.profile.mid

Bots = [nadyaMID,kiMID,ki2MID]
creator = ["u9f09cfcb17d037e2936b751bd9d40ead"]
Owner = ["u9f09cfcb17d037e2936b751bd9d40ead"]
admin = ["u9f09cfcb17d037e2936b751bd9d40ead"]

nadyaProfile = nadya.getProfile()
kiProfile = ki.getProfile()
ki2Profile = ki2.getProfile()

lineSettings = nadya.getSettings()
kiSettings = ki.getSettings()
ki2Settings = ki2.getSettings()

oepoll = OEPoll(nadya)
oepoll1 = OEPoll(ki)
oepoll2 = OEPoll(ki2)

responsename = nadya.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = ki2.getProfile().displayName
#==============================================================================#

with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

#if settings["restartPoint"] != None:
#    nadya.sendMessage(settings["restartPoint"], "Bot kembali aktif")
#    settings["restartBot"] = None

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╔═══════════════" + "\n" + \
                  "╠♥ ✿✿✿ NADYA_TJ ✿✿✿ ♥" + "\n" + \
                  "║" + "\n" + \
                  "╠══✪〘 Help Message 〙✪══" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Help 〙✪════════" + "\n" + \
                  "╠➥ Help" + "\n" + \
                  "╠➥ Translate" + "\n" + \
                  "╠➥ Texttospeech" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Protect 〙✪═══════" + "\n" + \
                  "╠➥ Protect 「On/Off」" + "\n" + \
                  "╠➥ QrProtect 「On/Off」" + "\n" + \
                  "╠➥ InviteProtect 「On/Off」" + "\n" + \
                  "╠➥ CancelProtect 「On/Off」" + "\n" + \
                  "╠➥ SetPro 「On/Off」" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Status 〙✪════════" + "\n" + \
                  "╠➥ Restart" + "\n" + \
                  "╠➥ Runtime" + "\n" + \
                  "╠➥ Speed" + "\n" + \
                  "╠➥ Status" + "\n" + \
                  "╠➥ About" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Settings 〙✪═══════" + "\n" + \
                  "╠➥ AutoAdd「On/Off」" + "\n" + \
                  "╠➥ AutoJoin「On/Off」" + "\n" + \
                  "╠➥ AutoLeave「On/Off」" + "\n" + \
                  "╠➥ AutoRead「On/Off」" + "\n" + \
                  "╠➥ CheckSticker「On/Off」" + "\n" + \
                  "╠➥ DetectMention「On/Off」" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Self 〙✪═════════" + "\n" + \
                  "╠➥ Me" + "\n" + \
                  "╠➥ MyMid" + "\n" + \
                  "╠➥ MyName" + "\n" + \
                  "╠➥ MyBio" + "\n" + \
                  "╠➥ MyPicture" + "\n" + \
                  "╠➥ MyVideoProfile" + "\n" + \
                  "╠➥ MyCover" + "\n" + \
                  "╠➥ StealContact「Mention」" + "\n" + \
                  "╠➥ StealMid「Mention」" + "\n" + \
                  "╠➥ StealName「Mention」" + "\n" + \
                  "╠➥ StealBio「Mention」" + "\n" + \
                  "╠➥ StealPicture「Mention」" + "\n" + \
                  "╠➥ StealVideoProfile「Mention」" + "\n" + \
                  "╠➥ StealCover「Mention」" + "\n" + \
                  "╠➥ CloneProfile「Mention」" + "\n" + \
                  "╠➥ RestoreProfile" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Group 〙✪════════" + "\n" + \
                  "╠➥ GroupCreator" + "\n" + \
                  "╠➥ GroupId" + "\n" + \
                  "╠➥ GroupName" + "\n" + \
                  "╠➥ GroupPicture" + "\n" + \
                  "╠➥ GroupTicket" + "\n" + \
                  "╠➥ GroupTicket「On/Off」" + "\n" + \
                  "╠➥ GroupList" + "\n" + \
                  "╠➥ GroupMemberList" + "\n" + \
                  "╠➥ GroupInfo" + "\n" + \
                  "╠➥ Kill「Mention」" + "\n" + \
                  "╠➥ KickAllMember"+ "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Special 〙✪═══════" + "\n" + \
                  "╠➥ Mimic「On/Off」" + "\n" + \
                  "╠➥ MimicList" + "\n" + \
                  "╠➥ MimicAdd「Mention」" + "\n" + \
                  "╠➥ MimicDel「Mention」" + "\n" + \
                  "╠➥ Mention" + "\n" + \
                  "╠➥ Lurking「Oɴ/Off/Reset」" + "\n" + \
                  "╠➥ Lurking" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Media 〙✪════════" + "\n" + \
                  "╠➥ Kalender" + "\n" + \
                  "╠➥ CheckDate「Date」" + "\n" + \
                  "╠➥ InstagramInfo「UserName」" + "\n" + \
                  "╠➥ InstagramPost「UserName」" + "\n" + \
                  "╠➥ SearchYoutube「Search」" + "\n" + \
                  "╠➥ SearchMusic「Search」" + "\n" + \
                  "╠➥ SearchLyric「Search」" + "\n" + \
                  "╠➥ SearchImage「Search」" + "\n" + \
                  "╠➥ ScreenshootWebsite「LinkUrl」" + "\n" + \
                  "║" + "\n" + \
                  "╠✪〘 Bot 〙✪═════════" + "\n" + \
                  "╠➥ AdminAdd" + "\n" + \
                  "╠➥ AdminDel" + "\n" + \
                  "╠➥ AdminList" + "\n" + \
                  "╠➥ OwnerAdd" + "\n" + \
                  "╠➥ OwnerDel" + "\n" + \
                  "╠➥ OwnerList" + "\n" + \
                  "╠➥ BanContact" + "\n" + \
                  "╠➥ UnbanContact" + "\n" + \
                  "╠➥ BanList" + "\n" + \
                  "╠➥ ClearBan" + "\n" + \
                  "╠➥ Respon" + "\n" + \
                  "╠➥ Absen" + "\n" + \
                  "╠➥ JoinAll" + "\n" + \
                  "╠➥ ByeAll" + "\n" + \
                  "║" + "\n" + \
                  "╚═〘 Credits By: ©Nadya_TJ™  〙"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔══〘 T E X T   T O   S P E E C H 〙" + "\n" + \
                         "╠ af : Afrikaans" + "\n" + \
                         "╠ sq : Albanian" + "\n" + \
                         "╠ ar : Arabic" + "\n" + \
                         "╠ hy : Armenian" + "\n" + \
                         "╠ bn : Bengali" + "\n" + \
                         "╠ ca : Catalan" + "\n" + \
                         "╠ zh : Chinese" + "\n" + \
                         "╠ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠ hr : Croatian" + "\n" + \
                         "╠ cs : Czech" + "\n" + \
                         "╠ da : Danish" + "\n" + \
                         "╠ nl : Dutch" + "\n" + \
                         "╠ en : English" + "\n" + \
                         "╠ en-au : English (Australia)" + "\n" + \
                         "╠ en-uk : English (United Kingdom)" + "\n" + \
                         "╠ en-us : English (United States)" + "\n" + \
                         "╠ eo : Esperanto" + "\n" + \
                         "╠ fi : Finnish" + "\n" + \
                         "╠ fr : French" + "\n" + \
                         "╠ de : German" + "\n" + \
                         "╠ el : Greek" + "\n" + \
                         "╠ hi : Hindi" + "\n" + \
                         "╠ hu : Hungarian" + "\n" + \
                         "╠ is : Icelandic" + "\n" + \
                         "╠ id : Indonesian" + "\n" + \
                         "╠ it : Italian" + "\n" + \
                         "╠ ja : Japanese" + "\n" + \
                         "╠ km : Khmer (Cambodian)" + "\n" + \
                         "╠ ko : Korean" + "\n" + \
                         "╠ la : Latin" + "\n" + \
                         "╠ lv : Latvian" + "\n" + \
                         "╠ mk : Macedonian" + "\n" + \
                         "╠ no : Norwegian" + "\n" + \
                         "╠ pl : Polish" + "\n" + \
                         "╠ pt : Portuguese" + "\n" + \
                         "╠ ro : Romanian" + "\n" + \
                         "╠ ru : Russian" + "\n" + \
                         "╠ sr : Serbian" + "\n" + \
                         "╠ si : Sinhala" + "\n" + \
                         "╠ sk : Slovak" + "\n" + \
                         "╠ es : Spanish" + "\n" + \
                         "╠ es-es : Spanish (Spain)" + "\n" + \
                         "╠ es-us : Spanish (United States)" + "\n" + \
                         "╠ sw : Swahili" + "\n" + \
                         "╠ sv : Swedish" + "\n" + \
                         "╠ ta : Tamil" + "\n" + \
                         "╠ th : Thai" + "\n" + \
                         "╠ tr : Turkish" + "\n" + \
                         "╠ uk : Ukrainian" + "\n" + \
                         "╠ vi : Vietnamese" + "\n" + \
                         "╠ cy : Welsh" + "\n" + \
                         "╚══〘 Jangan Typo 〙" + "\n" + "\n\n" + \
                          "Contoh : say-en Nadya Cantik"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══〘 T R A N S L A T E 〙" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══〘 Jangan Typo 〙" + "\n" + "\n\n" + \
                         "Contoh : tr-en Nadya Cantik"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                nadya.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(nadya.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            if settings["autoJoin"] == True:
                if settings["autoReject"]["status"] == True:
                    if len(group.members) > settings["autoReject"]["members"]:
                        nadya.acceptGroupInvitation(op.param1)
                    else:
                        nadya.rejectGroupInvitation(op.param1)
                else:
                    nadya.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = nadya.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))

            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   List User Invited : {}".format(str(listContact))
            print (arg)
                
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            group = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   User Join : {}".format(str(contact.displayName))
            print (arg)
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        nadya.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        nadya.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 26:
            print ("[ 26 ] SEND MESSAGE COMMAND")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    nadya.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    nadya.sendMessage(to, str(helpTranslate))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    nadya.sendMessage(to, "Please Wait...")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  if msg._from in Owner:    
                    nadya.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    nadya.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u14f64e139a3817afaabe27d237afb36b"
                        creator = nadya.getContact(owner)
                        contact = nadya.getContact(nadyaMID)
                        grouplist = nadya.getGroupIdsJoined()
                        contactlist = nadya.getAllContactIds()
                        blockedlist = nadya.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ Dilarang Remake Tanpa Ijin :P ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["protect"] == True: ret_ += "\n╠ Protect ✅"
                        else: ret_ += "\n╠ Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ Qr Protect ✅"
                        else: ret_ += "\n╠ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Invite Protect ✅"
                        else: ret_ += "\n╠ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n╠ Cancel Protect ✅"
                        else: ret_ += "\n╠ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
                    
                elif msg.text.lower().startswith("ownerdel "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                    if msg._from in Owner:
                        if Owner == []:
                            nadya.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            nadya.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠♥ ✿✿✿ NADYA_TJ ✿✿✿ ♥\n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +nadya.getContact(mi_d).displayName + "\n"
                            nadya.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~nad_nad. 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                    if msg._from in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                nadya.sendMessage(msg.to,"Added Target Fail !")
                                break
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
                    
                elif msg.text.lower().startswith("admindel "):
                    if msg._from in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                nadya.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                    else:
                        nadya.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                    if msg._from in Owner:
                        if admin == []:
                            nadya.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            nadya.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠♥ ✿✿✿ NADYA_TJ ✿✿✿ ♥\n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +nadya.getContact(mi_d).displayName + "\n"
                            nadya.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 line.me/ti/p/~nad_nad. 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                    if msg._from in Owner:
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Already On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Set To On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Already On")
                                
                elif text.lower() == 'protect off':
                    if msg._from in Owner:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Set To Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Already Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                    if msg._from in Owner:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Qr Already On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Qr Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                    if msg._from in Owner:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Qr Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Invite Already On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Invite Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'setpro on':
                    if msg._from in Owner:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        nadya.sendMessage(msg.to,"➲ All Protect Set To On")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'setpro off':
                    if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        nadya.sendMessage(msg.to,"➲ All Protect Set To Off")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                  if msg._from in Owner:    
                    settings["autoJoin"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                  if msg._from in Owner:
                    settings["autoLeave"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
                  if msg._from in Owner:
                    settings["autoLeave"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'autojoinlink on':
                    settings["autoJoinTicket"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'autojoinlink off':
                    settings["autoJoinTicket"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif text.lower() == "respon":
                    nadya.sendMessage(msg.to,responsename)
                    ki.sendMessage(msg.to,responsename2)
                    ki2.sendMessage(msg.to,responsename3)
                    
                elif msg.text.lower() == 'absen':
                    if msg._from in Owner:
                        nadya.sendContact(to, nadyaMID)
                        ki.sendContact(to, kiMID)
                        ki2.sendContact(to, ki2MID)

                elif text.lower() in ["byeall"]:
                  if msg._from in Owner:    
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)

                elif text.lower() in ["joinall"]:
                  if msg._from in Owner:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)

                elif text.lower() == 'me':
                    sendMessageWithMention(to, nadyaMID)
                    nadya.sendContact(to, nadyaMID)
                elif text.lower() == 'mymid':
                    nadya.sendMessage(msg.to,"[MID]\n" +  nadyaMID)
                elif text.lower() == 'myname':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = nadya.getContact(nadyaMID)
                    cover = nadya.getProfileCoverURL(nadyaMID)    
                    nadya.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        nadya.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.nadya.naver.jp/" + nadya.getContact(ls).pictureStatus + "/vp"
                            nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = nadya.getProfileCoverURL(ls)
                                nadya.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                  if msg._from in Owner:    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            nadya.cloneContactProfile(contact)
                            nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            nadya.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  if msg._from in Owner:    
                    try:
                        nadyaProfile.displayName = str(myProfile["displayName"])
                        nadyaProfile.statusMessage = str(myProfile["statusMessage"])
                        nadyaProfile.pictureStatus = str(myProfile["pictureStatus"])
                        nadya.updateProfileAttribute(8, nadyaProfile.pictureStatus)
                        nadya.updateProfile(nadyaProfile)
                        nadya.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        nadya.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            nadya.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            nadya.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            nadya.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            nadya.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        nadya.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+nadya.getContact(mi_d).displayName
                        nadya.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            nadya.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            nadya.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = nadya.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nadya.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    nadya.sendMessage(to, str(ret_))
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        nadya.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = nadya.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                    if msg._from in Owner:
                        settings["blacklist"] = {}
                        nadya.sendMessage(msg.to,"Blacklist Dibersihkan")
                        
                elif text.lower() == 'bancontact':
                    if msg._from in Owner:
                        settings["wblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                    if msg._from in Owner:
                        settings["dblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                    if msg._from in Owner:
                        if settings["blacklist"] == {}:
                            nadya.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            nadya.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="══════════List Blacklist═════════"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, nadya.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist :  %i" % len(settings["blacklist"])
                            nadya.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("kill "):
                    if msg._from in Owner:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(KAC).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(KAC).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'kickallmember':
                    if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            gs = nadya.getGroup(msg.to)
                            gs = ki.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
    #                       nadya.sendMessage(msg.to,"「 Bye All 」")
    #                       nadya.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                nadya.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ki,ki2,ki3,ki4]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    nadya.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'mention':
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        nadya.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        nadya.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        nadya.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        nadya.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        nadya.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            nadya.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"Lurking has not been set.")
                        
#==============================================================================#
 
#==============================================================================# 
#==============================================================================#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    nadya.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        nadya.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    nadya.sendMessage(to, str(ret_))                          
#===============================================================================[NEW]                         
            elif msg.text.lower().startswith("checkpraytime "):    
                sep = text.split(" ")
                location = text.replace(sep[0] + " ","")
                with requests.session() as web:
                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                    r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                        ret_ = "╔══[ Prayer Schedule ]"
                        ret_ += "\n╠ Lokasi : " + data[0]
                        ret_ += "\n╠ " + data[1]
                        ret_ += "\n╠ " + data[2]
                        ret_ += "\n╠ " + data[3]
                        ret_ += "\n╠ " + data[4]
                        ret_ += "\n╠ " + data[5]
                        ret_ += "\n╚══[ Complete ]"
                    else:
                        ret_ = "[ Prayer Schedule ] Error : Lokasi tidak ditemukan" 
                        nadya.sendMessage(to, str(ret_))
                        
            elif msg.text.lower().startswith("checkweather "):       
                sep = text.split(" ")
                location = text.replace(sep[0] + " ","")
                with requests.session() as web:
                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if "result" not in data:
                        ret_ = "╔══[ Weather Status ]"
                        ret_ += "\n╠ Lokasi : " + data[0].replace("Temperatur di kota ","")
                        ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","")
                        ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","")
                        ret_ += "\n╠ Tekanan Udara : " + data[3].replace("Tekanan udara : ","")
                        ret_ += "\n╠ Kecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                        ret_ += "\n╚══[ Complete ]"
                    else:
                        ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                        nadya.sendMessage(to, str(ret_))

            elif text.lower() == 'removeallchat':
                nadya.removeAllMessages(op.param2)
                nadya.sendMessage(to, "Berhasil hapus semua chat")

            elif text.lower() == 'time':
                nadya.sendMessage(to, "Goblok cek sendiri di tanggal jangan manja")

            elif msg.text.lower().startswith("gbroadcast "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                groups = nadya.groups
                for group in groups:
                    nadya.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                    nadya.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                    
            elif msg.text.lower().startswith("fbroadcast "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                friends = nadya.friends
                for friend in friends:
                    nadya.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    nadya.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
            elif msg.text.lower().startswith("allbroadcast "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                friends = nadya.friends
                groups = nadya.groups
                for group in groups:
                    nadya.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                    nadya.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                for friend in friends:
                    nadya.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    nadya.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))                             
                                    
#===============================================================================[nadyaMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT NADYA MESSAGE")
            try:
                if op.param3 in nadyaMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki2MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki3MID]

#-------------------------------------------------------------------------------[nadyaMID - ki4MID]
#===============================================================================[kiMID nadyaMID]
                if op.param3 in kiMID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
#===============================================================================[ki2MID nadyaMID]
                if op.param3 in ki2MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
#===============================================================================[ki3MID nadyaMID]

                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    nadya.sendMessage(op.param1,"Qr under protect")
            else:
                nadya.sendMessage(op.param1,"")
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            if op.param1 in read["readPoint"]:
                _name = nadya.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
        backupData()
    except Exception as error:
        logError(error)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = nadya.findGroupByTicket(ticket_id)
                        nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                        nadya.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name)) 
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if nadyaMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = nadya.getContact(sender)
                                    nadya.sendMessage(to, "sundala nu")
                                    sendMessageWithMention(to, contact.mid)
                                break
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        nadya.acceptGroupInvitation(op.param1)
        ki.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
    except Exception as e:
        nadya.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        nadya.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
