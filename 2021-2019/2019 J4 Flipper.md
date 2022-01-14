## Thought
可能性只有四个：
1. 不变
2. horizontal flip
3. vertical flip
4. horizontal + vertical flip

这种题目必须抵消掉不必要的重复flip步骤。
## Code
```python
numbers = ["1","2","3","4"]
commands = input()
Hs = commands.count('H')
Vs = commands.count('V')
if Hs % 2 == 1:
    numbers = numbers[2:] + numbers[:2]
    #print(numbers)
if Vs % 2 == 1:
    numbers = numbers[1:2]+numbers[0:1]+numbers[3:]+numbers[2:3]
    #print(numbers)
print(numbers[0],numbers[1])
print(numbers[2],numbers[3])
```
