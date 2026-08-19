class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHash = dict()
        tHash = dict()
        for c in s:
            if c in sHash.keys():
                sHash[c] = sHash[c] + 1
            else:
                sHash[c] = 1
        for c in t:
            if c in tHash.keys():
                tHash[c] =tHash[c] + 1
            else:
                tHash[c] = 1
        if len(sHash) != len(tHash):
            return False
        for l in sHash.keys():
            # if sHash[l] not in tHash:
            #     return False
            if sHash.get(l) != tHash.get(l):
                return False
        return True
