"""
Two words are anagrams of each other if they both contain the same letters.
Write a function that will find all the anagrams of a given word.
Example : anagrams("baba") => ["aabb", "abab", "abba", "bbaa", "baab"]
"""

from itertools import permutations


def anagrams(word):
    if len(word) > 0:
        possible_anagrams = set(permutations(word))
        anagrams_list = ["".join(item) for item in possible_anagrams]
        anagrams_list.remove(word)
        return anagrams_list
    else:
        return word


if __name__ == "__main__":
    anagrams("baba")
