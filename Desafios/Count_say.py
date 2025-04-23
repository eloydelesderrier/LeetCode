"""
A sequência de contagem e fala é uma sequência de sequências de dígitos definida pela fórmula recursiva:

countAndSay(1) = "1"
countAndSay(n)é a codificação de comprimento de execução de countAndSay(n - 1).
A codificação de comprimento de execução (RLE) é um método de compressão de strings que funciona substituindo caracteres idênticos consecutivos (repetidos 2 ou mais vezes) pela concatenação do caractere e o número que marca a contagem dos caracteres (comprimento da sequência). Por exemplo, para comprimir a string , "3322251"substituímos "33"por "23", substituímos "222"por "32", substituímos "5"por "15"e substituímos "1"por "11". Assim, a string comprimida se torna "23321511".

Dado um inteiro positivo n, retorne o elemento da sequência de contagem e fala .nth

Exemplo 1:
Entrada: n = 4
Saída: "1211"

Explicação:
countAndSay(1) = "1" 
countAndSay(2) = RLE de "1" = "11" 
countAndSay(3) = RLE de "11" = "21" 
countAndSay(4) = RLE de "21" = "1211"
Exemplo 2:

Entrada: n = 1
Saída: "1"

Explicação:
Este é o caso base.

Restrições:

1 <= n <= 30

"""

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            result = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    result += str(count) + prev[i - 1]
                    count = 1
            result += str(count) + prev[-1]
            return result
        
sol = Solution()
print(sol.countAndSay(4))
print(sol.countAndSay(1))  