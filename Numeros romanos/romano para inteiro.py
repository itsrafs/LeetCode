class Solution(object):
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            #converte os caracteres para o número correspondente
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        number = 0
        #no replace, o primeiro parametro substitui o segundo
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            #aqui, o num é o char atual da str, enquanto tiver algun char, ele converte para int
            number += roman_to_integer[char]
        return number

n = input('Write a roman number: ')
solution = Solution()
n = solution.romanToInt(n)
print(n)

