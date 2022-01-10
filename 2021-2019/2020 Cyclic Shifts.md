## Thought
1. 找到T中的`S[0]`的所有位置`i`，以此位置为可能性，判断是否是rotated S
2. 从T[i:]向后找，它所对应的S部分，也就是找到S的可能pivot点`k`; T[i:i+k] == S[:k]
3. 再从T[i]向前确认，T[i-(len(S)-k)] == S[k:]

### 要点
**从T[i:]向后找的时候，有几种情况需要考虑：**
1. i == len(T)-1，则pivot点k是1
2. T[i:k] == S, 则pivot点是len(S)，直接return True麻烦

从T[i]向前确认时，需要考虑i前够不够位置：
1. `if T[i-(len(s)-k)] < 0: return False`

## Code
```python
T = input()
S = input()
found = False

initials = []
for each in range(len(T)):
    if T[each] == S[0]:
        initials.append(each)

def check_after(index):
    nex = 1 # index's corresponding index in S
    if index == len(T)-1:
        return 1
    index +=1
    while T[index] == S[nex]:
        index +=1
        nex +=1
        if index == len(T):
            return nex
        if nex == len(S):
            return nex
    return nex # return the pivotal number (included) of S

for initial in initials:
    S_pivot = check_after(initial)
    if initial - (len(S)- S_pivot) < 0:
        continue
    if T[initial-(len(S)-S_pivot):initial] == S[S_pivot:]:
        found = True
        break
if found:
    print('yes')
else:
    print('no')
```
