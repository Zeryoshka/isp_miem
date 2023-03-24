from typing import Set, List, Callable, Iterable, Dict

Way = List[int]

class WaysCalculator():
    def __init__(
        self,
        start: int, finish: int,
        visit_rule: Callable[[int], int],
        allowed_operations: Iterable[Callable[[int], int]],
        use_cache: bool = False,
    ):
        self._store: List[Way] = None
        self._cache: Dict[int, Way] = {}
        self._use_cache = use_cache
        self._start = start
        self._finish = finish
        self._visit_rule = visit_rule
        self._allowed_operations = allowed_operations
        self.call_count = 0

        if start <= finish:
            self._check_finish = lambda start, finish: start >= finish
        else:
            self._check_finish = lambda start, finish: start <= finish

    def calc(self) -> List[Way]:
        if self._store is not None:
            return self._store
        
        self._store = []
        self._calculate_ways(self._start, self._finish, [])
        return self._store

    def _calculate_ways(self, start: int, finish: int, way_prefix: Way):
        self.call_count += 1
        way_prefix = way_prefix.copy()
        way_prefix.append(start)
        if self._check_finish(start, finish):
            if start == finish and self._visit_rule(way_prefix):
                self._store.append(way_prefix)
            return

        new_points = {
            new_point
            for new_point in map(lambda operation: operation(start), self._allowed_operations)
            if new_point is not None
        }
        for new_start in new_points:
            if self._use_cache and new_start in self._cache:
                for way in self._cache[new_start]:
                    self._store.append(way_prefix + way)
            else:
                count_before = len(self._store)
                self._calculate_ways(new_start, finish, way_prefix)
                if self._use_cache:
                    self._cache[new_start] = [way[len(way_prefix):] for way in self._store[count_before:]]



    def print_ways(self):
        for i, way in enumerate(self._store):
            print(f'{i + 1}: {" -> ".join(map(str, way))}')


if __name__ == '__main__':
    
    visit_rule = lambda way: len(set(way) and {8, 16}) != 0
    operations = (
        lambda x: x + 1,
        lambda x: x * 2 + 1,
    )

    calculator = WaysCalculator(3, 25, visit_rule, operations, use_cache=True)
    calculator.calc()
    calculator.print_ways()
    print(calculator.call_count)
