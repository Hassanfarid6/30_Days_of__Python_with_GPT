# after learning fundamentals trying writing factorial and fibanoci by yourself

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))



def binary_search(arr,target,start,end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
        
arr = [1,2,3,4,5,6,7,8,9,10]
target = 1
start = 0
end = len(arr) - 1
print(binary_search(arr,target,start,end))