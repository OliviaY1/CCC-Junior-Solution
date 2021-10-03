# Oct 2

# 题目：一定会有end page; the first number is the number of paths
# 思路：通过set查看是否所有的page都出现过，return 第一个output('Y'or 'N')
# 通过recursion查看最短的路，return第二个output(num)

# 要点：书页码从1开始到并包括于len(book); findPath()中的page比book中对应的index多出1

line = int(input())
book = [[] for i in range(line)]
real_pages = set()
for a in range(line):
  book[a]= list(map(int, input().split()))
  real_pages.update(book[a][1:]) # the first num is not page num
  
# ------------------output1------------------
expected_pages = {i for i in range(2,line+1)} # start from 1 to and include len(book)
# avoid the situation when page1 can be directed to
if 1 in real_pages:
  expected_pages.add(1)
if expected_pages == real_pages:
  print('Y')
else:
  print('N')

# ------------------output2------------------
def findPath(book, page, step, visited):
  # go through all the possibilities and then return the smallest step
  if book[page-1][0] == 0:
    return step
  else:
    visited.append(page)
    mini = 10000
    for i in book[page-1][1:]:
      if i not in visited:
        res = findPath(book, i, step+1, visited)
        if res < mini:
          mini = res
    return mini

# body
res = findPath(book,1,1,[])
print(res)



    
