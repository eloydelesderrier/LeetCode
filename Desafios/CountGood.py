""" 
Dado um array de inteiros numse um inteiro k, retorne o número de subarrays bons nums de .
Um subarray arré bom se houver pelo menosk pares de índices (i, j)tais que i < je arr[i] == arr[j].
Um subarray é uma sequência contígua não vazia de elementos dentro de um array.

Exemplo 1:
Entrada: nums = [1,1,1,1,1], k = 10
 Saída: 1
 Explicação: O único subarray bom é o próprio array nums.

 Exemplo 2:
Entrada: nums = [3,1,4,3,2,2,4], k = 2
 Saída: 4
 Explicação: Existem 4 submatrizes diferentes e boas: 
- [3,1,4,3,2,2] que tem 2 pares. 
- [3,1,4,3,2,2,4] que tem 3 pares. 
- [1,4,3,2,2,4] que tem 2 pares. 
- [4,3,2,2,4] que tem 2 pares.
 
Restrições:
1 <= nums.length <= 105
1 <= nums[i], k <= 109

"""
from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        numDict = dict()
        res = 0
        pares = 0
        numIdx = 0

        for direita in nums:
            if direita in numDict:
                pares += numDict[direita]
                numDict[direita] += 1
            else:
                numDict[direita] = 1

            while pares >= k:
                numDict[nums[numIdx]] -= 1
                pares -= numDict[nums[numIdx]]
                numIdx += 1
            res += numIdx

        return res


sol = Solution()
print(sol.countGood([1,1,1,1,1], 10))
print(sol.countGood([3,1,4,3,2,2,4], 2))  