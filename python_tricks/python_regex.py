# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-13 10:22:18
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-13 11:52:55

import re
def match(string):
    ''' match
    match 方法用于查找字符串的头部（也可以指定起始位置），它是一次匹配，
    只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果。它的一般使用形式如下：
        match(string[, pos[, endpos]])
    其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，
    指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。
    因此，当你不指定 pos 和 endpos 时，match 方法默认匹配字符串的头部。
    当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
    '''
    pattern = re.compile(r'\d+')
    m = pattern.match(string)
    print m
    n = pattern.match(string,3,10)
    '''
    group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，
            可直接使用 group() 或 group(0)；
    start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），
            参数默认值为 0；
    end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1）
，           参数默认值为 0；
    span([group]) 方法返回 (start(group), end(group))。

    '''

    print n
    print n.group(0)
    print n.start(0)
    print n.end(0)
    print n.span(0)

    p = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
    b = p.match('Hello World Wide Web')
    print b  # 匹配成功，返回一个 Match 对象
    print b.group(0) # 返回匹配成功的整个子串
    print b.span(0)  # 返回匹配成功的整个子串的索引
    print b.group(1)  # 返回第一个分组匹配成功的子串
    print b.span(1)  # 返回第一个分组匹配成功的子串的索引
    print b.span(2) # 返回第二个分组匹配成功的子串
    print b.groups()[0]  # 等价于 (m.group(1), m.group(2), ...)

def search(string):
    '''[search]
    search 方法用于查找字符串的任何位置，它也是一次匹配，
    只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，它的一般使用形式如下：

    [search(string[, pos[, endpos]])]

    其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，
    指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。

    当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
    '''

    p = re.compile('\d+')
    m = p.search(string)  # 这里如果使用 match 方法则不匹配
    print m
    print m.group()
    n = p.search(string,10,30) # 指定字符串区间
    print n
    print n.group()
    print n.span()


def findall(string):
    '''[findall]

    上面的 match 和 search 方法都是一次匹配，
    只要找到了一个匹配的结果就返回。然而，在大多数时候，我们需要搜索整个字符串，
    获得所有匹配的结果。

    findall 方法的使用形式如下：

    findall(string[, pos[, endpos]])

    其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，
    指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。

    findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表。

    Arguments:
        string {[type]} -- [description]
    '''

    p = re.compile(r'\d+')  # 查找数字

    '''
    https://stackoverflow.com/questions/4780088/what-does-preceding-a-string-literal-with-r-mean

    The r means that the string is to be treated as a raw string, which
    means all escape codes will be ignored.

    For an example:

        '\n' will be treated as a newline character,
        while r'\n' will be treated as the characters \ followed by n.

    When an 'r' or 'R' prefix is present, a character following a backslash is
    included in the string without change, and all backslashes are left in the
    string. For example, the string literal r"\n" consists of two characters:
    a backslash and a lowercase 'n'. String quotes can be escaped with a backslash,
     but the backslash remains in the string; for example, r"\"" is a valid string
      literal consisting of two characters: a backslash and a double quote;
      r"\" is not a valid string literal (even a raw string cannot end in an odd
       number of backslashes). Specifically, a raw string cannot end in a single
        backslash (since the backslash would escape the following quote character).
         Note also that a single backslash followed by a newline is interpreted
         as those two characters as part of the string, not as a line continuation.


    It means that escapes won’t be translated. For example:
        r'\n'

    is a string with a backslash followed by the letter n. (Without the r it would be a newline.)

    b does stand for byte-string and is used in Python 3, where strings are
    Unicode by default. In Python 2.x strings were byte-strings by default
    and you’d use u to indicate Unicode.
    '''
    ret1 = p.findall('hello 123456 789')
    ret2 = p.findall(string,0,10)
    print ret1,ret2

def finditer(string):
    '''[finditer]

    [finditer 方法的行为跟 findall 的行为类似，也是搜索整个字符串，
    获得所有匹配的结果。但它返回一个顺序访问每一个匹配结果（Match 对象）的迭代器。]

    Arguments:
        string {[type]} -- [description]
    '''
    p = re.compile('\d+')
    ret1 = p.finditer('hello 123456 789')
    ret2 = p.finditer(string,0,10)

    print type(ret1),type(ret2)
    for m1 in ret1:
         print 'matching string: {}, position: {}'.format(m1.group(), m1.span())

    print 'result2...'
    for m2 in ret2:
        print 'matching string: {}, position: {}'.format(m2.group(), m2.span())


def split(string):
    '''

    split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：

    split(string[, maxsplit])

    其中，maxsplit 用于指定最大分割次数，不指定将全部分割。

    Arguments:
        string {[type]} -- [description]
    '''
    p = re.compile(r'[\s\,\;]+')
    print p.split('a,b;;c  d')

def func(m):
    return 'hi' + ' ' + m.group(2)
def sub(string):

    '''sub 方法用于替换。它的使用形式如下：
        sub(repl, string[, count])
    其中，repl 可以是字符串也可以是一个函数：

        如果 repl 是字符串，则会使用 repl 去替换字符串每一个匹配的子串，并返回替换后的字符串
        ，另外，repl 还可以使用 id 的形式来引用分组，但不能使用编号 0；

        如果 repl 是函数，这个方法应当只接受一个参数（Match 对象），并返回一个字符串用于替换
        （返回的字符串中不能再引用分组）。

        count 用于指定最多替换次数，不指定时全部替换。

    '''

    p = re.compile(r'(\w+) (\w+)')
    s = 'hello 123, hello 456'
    print p.sub(r'hello world',s) # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
    print p.sub(r'\2 \1',s)   # 引用分组
    print p.sub(func,s)
    print p.sub(func,s,1)   # 最多替换一次

if __name__ == '__main__':
    string = 'one12twothree34four'
    match(string)
    search(string)
    findall(string)
    finditer(string)
    split(string)
    sub(string)
