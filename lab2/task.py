from collections import defaultdict

def regions_iter(n: int):
    for _ in range(n):
        _, _, region = tuple(input().split())
        yield region


def main():
    n = int(input())

    store: defaultdict[str, int] = defaultdict(int)
    for region in regions_iter(n):
        store[region] += 1

    min_value = min(store.values())
    records_to_out = filter(lambda region: store[region] == min_value, store.keys())
    print('regions: ', ' '.join(records_to_out))


if __name__ == '__main__':
    main()