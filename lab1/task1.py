from typing import List

def is_all_zeros_with_odd_index(arr: List[int]):
    # return all([not (value == 0 and i % 2 == 0) for i, value in enumerate(arr)])
    for i, value in enumerate(arr):
        if i == 0 and i % 2 == 0:
            return False
    return True



if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print('arr:', arr)
    n, m = map(int, input().split())
    if is_all_zeros_with_odd_index(arr):
        print('Max of array:', max(arr))
    
    arr2 = [
        v / 2 if n <= i <= m else v
        for i, v in enumerate(arr)
    ]
    print('arr2:', arr2)