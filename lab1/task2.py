from typing import List
from math import fabs

def get_index_first_negative(arr: List[int]) -> List[int]:
    for i, n in enumerate(arr):
        if n < 0:
            return i
    return -1


def modi(arr: List[int]) -> List[int]:
    delta = 0
    for i, n in enumerate(arr):
        if n == 0:
            delta += 1
        else:
            arr[i - delta] = n
    for i in range(delta):
        arr[len(arr) - 1 - i] = 0
    return arr


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    k = int(input())
    print('arr:', arr)
    first_negative_index = get_index_first_negative(arr)
    if first_negative_index != -1:
        last_negative_index = len(arr) - 1 - get_index_first_negative(arr[::-1])
        print('sum from first to last negative:', sum(arr[first_negative_index:last_negative_index]))
    else:
        print('No negative')

    mid_index = len(arr) // 2
    arr = sorted(arr[:mid_index]) + arr[mid_index:]
    print('sorted arr: ', arr)
    print('modi arr: ', modi(arr))

    last_version = list(filter(lambda x: fabs(x) >= k, arr))
    print('without removed:', last_version)
    
