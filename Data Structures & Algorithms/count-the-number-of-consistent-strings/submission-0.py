class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        count = 0
        for word in words:
            valid = True
            for c in word:
                if c not in allow:
                    valid = False
                    break
            if valid:
                count += 1
        return count
