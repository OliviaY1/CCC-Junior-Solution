## Thoughts
1. 先算出input的三个sections的长度：Larget section, Medium section, Small section
2. 将input中Large section中`non_Ls`移出来，将Medium Section中`non_Ms`移出来，再不算上`min(Ms in Large section, Ls in Medium section)`
3. 剩下的Small section就已经排好了

## Graphs
![](2021J4.jpg)

## Code
```python
books = input()
Ls, Ms, Ss = 0,0,0
for book in books: # get the length of each section
    if book == "L":
        Ls += 1
    elif book == 'S':
        Ss += 1
    else:
        Ms += 1
non_Ls, non_Ms, Ms_in_L, Ls_in_M = 0,0,0,0
for each in range(Ls): # calculate Ms in L and non_Ls
    if books[each] == 'M':
        Ms_in_L += 1
        non_Ls+=1
    if books[each] == 'S':
        non_Ls += 1
for each in range(Ls, Ls+Ms): # calculate Ls in M and non_Ms
    if books[each] == 'L':
        Ls_in_M += 1
        non_Ms += 1
    if books[each] == 'S':
        non_Ms += 1
print(non_Ls + non_Ms - min(Ms_in_L, Ls_in_M)) # the most important formula
```
