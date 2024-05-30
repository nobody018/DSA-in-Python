class ArrayList:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def display(self):
        print("Array:", self.array)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    for i in range(0,len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small = j
                
        arr[i], arr[small] = arr[small], arr[i]
        
    print("Sorted array:")
    print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = ArrayList()

while True:
    print("\nChoose Any Options")
    print("1. Insert Array")
    print("2. Display Array")
    print("3. Bubble Sort")
    print("4. Selection Sort")
    print("5. Insertion Sort")
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
        print("Bubble Sort")
        bubble_sort(arr.array)
        print("Sorted array:")
        arr.display()
    
    elif choice == 4:
        print("Selection Sort")
        selection_sort(arr.array)
        print("Sorted array:")
        arr.display()
    
    elif choice == 5:
        print("Insertion Sort")
        insertion_sort(arr.array)
        print("Sorted array:")
        arr.display()
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()

