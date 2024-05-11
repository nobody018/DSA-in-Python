def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    print("Sorted array:")
    print(arr)

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


       

    

    
    
    
    
arr= [34,2,55,3,1,23,45,33]

print(arr)
print()
print("Bubble Sort........")
bubble_sort(arr)
print()
print("Selection Sort........")
selection_sort(arr)