class Solution(object):
    def isPalindrome(self, head):
        head_invertido = head[::-1]

        if head == head_invertido:
            print("Is palindrome")
        else:
            print("Is not palindrome")

numbers = input("Write a numeric sequence: ")
solution = Solution()
numbers = solution.isPalindrome(numbers)
print(numbers)

