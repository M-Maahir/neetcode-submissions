class TimeMap:

    def __init__(self):
        self.hsmp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hsmp:
            self.hsmp[key] = []
        self.hsmp[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        current = self.hsmp.get(key, [])

        l = 0
        r = len(current)-1

        while l <= r:
            m = (l + r)//2

            if timestamp >= current[m][1]:
                res = current[m][0]
                l = m + 1
            else: r = m - 1

        return res
        
