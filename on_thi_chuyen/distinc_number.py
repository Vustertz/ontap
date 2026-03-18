import sys

input = sys.stdin.readline

n = int(input())
arr = []

while len(arr) < n:
    arr += list(map(int, input().split()))

print(len(set(arr)))