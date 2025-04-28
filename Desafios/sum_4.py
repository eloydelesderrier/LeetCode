"""
Dado um conjunto numsde ninteiros, retorne um conjunto de todos os quádruplos únicos [nums[a], nums[b], nums[c], nums[d]] tais que:

0 <= a, b, c, d < n
a, b, c, e dsão distintos .
nums[a] + nums[b] + nums[c] + nums[d] == target
Você pode retornar a resposta em qualquer ordem .

Exemplo 1:

Entrada: nums = [1,0,-1,0,-2,2], alvo = 0
 Saída: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Exemplo 2:

Entrada: nums = [2,2,2,2,2], alvo = 8
 Saída: [[2,2,2,2]]
 
Restrições:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution(object):
    def fourSum(self, nums, target):
    
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left +=1
                        right -= 1
                    elif total < target:
                        left +=1
                    else:
                        right -=1
        return list(res)
    

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0)) 
print(sol.fourSum([2,2,2,2,2], 8)) 