class arraylist:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.arr = [None] * maxSize
    
    def insert(self, index, data):
        if index < 0 or index >= self.maxSize:
            print("Out of bound")
        self.arr[index] = data
        self.size += 1
    
    def display(self):
        print("Array: ")
        print(self.arr[:self.size])
        
def bubble_sort(arr):
    n = arr.size
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Sorted array:")
    print(arr)
            
    



arr = arraylist(10)
arr.insert(0,12)
arr.insert(1,54)
arr.insert(2,35)
arr.insert(3,75)
arr.insert(4,80)
arr.insert(5,92)
arr.display()   

print()
bubble_sort(arr)     