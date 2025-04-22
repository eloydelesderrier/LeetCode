"""
Implemente a myAtoi(string s)função que converte uma string em um inteiro assinado de 32 bits.

O algoritmo myAtoi(string s)é o seguinte:

Espaço em branco : ignore qualquer espaço em branco inicial ( " ").
Sinalização : determine o sinal verificando se o próximo caractere é '-'ou '+', assumindo positividade se nenhum dos dois estiver presente.
Conversão : Lê o inteiro pulando os zeros à esquerda até que um caractere não dígito seja encontrado ou o fim da string seja alcançado. Se nenhum dígito for lido, o resultado será 0.
Arredondamento : Se o número inteiro estiver fora do intervalo de 32 bits de inteiros com sinal , arredonde-o para permanecer no intervalo. Especificamente, números inteiros menores que devem ser arredondados para , e números inteiros maiores que devem ser arredondados para .[-231, 231 - 1]-231-231231 - 1231 - 1
Retorna o inteiro como resultado final.

Exemplo 1:

Entrada: s = "42"

Saída: 42

Explicação:

Os caracteres sublinhados são os que são lidos e o cursor representa a posição atual do leitor. 
Passo 1: "42" (nenhum caractere é lido porque não há espaços em branco à esquerda) 
         ^ 
Passo 2: "42" (nenhum caractere é lido porque não há '-' nem '+') 
         ^ 
Passo 3: " 42 " ("42" é lido) 
           ^
Exemplo 2:

Entrada: s = " -042"

Saída: -42

Explicação:

Etapa 1: "    -042" (os espaços em branco à esquerda são lidos e ignorados) 
            ^ 
Etapa 2: "    - 042" ('-' é lido, então o resultado deve ser negativo) 
             ^ 
Etapa 3: " - 042 " ("042" é lido, os zeros à esquerda são ignorados no resultado) 
               ^
Exemplo 3:

Entrada: s = "1337c0d3"

Saída: 1337

Explicação:

Etapa 1: "1337c0d3" (nenhum caractere lido porque não há espaço em branco à esquerda) 
         ^ 
Etapa 2: "1337c0d3" (nenhum caractere lido porque não há '-' nem '+') 
         ^ 
Etapa 3: " 1337 c0d3" ("1337" é lido; a leitura para porque o próximo caractere não é um dígito) 
             ^

Exemplo 4:
Entrada: s = "0-1"
Saída: 0

Explicação:

Etapa 1: "0-1" (nenhum caractere é lido porque não há espaço em branco à esquerda) 
         ^ 
Etapa 2: "0-1" (nenhum caractere é lido porque não há '-' nem '+') 
         ^ 
Etapa 3: " 0 -1" ("0" é lido; a leitura para porque o próximo caractere não é um dígito) 
          ^

Exemplo 5:
Entrada: s = "palavras e 987"
Saída: 0

Explicação:
A leitura para no primeiro caractere não numérico 'w'.

Restrições:
0 <= s.length <= 200
sconsiste em letras inglesas (maiúsculas e minúsculas), dígitos ( 0-9), ' ', '+', '-', e '.'.

"""

class Solution(object):
    def myAtoi(self, s):
        chega_min, chega_max = -2**31, 2**31 -1
        i = 0
        n = len(s)
        result = 0
        sign = 1

        # 1. Ignora espaços em brancos
        while i < n and s[i] == ' ':
            i+=1

        # 2. Verifica o sinal
        if i < n and (s[i]== '-' or s[i]=='+'):
            sign = -1 if s[i] == '-' else 1
            i+=1

        # 3. Lê os digitos
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Verifica estouro antes de multiplicar por 10 e somar

            if result > (chega_max - digit) // 10:
                return chega_min if sign == -1 else chega_max

            result = result * 10 + digit
            i+=1

        return  sign * result 

        
     
sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -042"))
print(sol.myAtoi("1337c0d3"))
print(sol.myAtoi("0-1"))
print(sol.myAtoi("words and 987"))