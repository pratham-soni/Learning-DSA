import math
class Solution:
    def getGcd(self, A, B):
        if (B==0):
            return A
        return self.getGcd(B, A%B)

    def lcmAndGcd(self, A , B):
        # code here 
        gcd = self.getGcd(A,B)
        lcm = (A*B)//gcd
        return (lcm, gcd)

sol = Solution()
# print(sol.getGcd(5,10))
# print(sol.lcmAndGcd(663499, 452))

def checkArmstrong(n):
    #write your code here !!!!!!!!!
    originalNum = n
    lenOfNum = len(str(n))
    res = 0
    while n:
        if res <= originalNum:
            lastNum = n%10
            res += lastNum ** lenOfNum
            n = n//10
            print(res)
        else:
            break
    return res == originalNum

print(checkArmstrong(1634))
print(math.sqrt(36))