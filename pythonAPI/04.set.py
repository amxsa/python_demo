#coding:utf-8
#set无序，不重复
#set里面不能放入list
set1=set([1,2,3])
#输出为{1,2,3}
print(set1)
set2=set([2,2,3,4])
set1.add(4)
set1.remove(4)
#set的交集
print(set1&set2)
#set的并集
print(set1|set2)
# list去重
list1 = [2, 4, 3, 4, 5]
print(list(set(list1)))