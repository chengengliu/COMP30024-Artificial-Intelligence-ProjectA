
For part A, assume all Black pieces will be killable.


Right. However, please note that there is no accounting for board shinking while calculating Massacre.



About Running time:

Good question! We are still finalising the answer to this one, so I can't give you anything more concrete.

You shouldn't have to go beyond a sensible implementation of an appropriate uninformed search algorithm to pass all our tests.

For now, probably just start by trying to get a program that solves the 'Massacre' example board within a few seconds.


https://github.com/aimacode/aima-python  Aima Module

目前思路是将棋子列为一个class， MainClass 读入input时候建立这个棋子的obj。 
input读入完成以后得到一个含有棋子的list。 传入这个list进屠杀class， 进行search。