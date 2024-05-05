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

while True:
    print("\nChoose Any Options")
    print("1. Create Polynomial (Single variable)")
    print("2. Display Polynomial")
    print("3. Derivative of the Polynomial")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))





    if choice == 1:
        coef = int(input("Enter the Coefficient: "))
        exp = int(input("Enter the Exponent: "))
        poly1.insert(coef, exp)
        print("data is inserted \n")

    elif choice == 2:
        print("\n List:")
        poly1.show()
        print("\n")

    elif choice == 3:
        derivation(poly1)
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()







