# Sep 25
# Olivia Yan

# 题目：一个N*N的矩形列可能正时钟、逆时钟旋转了90、180度
# 要点：此条件下，最小的数字永远在左上角，最大的数字永远在矩形右下角

n = int(input())
data = []
for i in range (n):
  data.append(list(map(int, input().split())))

# clockwise rotate function
def rotate(data):
  # 倒着从data中每个list的第N个数字拿出，组成第N个list
  line = len(data)
  res = [[]for i in range(line)]
  
  for i in range(line):
    for a in range (line-1,-1,-1):
      res[i].append(data[a][i])
  return res

# 检查是否左上角是最小的数字
def check_accurate(data,mini):
  if data[0][0] == mini:
    return True
  return False

# body
mini = min(data[0][0], data[0][-1], data[-1][0], data[-1][-1])
while not check_accurate(data, mini):
  data = rotate(data)

# output
for i in range(len(data)):
  print(" ".join(list(map(str, data[i]))))
