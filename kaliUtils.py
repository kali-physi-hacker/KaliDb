# ----------------- Copyright Ⓒ Kali Association of Programmers -------------- 
#       Name of Author                      :   Kali Junior Brown (Dr. Kali)
#       Profession at the time of writing   :   (Junior High School Student)
#       Age At The Time Of Writing          :   16 years
#       License                             :   KAS - Kali Association of Scientist
#       Company                             :   Kali Association of Science And Technology (KAST)

#       This Program Is Just A Utility For KaliDb Program Written In Python To Demonstrate How Mathematics
#       And Python Could Be Used To Manipulate Visualization And Create Database Tables Rows And Columns


class KaliUtils():
    def maxLength(self, arr):
        maxLength = 0 
        for i in arr:
            if len(i) > maxLength:
                maxLength = len(i)
        return maxLength

    def HeadT(self, arr):
        max = int(self.maxLength(arr)+2)
        if max > 2:
            print ("+"+"-"*(max)+"+")
            print ("|"+" "*(int((max-9)/2)) + "Databases" + " "*(int((max-9)/2)) + "|")
            print ("+"+"-"*(max)+"+")
        else:
            print ("+"+"-"*(13)+"+")
            print ("|"+ " "*2 +"Databases"+ " "*2 +"|")
            print ("+"+"-"*(13)+"+")

    def alignT(self, arr):
        max = int(self.maxLength(arr)+1)
        if max > 1:
            for i in arr:
                print ("| " + i + " "*((max-len(i))) + "|")
            print ("+"+"-"*(max+1)+"+")
        else:
            print ("| "+" "*11 + " |")
            print ("| "+"No Database" + " |")
            print ("| "+" "*11 + " |")
            print ("+"+"-"*(13)+"+")\

    def analyseStr(self, word):
        spaceL = [-1]
        argL = []
        for i in range(len(word)):
            if word[i] == " ":
                spaceL.append(i)
        spaceL.append(len(word))
        #print(spaceL)
        for i in range(len(spaceL)-1):
            argL.append(word[(spaceL[i])+1:spaceL[i+1]])
        return argL


if __name__ == "__main__":
    arr = ("Kali", "NetworkingProgramming", "JuniorWorkings", "Brown", "Hacker", "Programmer")
    kali = KaliUtils()
    print(kali.maxLength(arr))
    kali.HeadT(arr)
    kali.alignT(arr)
    name = "My name is Desmond"
    me = kali.analyseStr(name)
    print(me)