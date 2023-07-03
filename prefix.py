from stack import *

def isOperator(ch):
    return ch in ['+', '-', '*', '/', '^', '(', ')']

def isFunction(ch):
    return ch in ['cos', 'sin', 'tan', 'cot', 'sec', 'csc', 'ln', 'log']

def isOperand(ch):
    if isFunction(ch) :
        return False
    try:
        float(ch)
        return True
    except:
        return ch.isalpha() or ch.isdigit()

def rev(x):
    return x[::-1]

class Prefix():
    
    def __init__(self,value):
        self.str = value.strip()
        self.arr = self.str.split(" ")
        self.arr = rev(self.arr)

    def isPrefix(self):
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

    def toPostfix(self):
        st = Stack(len(self.str))
        for i in self.arr:
            if(i == " "): pass
            elif(isOperand(i)):
                st.push(i)
                print(st)
            elif(isFunction(i)):
                op = st.top()
                st.pop()
                st.push(f"{op} {i}")
                print(st)        
            else:
                op1 = st.top()
                st.pop()
                op2 = st.top()
                st.pop()
                st.push(f"{op1} {op2} {i}")
                print(st)
        print(st)

    def toInfix(self):
        st = Stack(len(self.str))
        for i in self.arr:
            if( i == " "): pass
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
                st.push(f"({op2} {i} {op1})")
                print(st)
        print(st)
