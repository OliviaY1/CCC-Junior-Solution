- [ ] 2019 grader中7/15，test 9 wrong answer, test 11 time limit, 找出原因

## THought
1. 学会`'str'.count(substring, start, end)` `'str'.find(substring, start, end)` end的数字不包括
2. 通过count 和find

注意：
1. 同一个rule在一个string中可能有大于一的替换方式
    `'strings'`中有两个s
2. 这题用dfs，但是不用建visited，因为会有重复的step。

## Code
```python
rules = {} # {rule1:[rule_num, rule_res], rule2:[...,...]}
for i in range(3):
    line = input().split()
    rules[line[0]] = [i+1, line[1]]
req_steps, initial, final = input().split()
req_steps = int(req_steps)
found = False

def sub(curr,rule): # return a list of tuples (res_str, starting point)
    start = 0
    starts = [] # store all the possible substition index
    res = [] # store all the possible substituted string
    while curr.count(rule,start) > 0: 
        pos = curr.find(rule, start, len(curr))
        starts.append(pos)
        start = pos+1
    for each_start in starts:
        curr1 = curr[:each_start]+rules[rule][1]+curr[each_start+len(rule):]
        res.append((curr1, each_start))
    return res    

def change(curr:str,  path:list): # path:[[1,5,abc],[rule_num, starting point, after_string]]
    global found
    if found:
        return
    if len(path)>= req_steps and curr != final:
        return
    if len(path) == req_steps and curr == final:
        for line in path:
            print(line[0],line[1],line[2])
        found = True
        return
    #print(curr, visited, path)
    for each in rules.keys():
        if curr.count(each)>0:
            # find start point and substitute
            # return a list
            combos = sub(curr, each) 
            for combo in combos:
                change(combo[0],path+[[rules[each][0], combo[1]+1,combo[0]]])
change(initial, [])
# return line: which rule; start point; current result

```
