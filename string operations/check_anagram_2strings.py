class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        i3 = 0

        if not s:
            i3 = 1

        if not t:
            if i3 == 1:
                return True

        s1 = [q for q in s]

        s2 = [q for q in t]

        for ch in s1:
            if ch in s2:
                s2.remove(ch)
            else:
                return False

        return True
