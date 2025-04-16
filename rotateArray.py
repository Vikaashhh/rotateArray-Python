class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction
    def rotateArr(self, arr, d):
        n = len(arr)

        # Agar d array size se zyada hai to usko mod karke fix karo
        d = d % n

        # Step 1: pehle d elements ko cut karo
        left = arr[:d]         # Pehle d elements
        right = arr[d:]        # Bache hue elements

        # Step 2: right + left ko jod ke final rotated array banao
        for i in range(n):
            if i < n - d:
                arr[i] = right[i]
            else:
                arr[i] = left[i - (n - d)]

# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]  # Sample input
    d = 2                        # Rotate by 2 positions

    print("Original Array:", arr)

    sol = Solution()
    sol.rotateArr(arr, d)  # Rotate the array

    print("Rotated Array:", arr)
