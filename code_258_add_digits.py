class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while num >= 10:
            arr = [int(i) for i in str(num)]
            num = sum(arr)
        return num