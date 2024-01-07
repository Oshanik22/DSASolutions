from collections import deque
def printFirstNegativeInteger( A, N, K):
    result = []
    negatives = deque()
    i,j = 0, 0
    
    while j<len(A):
        if A[j] <0:
            negatives.append(A[j])
        if j-i+1 < K:
            j += 1
            continue
        
        if j-i+1 == K:
            if not negatives:
                result.append(0)
            else:
                result.append(negatives[0])
            
            if A[i] < 0:
                negatives.popleft()
            
            i += 1
            j +=1
    
    return result