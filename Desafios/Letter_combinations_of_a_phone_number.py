"""
Dada uma string contendo dígitos de2-9 ≤ ...
Abaixo, apresentamos um mapeamento de dígitos para letras (como nos botões do telefone). Observe que 1 não corresponde a nenhuma letra.

Exemplo 1:

Entrada: dígitos = "23"
 Saída: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Exemplo 2:

Entrada: dígitos = ""
 Saída: []
Exemplo 3:

Entrada: dígitos = "2"
 Saída: ["a","b","c"]
 

Restrições:

0 <= digits.length <= 4
digits[i]é um dígito no intervalo ['2', '9'].
"""

class Solution(object):
    def letterCombinations(self, digits):

        if not digits:
            return []
        
        phone_number = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combinations = ['']
        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for letter in phone_number[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations
        return combinations
    
sol = Solution()
print(sol.letterCombinations("23"))  
print(sol.letterCombinations(""))    

       
