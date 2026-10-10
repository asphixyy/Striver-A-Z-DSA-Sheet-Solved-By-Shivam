## Bomb the Base


### Problem Statement

There are \(N\) houses numbered from \(1\) to \(N\).

The \(i\)-th house has a defense strength \(A_i\).

A bomb with attack strength \(X\) can destroy a house only if:

\[
A_i < X
\]

When a house at position \(i\) is destroyed, all houses with indices from \(1\) to \(i\) are also destroyed, regardless of their defense strengths.

Determine the **maximum number of houses** that can be destroyed using the bomb.

### Input Format

- The first line contains two space-separated integers \(N\) and \(X\).
- The second line contains \(N\) space-separated integers representing the defense strengths of the houses.

### Output Format

Print a single integer representing the maximum number of houses that can be destroyed.

### Constraints

- \(1 \le N \le 10^5\)

### Example 1

**Input**
```text
5 4
2 5 1 3 6
```

**Output**
```text
4
```

**Explanation**

The fourth house has defense strength \(3\), which is less than \(X = 4\). Destroying the fourth house also destroys all houses before it. Therefore, the maximum number of houses destroyed is \(4\).

### Approach

1. Iterate through the array of defense strengths.
2. Whenever \(A_i < X\), update the answer to \(i+1\) using zero-based indexing.
3. Return the final answer.

### Complexity Analysis

- **Time Complexity:** \(O(N)\)
- **Space Complexity:** \(O(1)\) auxiliary space
