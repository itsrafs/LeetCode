class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        num = 1
        if 1 <= n <= 10**4:
            while int(num) <= n:
                if num % 3 == 0 and num % 5 == 0:
                    result.append("FizzBuzz")
                elif num % 3 == 0:
                    result.append("Fizz")
                elif num % 5 == 0:
                    result.append("Buzz")
                else:
                    result.append(str(num))
                num += 1
            return result

number = int(input('Write a number: '))
solution = Solution()
result = solution.fizzBuzz(number)
print(result)