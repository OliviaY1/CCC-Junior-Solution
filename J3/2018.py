# Olivia Yan
# 第N行的第N的数字是0，它之后的数字= 前面的数字+input对应的数字； 它之前的数字 = 后面的数字+input对应的数字
# 先创建2D matrix；再用两个for loop使前后相加减

# store input as a list of num
inp = list(map(int, input().split()))

# create a 2D matrix [[], [], [], []]
matrix = [[0 for a in range(5)] for i in range(5)]

for line in range(5):
  for each in range(line+1, 5): # 从第N行的第N个数字往后算
    matrix[line][each] = matrix[line][each-1] + inp[each-1]
   
  for each in range(line-1, -1, -1): # 从第N行的第N个数字往前算
    matrix[line][each] = matrix[line][each+1] + inp[each]

# use function " ".join(lst/dic/tuple of string)
for i in range(5):
  print(" ".join(list(map(str, matrix[i]))))
