
For part A, assume all Black pieces will be killable.


Right. However, please note that there is no accounting for board shinking while calculating Massacre.



About Running time:

Good question! We are still finalising the answer to this one, so I can't give you anything more concrete.

You shouldn't have to go beyond a sensible implementation of an appropriate uninformed search algorithm to pass all our tests.

For now, probably just start by trying to get a program that solves the 'Massacre' example board within a few seconds.


https://github.com/aimacode/aima-python  Aima Module


27/3 晚间update：
个人思路： naively thinking，一般来说每一个棋子有至少四种走法。 随机选取一个白棋子，开始走。 白棋子保存一个与黑棋子之间的distance， 取一个最小的距离（三个黑棋子取
最近的）（入Stack）搜索该白棋子的周围可走的地方，入Stack。走到不能再走时候，即完成。 可以加上对于此时与黑棋子的距离，dist。 每一步的dist
应该都变小，如果不是，不走这一步。 
对于黑棋子，如果已经被两个白棋子包围了，标记出来。下次traverse忽略掉。。


28/3 晚间update：
考虑使用greedy 贪婪最佳优先搜索
建立priority queue。
目前已经明白了如何建立child 。。找到了感觉。 
上传的code都会经过compile