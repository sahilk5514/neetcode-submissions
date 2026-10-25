from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        if len(s) != len(t):
            return False
    
        else:
            if set(s) != set(t):
                return False
            else: 
                    result1 = Counter(s)
                    result2 = Counter(t)

        if result1 == result2:
            return True 
        return False

                
                
        