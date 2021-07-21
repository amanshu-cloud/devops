#orderedDict
#counter 
#linkedlist
#deque = double ended queue
#orderedDict can be used as a stck

a = list(map(int,input().split()))

def binsearch(a,left,right,k):
    if left <= right:
        mid = (left + right)//2
        if a[mid]==k:
            return mid
        elif a[mid] > k:
            return binsearch(a,left,mid-1,k)
        elif a[mid] < k:
            return binsearch(a,mid+1,right,k)
        
        else:
            return None
        
print(binsearch(a,0,len(a),3))