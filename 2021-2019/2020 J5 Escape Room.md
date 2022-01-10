1. 非常注意backtracking，倒叙和正序的执行顺序。
|backtracking|forward|
|--|--|
|每次执行下一个recursion时，决定因素是curr的位置: `curr[0] * curr[1]`|每次执行下一个recursion时，决定因素是curr的value：`rooms[curr[0]-1][curr[1]-1]`|

## Thought
