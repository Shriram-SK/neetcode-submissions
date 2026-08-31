class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = tuple(sorted(word))
            seen.setdefault(key, []).append(word)
        
        return list(seen.values())