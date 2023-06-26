from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            counterM = Counter(magazine)
            counterR = Counter(ransomNote)

            if char in magazine and counterR[char] <= counterM[char]:
                print("True")
                return True
            else:
                print("False")
                return False

magazine = input("Write magazine: ")
ransom = input("Write the Ransom note: ")
solution = Solution()
s = solution.canConstruct(ransom, magazine)