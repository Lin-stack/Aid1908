'''
 编写一个函数，传入一个端口名称，返回这个端口运行情况中所描述的
 address地址信息
 （每段之间有空行每段首单词是端口名，端口名可能很复杂）
'''

import re



def find_address(port):
    '''

    :param port:端口名称
    :return: 端口对应的address
    '''
    file = open('exc.txt')
    while True:
        data = ''
        for i in file:
            if i == '\n':
                break
            data+=i
        if not data:
            return '没有该段落'
        obj = re.match(r'\S+',data) #使用正则匹配首个单词
        if port == obj.group():
            pattern = r'\w{4}\.\w{4}\.\w{4}'
            pattern1 = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown'
            obj = re.search(pattern,data)
            obj1 = re.search(pattern1,data)
            if obj:
                return obj.group(),obj1.group()

if __name__ == '__main__':
     port = input('输入查询的端口名称：')
     print(find_address(port))
