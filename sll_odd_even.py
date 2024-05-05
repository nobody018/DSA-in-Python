class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        p = self.head
        q = Node(data)
        
        if p == None:
            self.head = q
        else:
            while p.next != None:
                p = p.next
            p.next = q
    
    def show(self):
        p = self.head
        while p != None:
            print(p.data, end="->")
            p = p.next
        print("None")

def splitList(l1):
    l2 = LinkedList() #even list
    l3 = LinkedList() #odd list
    p = l1.head
    while p != None:
        if p.data % 2 == 0:
            l2.insert(p.data)
        else:
            l3.insert(p.data)
        p_next = p.next
        p.next = None
        p = p_next

    l1.head = None
    return l2, l3


list1 = LinkedList()

list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)

print()
print("Original list:")
list1.show()

even_list, odd_list = splitList(list1)

print()
print("Even numbers list:")
even_list.show()

print()
print("Odd numbers list:")
odd_list.show()

print()
print("Original list after splitting and deleting:")
list1.show()