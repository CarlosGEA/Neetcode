"""
Difficulty : Medium
Date created : 24-10-2024
"""

class TimeMap:

    def __init__(self):
        self.data = {}

        return None
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

        return None
         
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.data:
            return res
        
        kdata = self.data[key]
        l = 0
        r = len(kdata) - 1
        while l <= r:
            m = (l + r) // 2
            if kdata[m][0] <= timestamp:
                res = kdata[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
    

def main():

    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    print(timeMap.get("alice", 1))  # "happy"
    print(timeMap.get("alice", 2))  # "happy"
    timeMap.set("alice", "sad", 3)
    print(timeMap.get("alice", 3))  # "sad"
   
    return None


if __name__ == "__main__":
    main()