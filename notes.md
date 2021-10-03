## 2D list
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

## set 
### basic function
`.add()` `.remove()` `set1 == set2`  `a = set()`  
add any iterable: **`a.update(lst)`**  

### transfer list into set
`a = set([lst])` --> lst == [1,2,3] and a == {1,2,3}

## Data Structure: TREE


## return 
`lst.append()`在原lst上修改，return NoneType
string的method都是make a copy

