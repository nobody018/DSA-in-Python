class ArrayList:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def display(self):
        print("Array:", self.array)


def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)

def quick_sort_recursive(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



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

