"""
Dada uma string scontendo apenas os caracteres '(', ')', '{', '}', '['e ']', determine se a string de entrada é válida.

Uma string de entrada é válida se:
Os colchetes abertos devem ser fechados pelo mesmo tipo de colchetes.
Os colchetes abertos devem ser fechados na ordem correta.
Cada colchete fechado tem um colchete aberto correspondente do mesmo tipo.
 

Exemplo 1:

Entrada: s = "()"
Saída: verdadeiro

Exemplo 2:
Entrada: s = "()[]{}"

Saída: verdadeiro
Exemplo 3:

Entrada: s = "(]"
Saída: falso

Exemplo 4:
Entrada: s = "([])"

Saída: verdadeiro

Restrições:

1 <= s.length <= 104
sconsiste apenas em parênteses '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
    
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
    
        return not stack

sol = Solution()
print(sol.isValid("()"))  
print(sol.isValid("()[]{}"))  
print(sol.isValid("(]"))  
print(sol.isValid("([])"))  
print(sol.isValid("{[()]}")) 
print(sol.isValid("{[(])}"))  