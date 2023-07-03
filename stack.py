class Stack():
    
    def __init__(self, size):
        self.array = [None] * size
        self.size = 0
    
    def __str__(self):
        
        a = ""
        for i in self.array:
            if(i):
                a = f"{a} {i}"
        return str(a)
    
    def push(self, value):
        if (self.size < len(self.array)):
            self.array[self.size] = value
            self.size += 1
            return True
        return False

    def pop(self):
        if (not self.isEmpty()):
            self.size -= 1
            self.array[self.size] = None
            return True
        return False
    
    def top(self):
        if (not self.isEmpty()):
            return self.array[self.size - 1]
        return None

    def getSize(self):
        return self.size

    def isEmpty(self):
        return (self.size == 0)
