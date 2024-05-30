class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self ,data):
        p = self.head
        q = Node(data)
        while p == None:
            self.head = q
        else:
            while p.next != None:
                p = p.next
            p.next = q
            q.prev = p

    def show(self):
        p = self.head
        q = self.head
        while p != None:
            print(p.data, end=" <-> ")
            p = p.next
        print("None")
        while q.prev != None:
            print(q.data, end=" <-> ")
            q = q.prev
        print("None")
    
    def insert_end(self, data):
        p = self.head
        q = Node(data)

        while p.next != None:
            p = p.next
        p.next = q
        q.prev = p

    def insert_start(self,data):
        p = self.head
        q = Node(data)
        q.next = p
        p.prev = q
        self.head = q

    def insert_after_Node(self,data,sk):
        p = self.head
        q = Node(data)
        while p.next != None:
            if sk == p.data:
                q.next = p.next
                p.next.prev = q
                p.next = q
                q.prev = p
            elif sk != p.data:
                print("invalid data..")
            p = p.next


    def delete_start(self):
        p = self.head
        q = p.next
        p.next = None
        self.head = q
        q.prev = None
        print(p.data,"is removed....")
        del(p)

    def delete_end(self):
        p = self.head
        while p.next.next != None:
            p = p.next
        q = p.next
        p.next = None
        q.prev = None
        print(q.data,"node is removed....")
        del(q)

    def delete_mid(self, val):
        p =  self.head
        while p.next.data != val:
            p = p.next
        q = p.next
        p.next = q.next
        q.next.prev = p
        q.next = None
        q.prev = None
        print(q.data, "is deleted.....")    
        del(q)

l1 = DoublyLinkedList()
while True:
    print("\nChoose Any Options")
    print("1. Insert In The List")
    print("2. Show")
    print("3. Insert  At Head")
    print("4. Insert In The End")
    print("5. Insert After Particular Node")
    print("6. Delete  At The beginning")
    print("7. Delete In The End")
    print("8. Delete The Particular Node")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))





    if choice == 1:
        data = int(input("Enter your data: "))
        l1.insert(data)
        print(data,"is inserted \n")

    elif choice == 2:
        print("\n List:")
        l1.show()
        print("\n")

    elif choice == 3:
        data = int(input("Enter your data: "))
        l1.insert_start(data)
        print(data,"is inserted in Head\n")

    elif choice == 4:
        data = int(input("Enter your data: "))
        l1.insert_end(data)
        print(data,"is inserted in the end \n")      

    elif choice == 5:
        data = int(input("Enter your data: "))
        key = int(input("Enter your Node after which the data will be inserted: "))
        l1.insert_after_Node(data, key)
        print(data,"is inserted after", key)
        print("\n")  
    
    elif choice == 6:
        l1.delete_start()

    elif choice == 7:
        l1.delete_end()
    
    elif choice == 8:
        val = int(input("Enter the value: "))
        l1.delete_mid(val)

    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()    
