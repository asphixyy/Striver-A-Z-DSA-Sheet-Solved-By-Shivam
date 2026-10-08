# Characters from Paired Strings

Given **N** (N is even) strings of equal length. Make a string by concatenating the **first character of the first string** and the **last character of the last string**. Make another string by concatenating the **first two characters of the second string** and the **last two characters of the second-last string**. And so on.

Print the strings so formed in the same line, separated by a space. **Use string slicing.**

You can assume that the length of any string is **> N/2**.

## Input Format

- First line contains the value of **N**.
- The next line contains **N space-separated strings**.
- None of the strings contain spaces.

## Output Format

Print **N/2 space-separated strings**.

## Sample Input

6
alpha kumar polio virus hello gamma

## Sample Output

aa kulo polrus

## Explanation

The strings are paired from the outside towards the center:

- `alpha` → `a`
- `gamma` → `a`
- Result → `aa`

- `kumar` → `ku`
- `hello` → `lo`
- Result → `kulo`

- `polio` → `pol`
- `virus` → `rus`
- Result → `polrus`

Therefore, the output is:

aa kulo polrus
