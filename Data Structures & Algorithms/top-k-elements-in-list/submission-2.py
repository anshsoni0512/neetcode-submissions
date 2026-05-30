class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap={}
        for i in nums:
            hashmap[i]=1+hashmap.get(i,0)  #creted hashmap 

#key is element and value is frequency of tha element..


        arr=[]   #adding all ements in a list so that we can sort
        for key,value in hashmap.items():
            arr.append([value,key])  #Python sorts based on the first element of each pair (frequency).
#                                       This gives the list ordered by frequency.
        arr.sort()                   

        res=[]   #this array we want
        while len(res)<k:         #arr=[[value,key],[value,key]]
            res.append(arr.pop()[1])             #pop method deleted from end and 1 means key
        return res