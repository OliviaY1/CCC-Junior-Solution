# store three rules; store each index
rule = {}
for i in range(3):
  a = input().split() # return a list
  rule[a[0]] = (a[1], i+1) # {'AA': ('AB', 1), ...}
expected_step, initial, final = input.split()
# go through every character; check whether they can be substituted
def convert(expected_step, path, initial, final) -> list:
  if len(path) == expected_step and initial == final:
    return path
  else:
    if len(path) > expected_step:
      return
    for i in range(len(initial)):
      for j in range(i+1, len(initial)+1): # since slice will neglect the last element and we want the last one, so +1
        if initial[i:j] in rule: # slice rule: no matter how big the ending index is
          sub = rule[initial[i:j]] # is a tuple: (str, rule_index)
          copy = initial[:i] + sub[0] + initial[j:]
          
          copy_path = path
          copy_path.append(' '.join([str(sub[1]), i+1, copy]))
          # if can: go deeper to the next layer
          convert(expected_step, copy_path, copy, final)
          
res = convert(expected_step, [], initial, final)
print(res)

# if can: continue in this layer to see is there any other character can be substituted

# return the path if it fits the required steps

