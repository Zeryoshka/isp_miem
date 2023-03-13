

arr = list(map(int, input().split()))
min1 = min(arr)
arr.remove(min1)
min2 = min(arr)

print('min sum:', min1, '+', min2)