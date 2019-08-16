<details><summary>Question</summary>
<p>
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
</p>
</details>

[Question Link](https://www.hackerrank.com/challenges/word-order "https://www.hackerrank.com/challenges/word-order")

```python
from collections import OrderedDict

n = int(input())
word_dict = OrderedDict()
word_list = []

for _ in range(n):
    word = input()
    word_dict[word] = 0
    word_list.append(word)

for word in word_list:
    word_dict[word] += 1
dist = 0
for key, value in word_dict.items():
    if word_dict[key]:
        dist += 1
print(dist)
for key, value in word_dict.items():
    print(word_dict[key], end=' ')
```
