class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1

        for i in range(len(arr) - 1, -1, -1):

            current = arr[i]
            arr[i] = greatest
            greatest = max(greatest, current)
        
        return arr

            
                        
                        
                            
            