# 2D list
### create a 2D list
`a = [[0 for a in range(5)] for i in range(5)]`
`a = [[] for i in range(5)]`  
### Find the minimum/maximum number in a 2D list
The list is called lst: `min([min(i) for i in lst])`
`min(list(map(min, lst)))`

### clockwise rotate a 2D list
`return zip(*data[::-1])`
data[::-1] : 旋转大lst
 *：拆分大lst
 
---
# set 
### basic function
`.add()` `.remove()` `.discard()` `set1 == set2`  `a = set()`  
add any iterable: **`a.update(lst)`**  
join two sets: `set3 = set1.union(set2)` `set1.update(set2)`  
find the common elements: `set1.intersection_update(set2)` `set3 = set1.intersection(set2)`  
find the different elements: `set1.symmetric_difference_update(set2)` `set3 = set1.symmetric_difference(set2)`  
contain elements that one has but the other does not: `set3 = set1.difference(set2)`

`a.isdisjoint(b)` if a contains any element of b  

### transfer list into set
`a = set([lst])` --> lst == [1,2,3] and a == {1,2,3}

# dictionary
`if a in dict` is to check whether the value a is in ==the keys of dict==
`dict[key]` returns the value
`dic.values()` `dic.keys()` is not subscriptable! It does not return a list; You have to use `keys = [i for i in dic.keys()]` or `for i in dic.values()`
# defining a function
- You can operate other defined function in a function
- You can edit absolute variables that are outside the function 

# str
- How to edit string without make a copy: ==slice== `a = a[1:] + a[:1]` instead of `a[1:] = 'abc'`
- slice: ends when the ending index is bigger than its length
    - `a[1:10]` -> 123 when a=='0123'

# list
- How to add a list without `append`: `lst + [elements]` return a combined list
- `lst.append()` return None, its orginial lst changes

---
# Data Structure: TREE (dictionary)
![Tree Structure](https://media.geeksforgeeks.org/wp-content/cdn-uploads/binary-tree-to-DLL.png)  
a hierarchical tree structure with a root value and subtrees of children with a parent node: a set of linked nodes
### Breadth First Search (用while循环)
```python
def BFS(lst, node, visted, queue):
  visted.append(node)
  queue.append(node)
  
  while queue: # 可以输入任何情况：find the shortest path
    # 每一次都pop掉第一个value，然后添加它的children
    r = queue.pop(0)
    
    for item in lst[r]:
      if item not in visited:
        visited.append(item)
        queue.append(item)
```
* 注意node和lst的index 的对应
* 可以用于find the shortest path

