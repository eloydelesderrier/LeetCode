"""
Dada a estrutura headde uma lista encadeada, remova o nó do final da lista e retorne sua cabeça.nth

Exemplo 1:

Entrada: cabeça = [1,2,3,4,5], n = 2
 Saída: [1,2,3,5]
Exemplo 2:

Entrada: cabeça = [1], n = 1
 Saída: []
Exemplo 3:

Entrada: cabeça = [1,2], n = 1
 Saída: [1]
 

Restrições:

O número de nós na lista é sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Cria um nó fictício que aponta para a cabeça da lista
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move o primeiro ponteiro n + 1 passos à frente
        for i in range(n+1):
            first = first.next

        # Move o primeiro ponteiro até o final da lista, mantendo a distância de n nós entre os ponteiros
        while first:
            first = first.next
            second = second.next

        # Remove o n-ésimo nó do final da lista
        second.next = second.next.next
        return dummy.next
    

sol = Solution()
print(sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)) # [1,2,3,5]
print(sol.removeNthFromEnd(ListNode(1), 1)) # []
        