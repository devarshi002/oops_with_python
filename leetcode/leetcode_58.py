class Solution:
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        return len(words[-1])
    
solution = Solution()

print(solution.lengthOfLastWord("Hello WOrld"))