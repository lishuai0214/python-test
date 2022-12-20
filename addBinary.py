class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        flag = 0
        while a != "" and b != "":
            int_a = int(a[-1])
            int_b = int(b[-1])
            r = (int_a + int_b + flag) % 2
            flag = (int_a + int_b + flag)//2
            res = str(r) + res
            a = a[0:-1]
            b = b[0:-1]

        while a != "":
            int_a = int(a[-1])
            r = (int_a + flag) % 2
            flag = (int_a + flag)//2
            res = str(r) + res
            a = a[0:-1]

        while b != "":
            int_b = int(b[-1])
            r = (int_b + flag) % 2
            flag = (int_b + flag)//2
            res = str(r) + res
            b = b[0:-1]
        if flag == 1:
            res = "1" + res

        return res

if __name__ == '__main__':
    a = "111111"
    b = "1"
    s = Solution()
    res = s.addBinary(a, b)
    str = "abcde"
    print(res)
