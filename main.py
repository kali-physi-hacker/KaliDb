# ----------------- Copyright Ⓒ Kali Association of Programmers -------------- 
#       Name of Author                      :   Kali Junior Brown (Dr. Kali)
#       Profession at the time of writing   :   (Junior High School Student)
#       Age At The Time Of Writing          :   16 years
#       License                             :   KAS - Kali Association of Scientist
#       Company                             :   Kali Association of Science And Technology (KAST)

#       This Program Is To Demonstrate The Basic Concept Of Databases In Computer Science And How Python
#       Can Be Used To Manipulate And Simulate The Various Concepts.
#       Using The Power of Python, How Various Art Diagrams Could Be Made To Simulate Table Arts
#       And How Locked Hidden Files And Folders Could Simulate Databases, Rows And Columns In Python
#       Also How To Use Encryption In Python To Encrypt Sensitive Part of The File Contents For Storage
#                                               Security

#       Copyright Information
#       You Are Free To Use This Program For Whatever Purpose You Want To Use It For And
#       Distribute or Modify It To Suit Your Needs. But You Don't Have Neccessary Permissions 
#       And Rights To Change To Ownership Of This Program. The Program Was Solely Written By Kali Junior 
#       Brown And Remains The Sole Proprietor Of The Program
#       You Can Contribute The Project Via Github: https://kali-physi-hacker/KaliDb.git By Sending A 
#       Commit Request For Approval



import sys, os, glob, subprocess
from kaliUtils import KaliUtils

class KaliDb(KaliUtils):
    def __init(self, user=None, pword=None):
        self.user = user 
        self.pword = pword 
        self.run()

    def run(self):
        name = input("kaliDb>\nUser: ")
        pword = input("Password: ")
        if name == "ADMIN" and pword == "HACKER":
            self.start()
        else:
            print ("*-------------- Invalid Username or Password ---------------*")
            self.run()

    def start(self):
        print ("*--------------- Login Successful ----------------*")
        print ("Kali Db Started\n")
        self.root()
    
    def root(self):
        cmd = input("KaliDb> ")
        while (cmd != "quit"):
            try:
                if " " in cmd:
                    args = self.analyseStr(cmd)
                    exec("self."+args[0]+"(%s)"%args)
                   # delete
                    self.root()
                else:
                    exec("self."+cmd+"()")
                    cmd = input("KaliDb> ")
            except NameError:
                print ('Kali Bash Error: "%s" Command Not Found'%(cmd))
                cmd = input("KaliDb> ")
    

    def showdb(self):
        tree = glob.glob("*")
        dbs = []
        for i in tree:
            if os.path.isdir(i):
                dbs.append(i)
        self.HeadT(dbs)
        self.alignT(dbs)


    def cls(self):
        platform = os.platform 
        cmd = ""
        if platform == "win32":
            cmd += "cls"
        else:
            cmd += "clear"
        subprocess.call(cmd, shell=True)


    def createdb(self, arr):
        arr.remove(arr[0])
        for i in arr:
            if os.path.isdir(i):
                print ("*--------- Database Already Exists With The Name %s ----------*" %s)
            else:
                os.mkdir(i)
                print ("*----------------- Database %s Created Successfully -------------------*" %i)

    def deletedb(self, arr):
        arr.remove(arr[0])
        for i in arr:
            if os.path.isdir(i):
                print ("*------------- Database %s Does Not Exist ------------*" %i)
            else:
                os.rmdir(i)
                print ("*----------------- Database %s Deleted Successfully -------------------*" %i)

if __name__ == "__main__":
    KaliDb().run()
##des = KaliDb()
##des.showdb()