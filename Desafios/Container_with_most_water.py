"""
Você recebe um array de inteiros heightde comprimento n. Há nlinhas verticais desenhadas de forma que os dois pontos finais da linha sejam e .ith(i, 0)(i, height[i])
Encontre duas retas que, juntamente com o eixo x, formem um recipiente, de modo que o recipiente contenha mais água.
Retorne a quantidade máxima de água que um recipiente pode armazenar .
Observe que você não pode inclinar o recipiente.

Entrada: altura = [1,8,6,2,5,4,8,3,7]
 Saída: 49
 Explicação: As linhas verticais acima são representadas pela matriz [1,8,6,2,5,4,8,3,7]. Neste caso, a área máxima de água (seção azul) que o recipiente pode conter é 49.
Exemplo 2:

Entrada: altura = [1,1]
 Saída: 1
 
Restrições:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) -1

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return max_area
    

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # Saída: 49
print(sol.maxArea([1,1])) # Saída: 1