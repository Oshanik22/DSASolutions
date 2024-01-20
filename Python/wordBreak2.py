class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.findSentences(s, set(wordDict), {})

    def findSentences(self, s, words, memoise):
        if s in memoise:
            return memoise[s]

        if not s:
            return [""]

        result = []
        for i in range(1, len(s)+1):
            prefix = s[:i]

            if prefix in words:
                suffixes = self.findSentences(s[i:], words, memoise)

                for suffix in suffixes:
                    if suffix:
                        sentence = prefix + " " + suffix
                    else:
                        sentence = prefix

                    result.append(sentence)
        memoise[s] = result
        return result