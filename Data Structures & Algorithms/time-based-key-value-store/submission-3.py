class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # store： [[val,timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:


        res_space = self.store[key]
        if not res_space:
            return ""
        l = 0 
        r = len(res_space) - 1
        
        while l <= r:
            mid = l + (r-l)//2

            if res_space[mid][1] == timestamp:
                return res_space[mid][0]
            elif res_space[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
            if r <0:
                return ""
        return res_space[r][0]
        
        
