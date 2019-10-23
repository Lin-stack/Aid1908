'''
regex2.py  match对象属性演示
'''
import re

pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)
obj = regex.search('abcdefghi',0,7) #match对象

#属性变量
# print(obj.pos) #目标字符串的开始索引位置
# print(obj.endpos) #目标字符串的结束索引位 +1
# print(obj.re) # 正则
# print(obj.string) #目标字符串
# print(obj.lastgroup) #最后一组组名
# print(obj.lastindex) #最后一组序列


#属性方法
print(obj.span()) #匹配到的内容在目标字符串中的起止位置
print(obj.start())
print(obj.end())
print(obj.groupdict()) #获取捕获组的字典{组名：子组对应内容}
print(obj.groups()) #所有子组内容元组
print(obj.group()) #获取match对象内容
print(obj.group(1)) #组序号或组名称
print(obj.group('pig'))