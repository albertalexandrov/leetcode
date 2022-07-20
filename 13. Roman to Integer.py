"""
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


class Solution1:
    """МОЕ РЕШЕНИЕ (сложное)

    Добавляем особые случаи типа IX, IV и тд в маппинг и проходим окном размером два по s
    Однако, сделать можно было проще (см. Solution2)

    Notes:
        Можно было бы прийти к более простому и более легкому в восприятии Solution2, если бы я больше
        внимания обратил на особенности данных, а именно на особые случаи типа IV, IX, то есть когда
        меньшее число стоит перед бОльшим.  Тогда бы удалось увидеть, что число XIX можно привести
        к сумме вида 10 + (-1) + 10, то есть меньшее число прибавляется со знаком минус, и не пришлось
        бы сотворять окна, дописывать особые случаи в mapping

    """
    def romanToInt(self, s):
        mapping = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        idx = 0
        converted = 0
        pair = s[idx:idx + 2]

        while pair:
            if value := mapping.get(pair):
                converted += value
                idx += 2
            else:
                converted += mapping[pair[0]]
                idx += 1
            pair = s[idx:idx + 2]

        return converted


solution = Solution1()

assert solution.romanToInt('III') == 3
assert solution.romanToInt('LVIII') == 58
assert solution.romanToInt('MCMXCIV') == 1994


class Solution2:
    def romanToInt(self, s):
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        converted = 0

        for idx in range(len(s)):
            if idx + 1 < len(s) and mapping[s[idx]] < mapping[s[idx + 1]]:
                converted -= mapping[s[idx]]
            else:
                converted += mapping[s[idx]]

        return converted


solution2 = Solution2()

assert solution2.romanToInt('III') == 3
assert solution2.romanToInt('LVIII') == 58
assert solution2.romanToInt('MCMXCIV') == 1994
