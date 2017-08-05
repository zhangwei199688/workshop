'''
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''
class Solution(object):
    def countAndSay(self, n):
        if n==1:
            return "1"
        else:
            count=[1]
            for i in range(n-1):
                a=count[0]
                count.append("X")
                n=0
                lis=[]
                for j in range(len(count)):
                    if a==count[j]:
                        n+=1
                    else:
                        lis.append(str(n))
                        lis.append(str(a))
                        a=count[j]
                        n=0
                        n+=1
                count=lis
            return "".join(count)