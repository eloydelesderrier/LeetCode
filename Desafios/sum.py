"""
Dado um array de inteiros nums, retorne todos os tripletos [nums[i], nums[j], nums[k]]tais que i != j, i != k, e j != k, e nums[i] + nums[j] + nums[k] == 0.
Observe que o conjunto de soluções não deve conter tripletos duplicados.

Exemplo 1:

Entrada: nums = [-1,0,1,2,-1,-4]
 Saída: [[-1,-1,2],[-1,0,1]]
 Explicação:  
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. 
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. 
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. 
Os tripletos distintos são [-1,0,1] e [-1,-1,2]. 
Observe que a ordem da saída e a ordem dos tripletos não importam.
Exemplo 2:

Entrada: nums = [0,1,1]
 Saída: []
 Explicação: O único tripleto possível não soma 0.
Exemplo 3:

Entrada: nums = [0,0,0]
 Saída: [[0,0,0]]
 Explicação: O único tripleto possível soma 0.
 
Restrições:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        result = []

        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) -1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left+=1
                elif total > 0:
                    right -=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
        return result

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1]))  # Output: []
print(sol.threeSum([0,0,0]))  # Output: [[0,0,0]]