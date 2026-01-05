'''
Time: O(n * m)
Space: O(k)

n = Length of array
m = Average length of each word
k = Length of res
'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:   # type: ignore
        res = []
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res