"""
ete símbolos diferentes representam algarismos romanos com os seguintes valores:

Símbolo	Valor
  I	     1
  V	     5
  X	     10
  L	     50
  C	     100
  D	     500
  M	     1000

Os algarismos romanos são formados pela adição das conversões dos valores decimais, do maior para o menor. A conversão de um valor decimal em algarismo romano segue as seguintes regras:
Se o valor não começar com 4 ou 9, selecione o símbolo do valor máximo que pode ser subtraído da entrada, anexe esse símbolo ao resultado, subtraia seu valor e converta o restante em um algarismo romano.
Se o valor começar com 4 ou 9, use a  forma subtrativa  que representa um símbolo subtraído do símbolo seguinte, por exemplo, 4 é 1 ( I) menor que 5 ( V): IV e 9 é 1 ( I) menor que 10 ( X): IX. Somente as seguintes formas subtrativas são usadas: 4 ( IV), 9 ( IX), 40 ( XL), 90 ( XC), 400 ( CD) e 900 ( CM).
Somente potências de 10 ( I, X, C, M) podem ser anexadas consecutivamente, no máximo 3 vezes, para representar múltiplos de 10. Não é possível anexar 5 ( V), 50 ( L) ou 500 ( D) várias vezes. Se precisar anexar um símbolo 4 vezes, use a forma subtrativa .
Dado um número inteiro, converta-o em um numeral romano.

 
Exemplo 1:

Entrada: num = 3749

Saída: "MMMDCCXLIX"

Explicação:

3000 = MMM como 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC como 500 (D) + 100 (C) + 100 (C)
  40 = XL como 10 (X) menos de 50 (L)
   9 = IX como 1 (I) menos 10 (X)
Nota: 49 não é 1 (I) a menos que 50 (L) porque a conversão é baseada em casas decimais
Exemplo 2:

Entrada: num = 58
Saída: "LVIII"

Explicação:

50 = L
 8 = VIII
Exemplo 3:

Entrada: num = 1994

Saída: "MCMXCIV"

Explicação:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 
Restrições:
1 <= num <= 3999

"""

class Solution(object):
    def intToRoman(self, num):
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        
        ]
        result = []
        for values, symbol in roman_numerals:
            if num == 0:
                break
            count = num // values
            result.append(symbol * count)
            num -= count * values
        return ''.join(result)
    
sol = Solution()
print(sol.intToRoman(58))  # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
        