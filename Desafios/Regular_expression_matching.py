"""
Dada uma string de entrada s e um padrão p, implemente a correspondência de expressão regular com suporte para '.'e '*'onde:

'.'Corresponde a qualquer caractere único.
'*'Corresponde a zero ou mais elementos anteriores.
A correspondência deve cobrir toda a sequência de entrada (não parte dela).

Exemplo 1:

Entrada: s = "aa", p = "a"
 Saída: falso
 Explicação: "a" não corresponde à string inteira "aa".
Exemplo 2:

Entrada: s = "aa", p = "a*"
 Saída: verdadeiro
 Explicação: '*' significa zero ou mais do elemento precedente, 'a'. Portanto, ao repetir 'a' uma vez, ele se torna "aa".
Exemplo 3:

Entrada: s = "ab", p = ".*"
Saída: true
Explicação: ".*" significa "zero ou mais (*) de qualquer caractere (.)".
 
Restrições:
1 <= s.length <= 20
1 <= p.length <= 20
scontém apenas letras minúsculas do inglês.
pcontém apenas letras minúsculas do inglês, '.', e  '*'.
É garantido que para cada aparição do personagem '*', haverá um personagem anterior válido para corresponder.
"""

class Solution(object):
    def isMatch(self, s, p):
        def match(i, j):
            if j == len(p):
                return i == len(s)
            
            # Verifca se o caracter atual casa
            current_match = i < len(s) and (p[j] == s[i] or p[j]== '.')

            # Se o proximo caracter é '*', temos duas opções
            if j + 1 < len(p) and p[j + 1] == '*':
                # Pula o grupo 'caractere*' ou usa o caracter se ele casar
                return match(i, j + 2) or (current_match and match(i + 1, j))
            else:
                return current_match and match(i + 1, j + 1)
            
        return match(0, 0)
    
sol = Solution()
print(sol.isMatch('aa', 'a'))
print(sol.isMatch('aa', 'a*'))
print(sol.isMatch('ab', '.*'))