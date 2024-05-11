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

def frequencyOfNodes(l1):
    p = l1.head
    freq = {}
    
    while p != None:
        if p.data in freq:
            freq[p.data] += 1
        else:
            freq[p.data] = 1
        p = p.next

    print("Frequency of each nodes: ")
    print(freq)


list1 = LinkedList()

list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(1)
list1.insert(5)
list1.insert(2)
list1.insert(3)
list1.insert(2)
list1.insert(3)

print()
print("Original list:")
list1.show()

frequencyOfNodes(list1)