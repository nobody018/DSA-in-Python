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

def additionPolynomial(l1,l2):
    l3 = PolynomialLinkedList()
    p1 = l1.head
    p2 = l2.head

    while p1 != None and p2 != None:
        if p1.exp == p2.exp:
         sum_poly = p1.coef + p2.coef
         l3.insert(sum_poly, p1.exp)
         p1 = p1.next
         p2 = p2.next
        elif p1.exp > p2.exp:
            l3.insert(p1.coef, p1.exp)
            p1 = p1.next
        else:
            l3.insert(p2.coef, p2.exp)
            p2 = p2.next
    if p1 == None:
        while p2 != None:
            l3.insert(p2.coef, p2.exp)
            p2 = p2.next    
    if p2 == None:
        while p1 != None:
            l3.insert(p1.coef, p1.exp)
            p1 = p1.next  

    print("Addition of two polynomial is : ")
    l3.show()

poly1 = PolynomialLinkedList()
poly2 = PolynomialLinkedList()

while True:
    print("\nChoose Any Options")
    print("1. Create Polynomial 1")
    print("2. Display Polynomial 1")
    print("3. Create Polynomial 2")
    print("4. Display Polynomial 2")
    print("5. Addition of the two Polynomial(1+2)")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))





    if choice == 1:
        coef1 = int(input("Enter the Coefficient for 1st polynomial: "))
        exp1 = int(input("Enter the Exponent for 1st polynomial: "))
        poly1.insert(coef1, exp1)
        print("data is inserted \n")

    elif choice == 2:
        print("\n List of 1st polynomial:")
        poly1.show()
        print("\n")
    
    elif choice == 3:
        coef2 = int(input("Enter the Coefficient for 2nd polynomial: "))
        exp2 = int(input("Enter the Exponent for 2nd polynomial: "))
        poly2.insert(coef2, exp2)
        print("data is inserted \n")
    
    elif choice == 4:
        print("\n List of 2nd polynomial:")
        poly2.show()
        print("\n")

    elif choice == 5:
        additionPolynomial(poly1, poly2)
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()