class Solution:

#concatinaiton of string for encoding

    def encode(self, strs: List[str]) -> str:
        res=''
        for i in strs: #['neet','code']   i='neet then i='code'
            res=res+str(len(i))+'#'+i # res= 4#neet then res=4#neet+4#code 
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0   #this pointer for moving to next word
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j=j+1
            length=int(s[i:j])  # we want that integer at starting   slicing retuns string
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res


