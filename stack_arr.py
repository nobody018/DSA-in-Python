class ArrayStack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, element):
        self.data.append(element)
    
    def top(self):
        if self.is_empty():
            print("Stack is Empty")
        return self.data[-1]
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        return self.data.pop()
    
    def show(self):
        if self.is_empty():
            print("Stack is Empty")
        print(self.data)
    
stack_list = ArrayStack()
while True:
    print("\nChoose Any Options")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Display")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))

    if choice == 1:
        data = int(input("Enter your data: "))
        stack_list.push(data)
        print(data,"is inserted \n")

    elif choice == 2:
        stack_list.pop()
        print("\n")

    elif choice == 3:
        stack_list.show()
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()