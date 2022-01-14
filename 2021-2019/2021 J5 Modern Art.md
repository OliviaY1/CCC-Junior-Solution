## Thought
1. 根据M和N，建立一个全是Black的canvas
2. 创建两个functions，一个paint a row，一个paint a column
3. 根据每一行的command，使用paint a row/column的function
4. 执行完全部commands后，数多少cells是Golden

### 改进
有重复command的题目，我们必须注意commands之间可否**互相抵消**，省时。
1. 当同一个command出现4次时，canvas before和after并没有影响。当同一个command出现21次，我们只需要执行一次command  
这题，我们用dictionary先存下所有commands。`key: commands; value: numbers of occurrance`

2. canvas中只有Black和Golden互相切换，我们可以用`True / False`来表示


## Code
**注意赋值和相等的等于号使用，写完后检查**
```python
rows = int(input())
columns = int(input())
canvas = [['B' for i in range(columns)]for y in range(rows)]
def print_row(index, canvas):
    # return printed canvas
    for each in range(len(canvas[index-1])):
        if canvas[index-1][each] == 'B':
            canvas[index-1][each] = 'G'
        else:
            canvas[index-1][each] = 'B'
    return canvas
    
def print_column(index, canvas):
    # return printed canvas
    for row in range(len(canvas)):
        if canvas[row][index-1] == 'B':
            canvas[row][index-1] = 'G'
        else:
            canvas[row][index-1] = 'B'
    return canvas  

# use a dictionary to store the commands, key: command, value: commands times
lines = int(input())
commands = {}
for i in range (lines):
    line = input()
    if line in commands:
        commands[line]+=1
        continue
    commands[line] = 1

for command in commands.keys():
    if commands[command] % 2 == 0:
        continue
    else: # odd number
        if command[0] == 'R':
            canvas = print_row(int(command[2:]),canvas)
        elif command[0] == 'C':
            canvas = print_column(int(command[2:]), canvas)   
gold = 0
for row in canvas:
    gold += row.count('G')
print(gold)
```

