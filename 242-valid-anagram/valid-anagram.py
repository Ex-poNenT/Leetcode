class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = {}
        for i in s :
            if i in m1:
                m1[i] +=1 
            else :
                m1[i] = 1
        m2 = {}
        for i in t :
            if i in m2 :
                m2[i] += 1
            else :
                m2[i] = 1
        return m1 == m2 