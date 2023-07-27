class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort(reverse=True)
        
        if arr[-1] != 1:
            arr[-1] = 1

        for i in range(len(arr) - 2, 0, -1):
            if abs(arr[i] - arr[i + 1]) > 1:
                arr[i] = arr[i + 1] + 1

        return arr[0]
