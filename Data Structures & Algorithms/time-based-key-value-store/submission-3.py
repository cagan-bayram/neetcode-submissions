from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        # bisect_right to find insertion index
        i = bisect.bisect_right(pairs, (timestamp, chr(127)))
        if i == 0:
            return ""
        return pairs[i-1][1]
