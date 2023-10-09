"""Median calculator."""
def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0,n-i-1):
            if (arr[j] > arr [j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

            
def find_median(arr):
    n = len(arr)
    if n%2 ==0:
        return ((arr[n//2]) + (arr[n//2 -1])) /2
    else:
        return arr[n//2]




"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(f"Input: {numbers}")
bubble_sort(numbers)
print(f"Expected output: {find_median(numbers)}" )




