"""
Os algarismos romanos são representados por sete símbolos diferentes:  I, V, X, L, C, De M.

Símbolo  Valor 
I          1 
V          5 
X          10 
L          50 
C          100 
D          500 
M          1000

Por exemplo,  2é escrito como II em algarismos romanos, apenas duas unidades somadas. 12é escrito como  XII, que é simplesmente X + II. O número 27é escrito como XXVII, que é XX + V + II.

Os algarismos romanos são geralmente escritos do maior para o menor, da esquerda para a direita. No entanto, o algarismo para quatro não é IIII. Em vez disso, o número quatro é escrito como IV. Como o um está antes do cinco, nós o subtraímos, resultando em quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Há seis casos em que a subtração é usada:

Ipode ser colocado antes de V(5) e X(10) para formar 4 e 9. 
Xpode ser colocado antes de L(50) e C(100) para fazer 40 e 90. 
Cpode ser colocado antes de D(500) e M(1000) para fazer 400 e 900.
Dado um numeral romano, converta-o em um inteiro.

Exemplo 1:

Entrada: s = "III"
 Saída: 3
 Explicação: III = 3.
Exemplo 2:

Entrada: s = "LVIII"
 Saída: 58
 Explicação: L = 50, V= 5, III = 3.
Exemplo 3:

Entrada: s = "MCMXCIV"
 Saída: 1994
 Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.
 
Restrições:

1 <= s.length <= 15
scontém apenas os caracteres ('I', 'V', 'X', 'L', 'C', 'D', 'M').
É garantido  que sé um numeral romano válido no intervalo [1, 3999].

"""

class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_dict[char]

            if value < prev_value:
                total -=value
            else:
                total +=value

            prev_value = value
        
        return total
         
sol = Solution()
print(sol.romanToInt("III"))  # Output: 3
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
print(sol.romanToInt("IV"))  # Output: 4
