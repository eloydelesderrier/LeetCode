""" 
Dado um conjunto de inteiros nums e um inteiro target, retorne os índices dos dois números de forma que a soma deles sejatarget .
Você pode assumir que cada entrada terá exatamente uma solução e não pode usar o mesmo elemento duas vezes.
Você pode retornar a resposta em qualquer ordem.

Exemplo 1:

Entrada: nums = [2,7,11,15], alvo = 9
 Saída: [0,1]
 Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].
Exemplo 2:

Entrada: nums = [3,2,4], alvo = 6
 Saída: [1,2]
Exemplo 3:

Entrada: nums = [3,3], alvo = 6
 Saída: [0,1]
 
Restrições:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Existe apenas uma resposta válida.

Acompanhamento:  Você consegue criar um algoritmo que seja menor que a complexidade de tempo?O(n2) 
"""

class solution(object):
    def TwoSum(self, nums, target):
        indice_num = {}  # Armazena números e seu índice
        for i, num in enumerate(nums):
            val = target - num
            if val in indice_num:
               return [indice_num[val], i]
            indice_num[num] = i
    


valor = solution()
print(valor.TwoSum([2,7,11,15], 9))
print(valor.TwoSum([3,2,4], 6))
print(valor.TwoSum([3,3], 6))

    
  





