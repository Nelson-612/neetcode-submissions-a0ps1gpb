class MovingAverage:

    def __init__(self, size: int):
        self._queue = deque()
        self._sum = 0
        self._window = size

        

    def next(self, val: int) -> float:
        self._queue.append(val)
        self._sum += val

        if len(self._queue) > self._window:
            self._sum -= self._queue[0]
            self._queue.popleft()
        
        average = (self._sum / len(self._queue))
        return average

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
