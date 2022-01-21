1. 非常注意backtracking，倒叙和正序的执行顺序。


|backtracking|forward|
|--|--|
|每次执行下一个recursion时，决定因素是curr的位置: `curr[0] * curr[1]`|每次执行下一个recursion时，决定因素是curr的value：`rooms[curr[0]-1][curr[1]-1]`|

2. 有必要找到**最短路径**时，使用bfs！绝不使用dfs


## Thought: Breadth First Search


## Two time-limit codes
### bfs 13/15
```python
rows = int(input())
columns = int(input())
rooms = []
for line in range(rows):
  rooms.append(list(map(int,input().split())))
def possibleChild(curr: int):
  # find the possible children of curr; record if the exit exists
  res = []
  found = False
  for row in range(1,rows+1):
    for column in range(1,columns+1):
      if row * column == curr:
        if row == rows and column == columns:
          found = True
        res.append(rooms[row-1][column-1])
  return (res, found)

def bfs(queue):
  visited = [queue[0]]
  while queue:
    curr = queue.pop(0)
    children, found = possibleChild(curr)
    for child in children:
      if found:
        return found
      if child not in visited:
        visited.append(child)
        queue.append(child)
  return found
if bfs([rooms[0][0]]):
  print('yes')
else:
  print('no')
```
#### backtracking
```python
rows = int(input())
columns = int(input())
rooms = []
for i in range(rows):
    rooms.append(list(map(int,input().split())))

def combos(curr: tuple):
    # return all the possible positions whose k(value) == curr(x)*curr(y)
    res = []
    summ = curr[0] * curr[1]
    for x in range(rows):
        if rooms[x].count(summ) >=1:
            for y in range (columns):
                if rooms[x][y] == summ:
                    res.append((x+1,y+1))
        else:
            continue
    return res # not python count

found = False
# 倒推
def find(curr, visited):
    global found
    #TODO: visited
    if found:
        return
    if curr in visited:
        return
    if curr[0]*curr[1] == columns*rows:
        #print(visited)
        found = True
    #print(curr, visited)
    all_combos = combos(curr)
    for each_combo in all_combos:
        find(each_combo, visited+[curr])
find((rows, columns), [])
if found:
    print('yes')
else:
    print('no')
```

#### forward
```python
rows = int(input())
columns = int(input())
rooms = []
for i in range(rows):
    rooms.append(list(map(int,input().split())))

def combos(k:int):
    # return all the possible combo that k(value) can jump to
    # x is less than rows, y is less than columns
    res = []
    for x in range(1, rows+1):
        if k%x == 0 and (k//x) <= columns:
            res.append((x, k//x))
    return res # not python count

found = False
# 正推
def find(curr, visited):
    global found
    if found:
        return
    if curr in visited:
        return
    if curr == (rows, columns):
        #print(visited)
        found = True
    all_combos = combos(rooms[curr[0]-1][curr[1]-1])
    for each_combo in all_combos:
        find(each_combo, visited+[curr])
find((1,1), [])
if found:
    print('yes')
else:
    print('no')
```

