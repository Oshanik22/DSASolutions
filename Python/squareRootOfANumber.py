def floorSqrt(n):
   low, high = 0, n
   result= 1
   while low <= high:
      mid = low + ((high-low))//2

      if mid*mid <= n:
         result = mid
         low = mid+1
      
      else:
         high = mid-1
   
   return result

      
n= int(input())
print(floorSqrt(n))