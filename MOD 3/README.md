# Mod 3

## Problem Statement

Count integers in a given range, defined by two values, `start` and `end` (both inclusive), which are divisible by 3 and the sum of their digits is even.

## Input Format

Two lines of input:
- The first line contains the value of `start`.
- The second line contains the value of `end`.

## Output Format

Print an integer representing the count of numbers that satisfy both conditions.

## Constraints

`1 <= start <= end <= 100`

## Sample Input

```text
3
10
```

## Sample Output

```text
1
```

## Explanation

The range is `[3, 10]`. The numbers in the range are `3, 4, 5, 6, 7, 8, 9, 10`.

Out of these, only `3, 6, 9` are divisible by 3. Among them, only `6` has an even sum of digits.

Therefore, the answer is `1`.
