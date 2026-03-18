from python_library import array_input
from python_library import prime_num
def quicksort():
    nums = array_input() 

    def sort(arr):  
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sort(left) + middle + sort(right)

    return sort(nums)

def is_prime():
    n = int(input())
    return prime_num(n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm():
    a = int(input())
    b = int(input())
    c = gcd(a, b)
    return a * b // c

def dem_ki_tu(n):
    a = 0
    for i in n:
        a += 1
    return a

def dem_chu_so():
    n = int(input())
    return dem_ki_tu(str(n))

def dem_chu_so_chan():
    n = int(input())
    a = 0
    for i in str(n):
        if int(i) % 2 == 0:
            a += 1
    return a

def groupAnagrams():
    strs = input().split(",") 
    strs = [s.strip() for s in strs]  
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))  
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values()) 

print(groupAnagrams())
