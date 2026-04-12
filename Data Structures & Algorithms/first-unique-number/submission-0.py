class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = deque(nums)
        self._dict = defaultdict(int)
        for num in nums:
            self._dict[num] = self._dict.get(num, 0) + 1
        

    def showFirstUnique(self) -> int:
        while self._queue:
            if self._dict[self._queue[0]] == 1:
                return self._queue[0]
            else:
                self._queue.popleft()
        return -1
        

    def add(self, value: int) -> None:
        self._queue.append(value)
        self._dict[value] = self._dict.get(value ,0) + 1

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)