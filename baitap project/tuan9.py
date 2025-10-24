from python_library import array_input
def hello_1():
    print('hello')

def hello_n():
    n = int(input())
    for i in range(n):
        print("hello")

def hello_nn():
    n = int(input())
    for i in range(n):
        for j in range(n):
            print('hello')

def binary_search():
    target = int(input("target: "))
    arr = sorted(array_input()) 

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print("found", target, "at", mid)
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("not found", target)
    return False


binary_search()