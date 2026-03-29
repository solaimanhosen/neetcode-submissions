class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            hash_key = "".join(sorted(word))
            groups[hash_key].append(word)

        return list(groups.values())
