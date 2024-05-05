class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None
    
class PolynomialLinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self, coef, exp):
        p = self.head
        q = Node(coef, exp)
        
        if p == None:
            self.head = q
        else:
            while p.next != None:
                p = p.next
            p.next = q
    
    def show(self):
        p = self.head
        while p != None:
            print(f"{p.coef}X^{p.exp}", end=" ")
            if p.next != None:
                print("+", end=" ")
            p = p.next
        print()

def derivation(l1):
    result = PolynomialLinkedList()
    p = l1.head
    while p != None:
        new_coef = p.exp * p.coef
        new_exp = p.exp - 1
        result.insert(new_coef, new_exp)
        p = p.next
    print("\n Derivation of the Polynomial....")
    result.show()
    print()

poly1 = PolynomialLinkedList()
poly1.insert(3,2)
poly1.insert(4,3)


print("\n Polynomial: ")
poly1.show()

derivation(poly1)

