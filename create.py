import os
import fnmatch
import hashlib
from itertools import chain
from os import listdir
from os import path
import string
import re
import sys
from pathlib import Path
import unicodedata
import re

class Files:
    def getdir():
        dir = os.getcwd() + "\\music\\";
        return dir;
    def getsetdir():
        dir = os.getcwd()+"\\music\\";
        return dir;

               
    def getfiles():
        res = []
        for path in os.listdir(Files.getdir()):
            if os.path.isfile(os.path.join(Files.getdir(), path)):
                res.append(path)
        return fnmatch.filter(res,'*.mid')

    def getmd5fromfile(filename):
        md5_hash = hashlib.md5()
        md5file = "music//" + filename
        with open(md5file,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)
            return(md5_hash.hexdigest())
        
    def getsinglefile(index):
        files = Files.getfiles();
        return files[index];
    
    def getmd5byindex(index):
        return Files.getmd5fromfile(Files.getsinglefile(index));

    def getmd5():
        md5s = [];
        for entry in Files.getfiles():
            md5s.append(Files.getmd5fromfile(entry));
        return md5s;

    def getmusiclistids():
        list = ["theme" , "old_0" , "old_1" , "old_2" , "old_3" , "old_4" , "old_5"  , "old_6"  , "old_7" , "old_8" , "old_9" , "new_0" , "new_1" , "new_2" , "new_3" , "new_4" , "new_5"  , "new_6"  , "new_7" , "new_8" , "new_9" , "ezy_0" , "ezy_1" , "ezy_2" , "ezy_3" , "ezy_4" , "ezy_5"  , "ezy_6"  , "ezy_7" , "ezy_8" , "ezy_9" ];
        return list

    def stackdata():
        return list(zip(Files.getmusiclistids(),Files.getfiles(),Files.getmd5()));

    
    def getstackdata(index):
        array = [Files.stackdata()[index][0],Files.stackdata()[index][1],Files.stackdata()[index][2]];
        return array;

    def printmd5list():
        display = "\n[md5s]\n";
        for x in range(0, len(Files.stackdata())):
            array = Files.getstackdata(x);
            display += array[1]+" = " + array[2] + "\n";
        return display;

    def printmusicidlist():
        display = "\n[files]\n"
        for x in range(0, len(Files.stackdata())):
            array = Files.getstackdata(x);
            display += array[0]+" = " + array[1] + "\n";
        return display;

    def printmetadata():
        display = "[metadata]\nname = " + os.getlogin()+ "\nshortname = you\nversion = 1\ndescription = My list\n";
        return display;

    def printmusicnamelist():
        display = "\n[names]\n"
        for x in range(0, len(Files.stackdata())):
            array = Files.getstackdata(x);
            size = len(array[1]);
            name = array[1][:size - 4]
            display += array[1]+" = " + name + "\n";
        return display;

    def printorigintext():
        display = "\n[origin]\ndefault = The pc user " + os.getlogin() + " has decided that they wanted a custom music pack for OpenTTD so he decited to run DemonBigj781\' crappy codework...";
        return display;

    def joinalltexts():
        display = Files.printmetadata() + Files.printmusicidlist() + Files.printmd5list()+ Files.printmusicnamelist() + Files.printorigintext();
        return display;

    def createobmfile():
        file1 = open(Files.getdir()+'mymusic.obm', 'w');
        file1.write(Files.joinalltexts());
        file1.close()
        return

    def containsNumber(value):
        for character in value:
            if character.isdigit():
                return True
        return False
    
    def renamefiles():
        delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
        lv_path = os.getcwd()+ "\\submithere\\";
        paths = (os.path.join(root, filename)
            for root, _, filenames in os.walk(lv_path)
            for filename in filenames)
        print ("Search at " + lv_path)
        for count, path in enumerate(paths, start = 0):
            newname = path.replace('#', '')
            newname = newname.replace(lv_path, '')
            newname = newname.replace('%', '')
            newname = newname.replace('*', '')
            newname = newname.replace('<', '')
            newname = newname.replace('>', '')
            newname = newname.replace('*', '')
            newname = newname.replace('?', '')
            newname = newname.replace('\'', '')
            newname = newname.replace(' ', '')
            newname = newname.replace('-', '')
            newname = newname.replace('(', '')
            newname = newname.replace(')', '')
            for i in range(len(Files.getsetdir())):
                newname = newname.replace('Copy', '')
                newname = newname.replace(str(i), '')
            
            newname = newname[:-4] + str(count) +".mid";
            os.rename(path, os.getcwd()+"\\music\\"+ newname);

            
Files.renamefiles();

Files.createobmfile();


