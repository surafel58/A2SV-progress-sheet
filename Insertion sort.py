def insertionSort1(n, arr):
    # Write your code here
    last_element = arr[-1]
    i = len(arr) - 1
    
    while i > 0:
      
      if arr[i-1] > last_element:
        arr[i] = arr[i-1]
        for j in range(n):
            print(arr[j], end=" ")
        print()
        
      else: 
          arr[i] =  last_element
          for j in range(n):
            print(arr[j], end=" ")
          print()
          break
      
      i -= 1
      
    if i==0:
        arr[0] =  last_element
        for j in range(n):
            print(arr[j], end=" ")
        print() 
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
