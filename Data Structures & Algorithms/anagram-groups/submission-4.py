class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for s in strs:
            ss="".join(sorted(s))   #sorted(s) → sorted("eat") → ['a', 'e', 't'] (list of characters, alphabetically sorted)
# ''.join(['a', 'e', 't']) → "aet" (joins the list into a string with no separator)
# sortedS = "aet"
            res[ss].append(s)
        return list(res.values())


#   With list():
# return list(res.values())
# # Returns: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# # Type: <class 'list'>

# # Without list():
# return res.values()
# # Returns: dict_values([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
# # Type: <class 'dict_values'>











#The list parameter tells defaultdict: "Whenever someone accesses a key that doesn't exist, automatically create an empty list [] for that key."   
#res = {}
# if "aet" not in res:
#     res["aet"] = []      # Create the list first
# res["aet"].append("eat") # Then append
