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
新加的NewPiece.py单独列出来，包括了部分create child的function。
目前仍在写create child。 

Queue python source code:
https://github.com/python/cpython/blob/3.6/Lib/queue.py

New updates in bestFirstExa file, current goal is to get the path done, this can be done by using the given method,
although what kind of method still need to be studied, fuking desperate...., the algorithm is best first search. 
white piece can't jump during the path finding stage, it need to be settled or better be settled.

Update :
1 找到所有可以被消灭的黑棋子
2 根据priority sort black piece list。
3 正在写（
		如果黑棋子旁边有白棋子/黑棋子/Corner，优先考虑， weight设定为1
		按距离来算，附近最近的白棋子的距离最短者，先干
）
4 干完以后需要update board做好标记，并且update pqueue