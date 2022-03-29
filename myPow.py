ef myPow(self, x: float, n: int) -> float:
        
        table = {}
        table[0] = 1
        table[1] = x
        if x == 0:
            return 0
        table[-1] = 1 / x
        
        #print(-13//2)
        def mypow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n in table:
                return table[n]
            else:
                if n > 0:
                    rem = n // 2
                    a = mypow(x,rem) * mypow(x,n-rem)
                    table[n] = a
                    return a
                else:
                    n = -1 * n
                    rem = n //2
                    a = 1/mypow(x,rem) * 1/mypow(x,n-rem)
                    table[-n] = a
                    return a
        
        return mypow(x,n)
