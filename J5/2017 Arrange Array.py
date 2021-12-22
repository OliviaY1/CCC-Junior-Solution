input()
woods = list(map(int, input().split()))

# create a wood_dic: keys is the length of each wood, values is the numbers
wood_dic = {}
for wood in woods:
  if wood not in wood_dic:
    wood_dic[wood] = 1
  else:
    wood_dic[wood] += 1

# create a sum_dic: keys is the sum of two woods (can be the same length); values is the occurance / the fence length
wood_length = wood_dic.keys()
for up in range (len(wood_length)): # should the last one be included?
  if wood_dic[wood_length[up]] >1:
    start = up # include up itself
  else:
    start = up+1 # not include it
  for down in range(start, len(wood_length)):
    summ = wood_length[up] + wood_length[down]
    
    if up == down:
      if summ not in sum_dic:
        sum_dic[summ] = wood_dic[keys[first]] //2
      else:
        sum_dic[summ] +=  wood_dic[keys[first]] //2
      
    else: # two woods are not the same length
      if summ not in sum_dic:
        sum_dic[summ] = min(wood_dic[keys[first]], wood_dic[keys[second]])
      else:
        sum_dic[summ] += min(wood_dic[keys[first]], wood_dic[keys[second]])
        
# in sum_dic, find the maximum values. If there are more than one max values, store the occurance of different keys
fence_lengths = sum_dic.values()
max_length, heights = 0, 0
for fence_length in fence_lengths:
  if fence_length > max_length:
    max_length = fence_length
    heights = 1
  elif fence_length == max_length:
    heights += 1
print(max_length, heights)

      
