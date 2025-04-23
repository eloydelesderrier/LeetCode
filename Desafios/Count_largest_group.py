"""
É fornecido um inteiro n.

Cada número de 1a né agrupado de acordo com a soma de seus dígitos.

Retorna o número de grupos que têm o maior tamanho .

Exemplo 1:

Entrada: n = 13
 Saída: 4
 Explicação: Há 9 grupos no total, eles são agrupados de acordo com a soma de seus dígitos de números de 1 a 13: 
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. 
Há 4 grupos com maior tamanho.
Exemplo 2:

Entrada: n = 2
 Saída: 2
 Explicação: Existem 2 grupos [1], [2] de tamanho 1.
 
Restrições:
1 <= n <= 104

"""

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]*37
        for i in range(1, n+1):
            count[sum(map(int, str(i)))] += 1
        max_count = max(count)
        return count.count(max_count)
    
sol = Solution()
print(sol.countLargestGroup(13)) # 4
print(sol.countLargestGroup(2)) # 2