class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.top = None
     

    def push(self,data):
        p = self.top
        q = Node(data)
        q.next = p
        self.top = q

    def pop(self):
        p = self.top
        q = p.next
        p.next = None
        self.top = q
        print(p.data,"is removed....")
        del(p)

        
    def show(self):
        p = self.top
        while p != None:
            print(p.data, end="->")
            p = p.next
        print("None")

l1 = LinkedList()
while True:
    print("\nChoose Any Options")
    print("1. Push")
    print("2. Pop")
    print("3. Show")
    print("4. Exit")
    choice =int(input("Enter your Choice........... \n"))

    if choice == 1:
        data = int(input("Enter your data: "))
        l1.push(data)
        print(data,"is inserted \n")

    elif choice == 3:
        print("\n List:")
        l1.show()
        print("\n")

    elif choice == 2:
        l1.pop()

    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()