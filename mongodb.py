# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:26:39 2020

@author: liu_linshan
"""
from pymongo import MongoClient
client = MongoClient(host,port)
collection = client[db名][集合名]
#添加一条数据
ret = collection.insert_one({“name”:“test10010”,“age”:33})
print(ret)
#添加多条数据
item_list = [{“name”:“test1000{}”.format(i)} for i in range(10)]
insert_many#接收一个列表，列表中为所有需要插入的字典
t = collection.insert_many(item_list)
#查找一条数据
find_one查找并且返回一个结果,接收一个字典形式的条件
t = collection.find_one({“name”:“test10005”})
print(t)
查找全部数据
结果是一个Cursor游标对象，是一个可迭代对象，可以类似读文件的指针，但是只能够进行一次读取
find返回所有满足条件的结果，如果条件为空，则返回数据库的所有
t = collection.find({“name”:“test10005”})
#结果是一个Cursor游标对象，是一个可迭代对象，可以类似读文件的指针，
for i in t:
print(i)
for i in t: #此时t中没有内容
print(i)
更新一条数据 注意使用$set命令
update_one更新一条数据
collection.update_one({“name”:“test10005”},{"$set":{“name”:“new_test10005”}})
更行全部数据
update_one更新全部数据
collection.update_many({“name”:“test10005”},{"$set":{“name”:“new_test10005”}})
删除一条数据
delete_one删除一条数据
collection.delete_one({“name”:“test10010”})
删除全部数据
delete_may删除所有满足条件的数据

collection.delete_many({“name”:“test10010”})
