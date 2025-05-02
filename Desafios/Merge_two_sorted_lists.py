"""
São fornecidos os cabeçalhos de duas listas encadeadas classificadas list1e list2.
Mescle as duas listas em uma lista ordenada . A lista deve ser formada juntando os nós das duas primeiras listas.
Retorna o cabeçalho da lista vinculada mesclada .

Exemplo 1:

Entrada: lista1 = [1,2,4], lista2 = [1,3,4]
 Saída: [1,1,2,3,4,4]
Exemplo 2:

Entrada: lista1 = [], lista2 = []
 Saída: []
Exemplo 3:

Entrada: lista1 = [], lista2 = [0]
 Saída: [0]
 
Restrições:

O número de nós em ambas as listas está no intervalo [0, 50].
-100 <= Node.val <= 100
Ambos list1e list2são classificados em ordem não decrescente .

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
       
        # Cria um nó fictício para facilitar a manipulação da lista resultante
        dummy = ListNode(0)
        current = dummy

        # Enquanto houver elementos em ambas as listas
        while list1 and list2:
            # Compara os valores dos nós atuais de ambas as listas
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move o ponteiro atual para o próximo nó
            current = current.next

        # Se ainda houver elementos em list1, adiciona-os à lista resultante
        if list1:
            current.next = list1
        # Se ainda houver elementos em list2, adiciona-os à lista resultante
        elif list2:
            current.next = list2
        
        # Retorna a lista resultante, ignorando o nó fictício
        return dummy.next

sol = Solution()
print(sol.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))  
print(sol.mergeTwoLists(None, None))  #
print(sol.mergeTwoLists(None, ListNode(0)))  