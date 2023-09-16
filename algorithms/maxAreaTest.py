class Solution:
    def maxArea(self, height) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

if __name__ == '__main__':
    list = [1, 4, 5, 3, 2, 1, 7, 3, 5]
    solution = Solution()
    res = solution.maxArea(list)
    print(res)