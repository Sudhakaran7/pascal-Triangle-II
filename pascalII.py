class Solution2(object):
    def getRow(self, rowIndex):
        result = [1]
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in range(1, i)] + [1]
        return result

val=Solution2()
n=int(input())
print(*val.getRow(n))
