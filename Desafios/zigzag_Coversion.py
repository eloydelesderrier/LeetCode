"""
A sequência "PAYPALISHIRING"é escrita em um padrão de ziguezague em um determinado número de linhas como este: (você pode querer exibir esse padrão em uma fonte fixa para melhor legibilidade)

PAHN
APLSIIG
YIR
E então leia linha por linha:"PAHNAPLSIIGYIR"

Escreva o código que receberá uma string e fará essa conversão dado um número de linhas:

string convert(string s, int numRows);
 
Exemplo 1:
Entrada: s = "PAYPALISHIRING", numRows = 3
 Saída: "PAHNAPLSIIGYIR"

Exemplo 2:
Entrada: s = "PAYPALISHIRING", numRows = 4
 Saída: "PINALSIGYAHRPI"
 Explicação:
ALFINETE
ALSIG
YAHR
PI

Exemplo 3:
Entrada: s = "A", numRows = 1
 Saída: "A"
 
Restrições:
1 <= s.length <= 1000
sconsiste em letras inglesas (minúsculas e maiúsculas) ','e '.'.
1 <= numRows <= 1000  

"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        
        rows = [''] * numRows

        linha_atual = 0
        step = 1

        for char in s:
            rows[linha_atual] += char

            if linha_atual == 0:
                step = 1
            
            elif linha_atual == numRows - 1:
                step = -1
            
            linha_atual += step
        
        return ''.join(rows)

        

sol = Solution()
print(sol.convert('PAYPALISHIRING', 4))