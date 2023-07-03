from stack import *
from prefix import *
from postfix import *

class Infix():
    
    def __init__(self,value):
        self.str = value
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3 ,'?' : 80}
        self.arr = self.str.split(" ")
        self.negative()
        self.arr_rev = rev(self.arr)

    def negative(self):
        for i in range(len(self.arr)):
            if (self.arr[i] == "-" and (isOperand(self.arr[i+1]) or isFunction(self.arr[i+1]))):
                if (i == 0 or ((isOperator(self.arr[i-1]) or isFunction(self.arr[i-1])) and self.arr[i-1] != ')') ):
                    self.arr[i] = "?" 

    def notGreater(self, x, y):
        try:
            if isFunction(x):
                a = 82
            else:
                a = self.precedence[x]
            if isFunction(y):
                b = 82
            else: 
                b = self.precedence[y]
            return True if a  <= b else False
        except KeyError:
            return False

    def isLess(self, x, y):
        try:
            if isFunction(x):
                a = 82
            else:
                a = self.precedence[x]
            if isFunction(y):
                b = 82
            else: 
                b = self.precedence[y]
            return True if a < b else False
        except KeyError:
            return False

    def isSame(self, x, y):
        try:
            if isFunction(x):
                a = 82
            else:
                a = self.precedence[x]
            if isFunction(y):
                b = 82
            else: 
                b = self.precedence[y]
            return True if a == b else False
        except KeyError:
            return False

    def isInfix(self):
        isOperandRepeat = False
        isOperatorRepeat = False
        pSt = Stack(len(self.arr))

        for i in self.arr:
            if i == "(":
                pSt.push(i)
            elif i == ")":
                if not pSt.pop():
                    return False
            else: pass
        if not pSt.isEmpty():
            return False
        
        for i in self.arr:
            if isFunction(i):
                pass
            elif isOperand(i):
                isOperatorRepeat = False
                if isOperandRepeat:
                    return False
                else:
                    isOperandRepeat = True
            elif i == "(" or i ==")" or i =='?':
                pass
            elif isOperator(i):
                isOperandRepeat = False
                if isOperatorRepeat:
                    return False
                else: isOperatorRepeat = True
            else: return False
        return True

    def toPostfix(self):
        st = Stack(len(self.str))
        output = Stack(len(self.str))
        for i in self.arr:
            if (isOperand(i)):
                output.push(i)
                print("Output:" + str(output))

            elif (i == '('):
                st.push(i)
                print("Stack:" + str(st))

            elif (i == ')'):
                while (st.top() != '(' and not st.isEmpty()):
                    output.push(st.top())
                    st.pop()
                    print("Output:" + str(output))
                    print("Stack:" + str(st))
                st.pop()

            else:
                while (not st.isEmpty() and self.notGreater(i,st.top())):
                    output.push(st.top())
                    st.pop()
                    print("Output:" + str(output))
                    print("Stack:" + str(st))
                st.push(i)
                print("Stack:" + str(st))

        while (not st.isEmpty()):
            output.push(st.top())
            st.pop()
            print("Output:" + str(output))
            print("Stack:" + str(st))
        
        return str(output)

    def toPrefix(self):
        st = Stack(len(self.str))
        output = Stack(len(self.str))
        for i in self.arr_rev:
            if(isOperand(i)):
                output.push(i)
                print("Output:" + str(output))

            elif(i == ')'):
                st.push(i)

            elif(i == '('):
                while (st.top() != ')' and not st.isEmpty()):
                    output.push(st.top())
                    st.pop()
                    print("Output:" + str(output))
                    print("Stack:" + str(st))
                st.pop()
            
            else:
                while (not st.isEmpty() and (self.isLess(i,st.top()) or (self.isSame(i,st.top()) and i == '^') )):
                    output.push(st.top())
                    st.pop()
                    print("Output:" + str(output))
                    print("Stack:" + str(st))
                st.push(i)
                print("Stack:" + str(st))

        while (not st.isEmpty()):
            output.push(st.top())
            st.pop()
            print("Output:" + str(output))
            print("Stack:" + str(st))

        output.array = rev((output.array))
        print("Output:" + str(output))
        print("Stack:" + str(st))

a = Prefix("+ - * 7 21 / 6 8 92")
#a = Infix("7 * 21 - 6 / 8 + 92") 
#a.toPostfix()

#1  in to post  "3 + (8 ^ 2) / 12 * 9"
#2  post to pre "9 ? 7 ^ 6 * 3 2 - 9 ^ + 72 sin /"
#3  pre to in   "- 2 - * 5 / 12 + 6 8 ^ 2 3"
#4  post to pre "7 21 * 6 8 / - 92 +"
