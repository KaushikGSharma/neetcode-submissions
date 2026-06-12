class Solution:

    def encode(self, strs: List[str]) -> str:
        string_to_join=[]
        for word in strs:
            word_check_sum=len(word)
            string_to_join.append(str(word_check_sum) + "\u00B0" + word)
        string_joined="\u00A9".join(string_to_join)
        return string_joined



    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        if s==None or len(s)==0:
            return decoded_string
        string_separated_cs=s.split("\u00A9")
        for word_with_cs in string_separated_cs:
            length,word=word_with_cs.split("\u00B0")
            decoded_string.append(word)
        return decoded_string

            
