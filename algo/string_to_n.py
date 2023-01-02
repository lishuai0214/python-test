class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return ""

        l = numRows + numRows - 2
        list = []
        temp = ''
        for i in range(len(s)):
            if i == 0 or i%(l) != 0:
                temp = temp + s[i]
            elif i%(l) == 0:
                list.append(temp)
                temp = s[i]
                
        if temp != '':
            list.append(temp)

        print(list)

        res = ''

        for k in range(numRows):
            for str in list:
                if k < len(str):
                    if k < numRows:
                        res = res + str[k]
                    print(l - k)
                    if l - k < len(str) and l - k >= numRows:
                        res = res + str[l - k]
        print(res)
        return res


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 4
    solution = Solution()
    solution.convert(s, numRows)