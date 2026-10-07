class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            word_s = str(sorted(word))
            if word_s in anagrams:
                anagrams[word_s].append(word)
            else:
                anagrams[word_s] = [word]

        return list(anagrams.values())