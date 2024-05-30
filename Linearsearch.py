class ArrayList:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def display(self):
        print("Array:", self.array)


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1



arr = ArrayList()

while True:
    print("\nChoose Any Options")
    print("1. Insert Array")
    print("2. Display Array")
    print("3. Linear Search")
    print("4. Binary Search")
    print("0. Exit")
    choice =int(input("Enter your Choice........... \n"))
    if choice == 1:
        data = int(input("Enter the element: "))
        arr.insert(data)
        print("data is inserted \n")

    elif choice == 2:
        print("\n List of 1st polynomial:")
        arr.display()
        print("\n")
    
    elif choice == 3:
        target = int(input("Enter the target: "))
        result = linear_search(arr.array, target)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found")
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()

