class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = [_ for _ in magazine]
        for i in ransomNote:
            if i not in magazine:
                return False
            elif i in magazine:
                magazine.remove(i)
        else:
            return True
        
