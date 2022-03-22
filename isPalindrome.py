def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        copy = ''
        for char in s:
            if char.isalnum():
                copy += char
       
        i = len(copy) - 1
        j = 0
        
        
        while i >= len(copy) // 2:
            if copy[i] != copy[j]:
                return False
            i -= 1
            j += 1
        
        return True
