class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)
        streamSorted = sorted(self.stream, reverse=True)
        return streamSorted[self.k-1]
