# Time Complexity: O(n * n) where n is the length of the array.
# Space Complexity: O(n) where n is the length of the array.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            arr = []        # For storing lists of rows.
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    arr.append(result[i - 1][j - 1] + result[i - 1][j])     # From previous row
            result.append(arr)
        return result