"""
Dado um conjunto de inteiros numsde comprimento ne um inteiro target, encontre três inteiros em numsque a soma seja mais próxima de target.
Retorna a soma dos três números inteiros .
Você pode assumir que cada entrada teria exatamente uma solução.

Exemplo 1:
Entrada: nums = [-1,2,1,-4], alvo = 1
 Saída: 2
 Explicação: A soma que mais se aproxima do alvo é 2. (-1 + 2 + 1 = 2).
Exemplo 2:

Entrada: nums = [0,0,0], alvo = 1
 Saída: 0
 Explicação: A soma mais próxima do alvo é 0. (0 + 0 + 0 = 0).
 
Restrições:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        
        return closest_sum