from stack import *
from prefix import *

class Postfix():
    
    def __init__(self,value):
        self.str = value
        self.arr = self.str.split(" ")

    def isPostfix(self):
        pSt = Stack(len(self.arr))

        for i in self.arr:
            if i == " ":
                pass
            elif isOperand(i):
                pSt.push(i)
            elif isFunction(i):
                pass
            elif isOperator(i):
                if pSt.pop() == False or pSt.getSize() == 0:
                    return False
            else: return False
        
        if pSt.getSize() != 1:
            return False

        return True

    def toPrefix(self):
        st = Stack(len(self.str))
        for i in self.arr:
            if(i == " "): pass

            elif isOperand(i):
                st.push(i)
                print(st)
            elif isFunction(i):
                op = st.top()
                st.pop()
                st.push(f"{i} {op}")
            else:
                op2 = st.top()
                st.pop()
                op1 = st.top()
                st.pop()
                st.push(f"{i} {op1} {op2}")
                print(st)
                
    def toInfix(self):
        st = Stack(len(self.str))
        for i in self.arr:
            if(i == " "): pass
            elif isOperand(i):
                st.push(i)
                print(st)
            elif isFunction(i):
                op = st.top()
                st.pop()
                st.push(f"({i} {op})")
                print(st)
            else:
                op2 = st.top()
                st.pop()
                op1 = st.top()
                st.pop()
                st.push(f"({op1} {i} {op2})")
                print(st)
