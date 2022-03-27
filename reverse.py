def reverse(self, x: int) -> int:
        if x < -2147483648 or x > 2147483647:
            return 0
        
        
        if x < 0:
            s = str(x)
            s = s[1:]
            s = s[::-1]
            sol =  -1 * int(s)
            if sol < -2147483648 or sol > 2147483647:
                return 0
            return sol
        else:
            s = str(x)
            s = s[::-1]
            
            sol = int(s)
            if sol < -2147483648 or sol > 2147483647:
                return 0
            return sol
