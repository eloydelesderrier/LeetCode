"""
Dado um array de inteiros indexados em 0nums de comprimento ne um inteiro k, retorne o número de pares (i, j) onde 0 <= i < j < n , tal que nums[i] == nums[j] e (i * j) é divisível por k .

Exemplo 1:
Entrada: nums = [3,1,2,2,2,1,3], k = 2
 Saída: 4
 Explicação:
Existem 4 pares que atendem a todos os requisitos:
- nums[0] == nums[6], e 0 * 6 == 0, que é divisível por 2.
- nums[2] == nums[3], e 2 * 3 == 6, que é divisível por 2.
- nums[2] == nums[4], e 2 * 4 == 8, que é divisível por 2.
- nums[3] == nums[4], e 3 * 4 == 12, que é divisível por 2.
Exemplo 2:

Entrada: nums = [1,2,3,4], k = 1
 Saída: 0
 Explicação: Como nenhum valor em nums é repetido, não há pares (i,j) que atendam a todos os requisitos.
 
Restrições:
1 <= nums.length <= 100
1 <= nums[i], k <= 100

"""

class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k ==0:
                    count+=1
        
        return count
    

sol = Solution()
print(sol.countPairs([3,1,2,2,2,1,3], 2))
print(sol.countPairs([1,2,3,4], 1))