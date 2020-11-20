class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = re.split(r'\W+', paragraph.lower())
        word = [element for element in word if element not in banned]
        word = max(word, key = word.count)
        return word