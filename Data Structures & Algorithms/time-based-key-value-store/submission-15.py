class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # smaller or equal to the value
        if key not in self.store:
            return ""
        answerspace = self.store[key] # ('happy',1), ('sad', 3)
        if not answerspace:
            return ""
         # no timestamp <= target
        if answerspace[0][1] > timestamp:
            return ""
     
        l = 0 
        r = len(answerspace) - 1
        
        while l < r:

            # m = (l + r) // 2
            m = math.ceil( (l + r) / 2)
            # m = (l + r + 1)//2

            if answerspace[m][1] == timestamp:
                return answerspace[m][0]

            elif answerspace[m][1] > timestamp: # cant be the answer, need to search left side
                r = m - 1
            else:
                l = m 

        return answerspace[l][0]


