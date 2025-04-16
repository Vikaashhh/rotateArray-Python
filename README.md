# 🔄 Day-4 DSA Challenge – Rotate Array by D Elements

This repository contains the solution for rotating an array by **D elements in a counter-clockwise direction**. The implementation leverages Python slicing and index manipulation for clarity and performance.

---

## 🧠 Problem Statement

Given an array `arr[]` of size `n` and an integer `d`, rotate the array **counter-clockwise by d elements**.

### ✅ Example:

**Input:**
arr = [1, 2, 3, 4, 5, 6, 7] d = 2

**Output:**
[3, 4, 5, 6, 7, 1, 2]

---

## 🔍 Approach

### ✔ Step-by-step Explanation:

1. **Edge Handling:** If `d > n`, reduce it using `d = d % n`.
2. **Array Split:**
   - First part: `arr[0:d]`
   - Second part: `arr[d:]`
3. **Merge:** Rebuild the array by concatenating second part + first part.
This solution ensures **O(n) time complexity** and uses **O(1) extra space** with in-place updates.

---

## 🏁 Output
Original Array: [1, 2, 3, 4, 5, 6, 7]

Rotated Array:  [3, 4, 5, 6, 7, 1, 2]

## 🚀 How to Run
1. Clone the repository: 
git clone https://github.com/your-username/day4-rotate-array.git

cd day4-rotate-array

2. Execute the Python file: 
python rotateArray.py

## 📌 Tags
#python #dsa #array #rotate-array #twopointer #codingchallenge #dailyDSA #beginnerfriendly #leetcode

## 🙌 Author
Vikash Joshi

Front-End Developer | UI/UX Enthusiast | DSA Explorer

• LinkedIn:- https://www.linkedin.com/in/itaintvi/

---
## 🌱 Let’s Connect
If you found this helpful, feel free to ⭐ the repo and share your thoughts. Let’s build and grow in public together! 🚀
