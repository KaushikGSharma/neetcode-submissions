from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orginal_mapping_dict=defaultdict(list)
        result=[]
        for s in strs:
            char_map=Counter(s)
            sorted_char_dict=dict(sorted(char_map.items(), key=lambda item:item[0]))
            orginal_mapping_dict[str(sorted_char_dict)].append(s)
        for key,value in orginal_mapping_dict.items():
            result.append(value)
        return result
