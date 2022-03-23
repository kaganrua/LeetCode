def firstBadVersion(self, n: int) -> int:
        
        start = 1
        end = n
        
        while start <= end:
            mid = (start+end) // 2
            
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    end = mid - 1
                else:
                    return mid
            
            else:
                start = mid + 1
