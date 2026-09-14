class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        
        for i in range(0,n+1):
            s=bin(i)
            count = 0
            for j in  s:
                if j=='1':
                    count+=1
                
            arr.append(count)    

        return arr   

