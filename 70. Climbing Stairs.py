"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2

Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3

Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

"""


class Solution(object):
    """
    Как сводят от дерева решений к ряду Фибоначчи хорошо показано в https://www.youtube.com/watch?v=Y0lT9Fck7qI

    К этому возможно получилось бы самостоятельно, если составить дерево и приглядеться к результату внимательно
    Можно было бы заметить, что есть повторяющиеся поддеревья и так прийти к единственной ветке (см. видео)

    В который раз убеждаюсь, что стоит только внимательно присмотреться к данным, то можно прийти к решению

    """
    def climbStairs(self, n):
        one, two = 1, 1

        for _ in range(n - 1):
            one, two = two, one + two

        return two
