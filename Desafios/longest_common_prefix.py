"""
Escreva uma função para encontrar a maior string de prefixo comum entre uma matriz de strings.
Se não houver um prefixo comum, retorne uma string vazia "".

Exemplo 1:

Entrada: strs = ["flor","fluxo","voo"]
 Saída: "fl"
Exemplo 2:

Entrada: strs = ["cachorro","carro de corrida","carro"]
 Saída: ""
 Explicação: Não há um prefixo comum entre as strings de entrada.
 
Restrições:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i]consiste apenas em letras minúsculas do inglês se não estiver vazio.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Inicializa o prefixo comum com a primeira string
        prefix = strs[0]

        #Iterar sobre as strings restanes
        for s in strs[1:]:
            # Enquanto o prefixo não for um prefixo da string atual, reduz o prefixo
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix


            