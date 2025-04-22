"""
Dado um inteiro com sinal de 32 bits x, retorne xcom seus dígitos invertidos . Se a inversão xfizer com que o valor saia do intervalo de inteiros com sinal de 32 bits , retorne .[-231, 231 - 1]0
Suponha que o ambiente não permite que você armazene inteiros de 64 bits (com ou sem sinal).

Exemplo 1:
Entrada: x = 123
 Saída: 321

Exemplo 2:
Entrada: x = -123
 Saída: -321

Exemplo 3:
Entrada: x = 120
 Saída: 21

Restrições:
-231 <= x <= 231 - 1

"""

class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x_new = str(abs(x))
        re_x = x_new[::-1]
        result = sign * int(re_x)
        if result < -2**31 or result > 2**31 -1 :
            return 0
        return result
    
sol = Solution()
print(sol.reverse(123))