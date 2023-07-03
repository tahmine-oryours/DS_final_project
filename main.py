from stack import *
from postfix import *
from prefix import *
from infix import *

def dicsort(dic):
    sortedDic = {}
    keylist = list(dic)
    while(len(keylist)):
        max = -1
        key = ""
        for i in keylist:
            if (dic[i] > max):
                max = dic[i]
                key = i
        dic[key] =  -5
        sortedDic[key] = max
        keylist.remove(key)
    return sortedDic

history = {}

if __name__ == "__main__":
    while(True):
        print("1:infix to postfix")
        print("2:infix to prefix")
        print("3:prefix to postfix")
        print("4:prefix to infixfix")
        print("5:postfix to prefix")
        print("6:postfix to infix")
        print("7:history")
        print("0:quit")
        a = input()

        if a == "1":
            print("please enter a valid string")
            value = input()
            infix = Infix(value)
            infix.toPostfix()
            input("press enter to continiue")
            try:
                history["infix to postfix"] = history["infix to postfix"] + 1
            except:
                history["infix to postfix"] = 1
        elif a == "2":
            print("please enter a valid string")
            value = input()
            infix = Infix(value)
            infix.toPrefix()
            input("press enter to continiue")
            try:
                history["infix to prefix"] = history["infix to prefix"] + 1
            except:
                history["infix to prefix"] = 1    
        elif a == "3":
            print("please enter a valid string")
            value = input()
            prefix = Prefix(value)
            prefix.toPostfix()
            input("press enter to continiue")
            try:
                history["prefix to postfix"] = history["prefix to postfix"] + 1
            except:
                history["prefix to postfix"] = 1        
        elif a == "4":
            print("please enter a valid string")
            value = input()
            prefix = Prefix(value)
            prefix.toInfix()
            input("press enter to continiue")
            try:
                history["prefix to infix"] = history["prefix to infix"] + 1
            except:
                history["prefix to infix"] = 1    
        elif a == "5":
            print("please enter a valid string")
            value = input()
            postfix = Postfix(value)
            postfix.toPrefix()
            input("press enter to continiue")
            try:
                history["postfix to prefix"] = history["postfix to prefix"] + 1
            except:
                history["postfix to prefix"] = 1  
        elif a == "6":
            print("please enter a valid string")
            value = input()
            postfix = Postfix(value)
            postfix.toInfix()
            input("press enter to continiue")
            try:
                history["prefix to intfix"] = history["prefix to intfix"] + 1
            except:
                history["prefix to intfix"] = 1    
        elif a == "7":
            history = dicsort(history)
            print(history)
        elif a == "0":
            break
