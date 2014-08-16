#!/usr/bin/env python
# use utf-8
import os, sys,time
from datetime import datetime
path = '/tmp/motion'
longest = 7
def GetAVIlist(path):
    resultlist = []
    for n in os.listdir(path):
        if os.path.isfile(path+'/'+n) == True and '.avi' in n:
            resultlist.append(n)
    return resultlist
def LastAVI(avilist):
    tag0 = 0
    avi0 = ''
    for n in avilist:
        tag = int(n.split('-')[1][:-4])
        if tag >tag0:
            tag0 = tag
            avi0 = n
        else:
            continue
    return avi0
def CheckDelta(avipath):
    datastr = avipath.split('-')[1]
    y,m,d = int(datastr[0:4]),int(datastr[4:6]),int(datastr[6:8])
    now = datetime.now()
    past = datetime(y,m,d,12,0,0,0)
    rawdelta = now - past
    delta = getattr(rawdelta,'days')
    if delta > longest:
        os.remove(path+'/'+avipath)
        return 1
    else:
        return 0
# def TarFLVjpg(flvname):
#     nametag = flvname.split('-')[0]
#     tgzname = flvname[:-3]+'tgz'
#     jpgall  = nametag+'-*-*.jpg'
#     os.system('tar zcvf %s/%s %s --remove-files' %(path,tgzname,jpgall))
#     return 1
# def DIRgoto(flvname):
#     date = flvname.split('-')[1][:8]
#     datedir = 'Archive_'+date
#     if os.path.isdir(datedir) == False:
#         os.mkdir(path+'/'+datedir)
#     os.system('mv %s/%s.* %s/%s' %(path,flvname[:-4],path,datedir))
#     return 1
# def GetDIRlist(path):
#     dirlist = []
#     for n in os.listdir(path):
#         if os.path.isdir(path+'/'+n) == True and 'Archive_' in n:
#             dirlist.append(n)
#     return dirlist
# def CalcDelta(arcdir):
#     y,h,m = arcdir[8:12],arcdir[12:14],arcdir[14:16]
#     now = datetime.now()
#     past = datetime(y,h,m,12,0,0,0)
#     rawdelta = now - past
#     delta = getattr(rawdelta,'days')
#     if delta > longest:
#         os.rmdir(path+'/'+arcdir)
#         return 1
#     else:
#         return 0
#def main():
#    flvlist = GetFLVlist(path)
#    if len(flvlist) == 0:
#        return 0
#    for flvpath in flvlist:
#        TarFLVjpg(flvpath)
#        DIRgoto(flvpath)
#    dirlist = GetDIRlist(path)
#    if len(dirlist) == 0:
#        return 0
#    for arcdir in dirlist:
#        CalcDelta(arcdir)
def main():
    avilist = GetAVIlist(path)
    if len(avilist) == 0:
        sys.exit()
    last = LastAVI(avilist)
    for avi in avilist:
        if avi == last:
            continue
        else:
            CheckDelta(avi)

if __name__ == '__main__':
    while 1:
        main()
        time.sleep(3600)
