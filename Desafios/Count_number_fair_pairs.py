"""
Dado um array inteiro indexado em 0nums de tamanho ne dois inteiros lowere upper, retorne o número de pares justos .
Um par (i, j)é justo se:

0 <= i < j < n, e
lower <= nums[i] + nums[j] <= upper
 
Exemplo 1:

Entrada: nums = [0,1,7,4,4,5], inferior = 3, superior = 6
 Saída: 6
 Explicação: Existem 6 pares justos: (0,3), (0,4), (0,5), (1,3), (1,4) e (1,5).
Exemplo 2:

Entrada: nums = [1,7,9,2,5], inferior = 11, superior = 11
 Saída: 1
 Explicação: Há um único par justo: (2,3).
 
Restrições:
1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109

"""


class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        def countPairs(limit):
            count = 0
            left = 0
            right = len(nums) -1

            while left < right:
                if nums[left] + nums[right] <= limit:
                    count += right - left
                    left+=1
                else:
                    right-=1
            return count
        
        return countPairs(upper) - countPairs(lower - 1)

sol = Solution()
print(sol.countFairPairs([0,1,7,4,4,5], 3, 6)) # 6
print(sol.countFairPairs([1,7,9,2,5], 11, 11)) # 1
    
