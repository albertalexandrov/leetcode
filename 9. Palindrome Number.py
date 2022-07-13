"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""


class Solution1:
    """
    Простое решение, но требующее дополнительную память О(2n) -
    перевести число в строку и сравнить с реверстнутой строкой

    Стоит обратить на работу с граничными случаями:
    - если х меньше 0, то такое число не яявляется палиндромом
    - если число заканчивается на 0 (остаток от деления равен 0) то такое число также не является палиндром

    Эти крайние случаи избавят нас от необходимости преобразовывать в строку и тратить время и память

    """
    def isPalindrome(self, x):
        if x < 0 or x % 10 == 0:
            return False
        as_string = str(x)
        return as_string == as_string[::-1]


class Solution2:
    """
    Решение посложнее, но не тратящее память (если переводить в строку, то каждый символ - 1 байт)

    В этом решении разворачивается число, причем только его половина
    Условие x == reversed_num // 10 - для чисел с нечетным количеством цифр

    Обработка крайних случаев такая же как в первом варианте

    """
    def isPalindrome(self, x):
        if x < 0 or x % 10 == 0:
            return False
        reversed_num = 0
        while x > reversed_num:
            x, remainder = divmod(x, 10)
            reversed_num = reversed_num * 10 + remainder
        return x == reversed_num or x == reversed_num // 10


solution = Solution2()
assert solution.isPalindrome(121) is True
assert solution.isPalindrome(-121) is False
assert solution.isPalindrome(10) is False
