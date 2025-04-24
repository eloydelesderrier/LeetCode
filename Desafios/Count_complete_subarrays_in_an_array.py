"""
Você recebe uma matriz numscomposta de números inteiros positivos .
Chamamos um subarray de um array de completo se a seguinte condição for satisfeita:
O número de elementos distintos no subarray é igual ao número de elementos distintos no array inteiro.
Retorna o número de submatrizes completas .
Um subarray é uma parte contígua não vazia de um array.

Exemplo 1:

Entrada: nums = [1,3,1,2,2]
 Saída: 4
 Explicação: Os subarrays completos são os seguintes: [1,3,1,2], [1,3,1,2,2], [3,1,2] e [3,1,2,2].
Exemplo 2:

Entrada: nums = [5,5,5,5]
 Saída: 10
 Explicação: A matriz consiste apenas no inteiro 5, portanto, qualquer submatriz está completa. O número de submatrizes que podemos escolher é 10.
 
Restrições:
1 <= nums.length <= 1000
1 <= nums[i] <= 2000

"""
class Solution(object):
    def countCompleteSubarrays(self, nums):
        n = len(set(nums))
        count = 0
        for i in range(len(nums)):
            distinct_count = set()
            for j in range(i, len(nums)):
                distinct_count.add(nums[j])
                if len(distinct_count) == n:
                    count+=1
        return count

sol = Solution()
print(sol.countCompleteSubarrays([1,3,1,2,2])) # 4
print(sol.countCompleteSubarrays([5,5,5,5])) # 10