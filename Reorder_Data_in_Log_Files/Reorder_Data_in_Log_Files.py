class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha, digit = [], []
        for word in logs:
            if (word.split()[1]).isdigit():
                digit.append(word)
            else:
                alpha.append(word)
        alpha.sort(key= lambda x:(x.split()[1:], x.split()[0]))
        return alpha + digit