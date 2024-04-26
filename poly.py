class Node:
    def __init__(self, coff, exp):
        self.coff = coff
        self.exp = exp
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self, coff, exp):
        p = self.head
        q = Node(coff, exp)
        if p == None:
            self.head = q
        else:
            while p.next != None:
                p = p.next
            p.next = q
            
    def show(self):
        p = self.head
        l = 1
        while p != None:
            if p.coff>=0:
                if l== 1:
                    print(p.coff,"X^",p.exp, end="")
                else:
                    print("+",p.coff,"X^",p.exp, end="")
            elif p.coff < 0 :
                print(p.coff,"X^",p.exp,end="")
            p = p.next
            l += 1

def derivation(l1):
    d1 = Linkedlist()
    
    p = l1.head
    while p != None:
        exp1= p.exp - 1
        coff1 = p.exp * p.coff
        d1.insert(coff1, exp1)
        p = p.next
    print("\n Derivation of the polynimila")
    d1.show()



        
    
poly1 = Linkedlist()
poly1.insert(4,3)
poly1.insert(-5,3)
poly1.insert(4,1)
poly1.show()
derivation(poly1)
