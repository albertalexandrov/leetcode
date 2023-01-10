"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

"""
from collections import defaultdict

# основная сложность была с тем, чтобы сделать из каждого слова ключ,
# который был бы общим для анаграмм.  сначала был применен Counter,
# который не хешируемый и который невозможно использовать в качестве
# ключа словаря (также была попытка преобразовать его в tuple, но это
# не давало нужного результата, так как ключи в Counter могли быть в
# произвольном порядке)


class Solution1:
    """Решение 1.

    Time: O(m * nlog(n))
    Space: O(m * n)

    Неоптимальное решение с точки зрения скорости

    Временная сложность обусловлена тем, что каждое слово (m) нужно отсортировать (nlog)
    Пространственная сложность обусловлена тем, что каждое применение sorted возвращает новый объект

    """
    def group_anagrams(self, strs):
        holder = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            holder[key].append(word)

        return holder.values()


class Solution2:
    """Решение 2.

    Time: O(m * n)
    Space: O(n)

    Подсмотренное решение

    Как было написано выше, были проблемы с тем, чтобы придумать ключ, который бы описывал
    разные анаграммы.  Таким ключом становится список, в котором позиции равны порядковому
    номеру буквы в алфавите.  Таким образом, мы гарантируем, что анаграммы имеют одинаковый
    ключ без необходимости сортировки

    """

    def group_anagrams(self, strs):
        holder = defaultdict(list)

        for word in strs:
            key = [0] * 26

            for letter in word:
                pos = ord(letter) - ord('a')  # ord('a') принимаем за нулевую позицию
                key[pos] += 1

            holder[tuple(key)].append(word)

        return holder.values()
