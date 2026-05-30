class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hashmap1={}  #created hashmap with elements and frequencies
        for i in nums:
            hashmap1[i]=1+hashmap1.get(i,0)

        l=[]
        for ele,fre in hashmap1.items():
            l.append([fre,ele])
        l.sort()  # we got sorted dictonary by frequencies

        #now get last elemnts from list
        res=[]
        
        while len(res)<k:
            res.append(l.pop()[1])  #1 means give key from [3,1]
        return res
        
    




        

#key is element and value is frequency of tha element..
#in dictonary the elments are sorted by key not value so we want list to sort based on frequency

#         arr=[]   #adding all ements in a list so that we can sort
#         for key,value in hashmap.items():
#             arr.append([value,key])  #Python sorts based on the first element of each pair (frequency).
# #                                       This gives the list ordered by frequency.
#         arr.sort()  #arr is changed now and it return none                   

#         res=[]   #this array we want
#         while len(res)<k:         #arr=[[value,key],[value,key]]
#             res.append(arr.pop()[1])             #pop method deleted from end and 1 means key
#         return res



        # hashmap={}
        # for i in nums:
        #     hashmap[i]=1+hashmap.get(i,0)  #created hashmap 

        # freq = []    
        # for i in range(len(nums) + 1):
        #     freq.append([])  #creating empty list. no of empty list is equal to input size
        #     #input size 6 so 6 lists in freq..

        

        # #[1,1,1,2,2,100]
        # for number,count in hashmap.items():  #(1,3),(2,2),(100,1)
        #     freq[count].append(number) #adding element in freq list inside list based on index
        
        # res=[]
        # for i in range(len(nums),0,-1):
        #     for n in freq[i]:   #n is the list assign to each index and i is the index
        #         res.append(n)  #append numbers in result 
        #         if len(res)==k:
        #             return res