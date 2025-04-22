class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Números negativos não são palíndromos 
        if x < 0:
            return False
        
        # Converte o número em uma string
        str_x = str(x)

        # Compara o inicio é o fim
        return str_x == str_x[::-1]
    
sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))