class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


# res = {}
# if "aet" not in res:
#     res["aet"] = []  # Create empty list manually
# res["aet"].append("eat")  # Now it works


        res=defaultdict(list)
        for s in strs:
            ss="".join(sorted(s))   #sorted(s) → sorted("eat") → ['a', 'e', 't'] (list of characters, alphabetically sorted)
# ''.join(['a', 'e', 't']) → "aet" (joins the list into a string with no separator)
# sortedS = "aet"
            res[ss].append(s)  # if you append in key it becomes value
        return list(res.values())  # i want values but in form of list


#   With list():
# return list(res.values())
# # Returns: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# # Type: <class 'list'>

# # Without list():
# return res.values()
# # Returns: dict_values([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
# # Type: <class 'dict_values'>


    #  res = defaultdict(list)
    #     for s in strs:   # for every word 'eat'
    #         count = [0] * 26
    #         for c in s:  # count how many times e, a and t comes
    #             count[ord(c) - ord('a')] += 1  # creating a key
    #         res[tuple(count)].append(s)  # for the above created key add value
    #     return list(res.values())










#The list parameter tells defaultdict: "Whenever someone accesses a key that doesn't exist, automatically create an empty list [] for that key."   
#res = {}
# if "aet" not in res:
#     res["aet"] = []      # Create the list first
# res["aet"].append("eat") # Then append
