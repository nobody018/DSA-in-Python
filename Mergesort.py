class ArrayList:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def display(self):
        print("Array:", self.array)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



arr = ArrayList()

while True:
    print("\nChoose Any Options")
    print("1. Insert Array")
    print("2. Display Array")
    print("3. Quick Sort")
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
        quick_sort(arr.array)
        print("Sorted array:")
        arr.display()
    
    elif choice == 0:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()

