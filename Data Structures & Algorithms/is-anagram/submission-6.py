class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = [s.count(i) for i in s]
        countsT = [t.count(i) for i in t]
        s_dict = {k:v for (k,v) in zip(s, countsS)}
        t_dict = {k:v for (k,v) in zip(t, countsT)}
        
        s_dict = dict(sorted(s_dict.items()))
        t_dict = dict(sorted(t_dict.items()))
        
        if s_dict == t_dict:
            return True
        return False       