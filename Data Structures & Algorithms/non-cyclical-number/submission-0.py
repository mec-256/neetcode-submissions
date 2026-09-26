class Solution:
    def isHappy(self, n: int) -> bool:
        

     def cal_sum(n):
        sum = 0
        while(n>0):
            num = n%10
            sum += num ** 2
            n = n//10
        return sum     

     seen =  set()

     while n!= 1 and n not in seen:
         seen.add(n)
         n = cal_sum(n)


     return n==1    



                 