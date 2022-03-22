def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s_ = [c for c in ' '.join(''.join(s).split(' ')[::-1])]
        
        for i in range(len(s_)):
            s[i] = s_[i]
        
