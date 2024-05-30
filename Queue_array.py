class ArrayQueue:
    def __init__(self,max_size):
        self.max_size : max_size
        self.data = [None] * max_size
        self.rear = -1
        self.front = -1
    
    def __len__(self):
        return self.rear + 1 

    def is_empty(self):
        return self.rear == -1
    
    def is_full(self):
        return self.rear == self.max_size
    
    def enqueue(self, element):
        if self.is_full():
            print("Queue is Full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = self.rear + 1
        self.data[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        temp = self.data[self.front]
        self.data[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = self.front + 1
        print(temp, " is removed..")
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.data[i], end=" ")
            print()


Queue_list = ArrayQueue(12)
while True:
    print("\nChoose Any Options")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Display")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))

    if choice == 1:
        data = int(input("Enter your data: "))
        Queue_list.enqueue(data)
        print(data,"is inserted \n")

    elif choice == 2:
        Queue_list.dequeue()
        print("\n")

    elif choice == 3:
        Queue_list.display()
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()
