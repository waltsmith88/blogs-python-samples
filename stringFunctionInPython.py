#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-12

## replaxce()函数
print('=*'*10, 'replace()函数', '=*'*10)
str = 'hello world hello waltsmith'
str1 = 'hello'
str2 = 'HELLO'
# 将所有的str1替换为str2
print( str1.replace(str1, str2) )
# 只将前1个str1替换为str2
print( str1.replace(str1, str2, 1) )

## split()函数
print('=*'*10, 'split()函数', '=*'*10)
str3 = 'I am a good boy!'
# 以空格分割字符串，分界符默认为空格
print(str3.split(' ', 3))
# 以字母o作为分界符，指定最大分割为2,将返回最大分割+1个元素的列表
print(str3.split('o', 2))

## capitalize()函数
print('=*'*10, 'capitalize()函数', '=*'*10)
str4 = 'I aM waLt smith'
# 字符串的首字母大写，其余字母全部小写
print(str4.capitalize())

## title()函数
print('=*'*10, 'title()函数', '=*'*10)
# 正常字符串的转换
str5 = "I am walt smith!"
print(str5.title())
# 字符中包含标点符号
str6 = "I'm walt-sMith!"
print(str6.title())

## 修正title()
print('=*'*10, 're修正title()函数', '=*'*10)
import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                             mo.group(0)[1:].lower(), s)
str7 = "I'm walt's friend!"
print(titlecase(str7))


## startswith()函数
print('=*'*10, 'startswith()函数', '=*'*10)
str8 = "Hello Walt Smith"
print(str8.startswith("Hello"))

## endswith()函数
print('=*'*10, 'endswith()函数', '=*'*10)
str9 = "Hello Walt Smith"
print(str9.endswith("Smith"))

## lower()函数
print('=*'*10, 'lower()函数', '=*'*10)
str10 = "Hello Walt Smith"
print(str10.lower())

## upper()函数
print('=*'*10, 'upper()函数', '=*'*10)
str10 = "Hello Walt Smith"
print(str10.upper())

## ljust()函数
print('=*'*10, 'ljust()函数', '=*'*10)
str10 = "Hello Walt Smith"
print("str10的原长度为%d" % (len(str10)))
print(str10.ljust(20))
print("str10处理后的长度为%d" % (len(str10.ljust(20))))

## rjust()函数
print('=*'*10, 'rjust()函数', '=*'*10)
str11 = "Hello Walt Smith"
print(str11.rjust(20))
print("str10的原长度为%d" % (len(str11)))
print("str11处理后的长度为%d" % (len(str11.ljust(20))))

## center()函数
print('=*'*10, 'center()函数', '=*'*10)
str12 = "Hello Walt Smith"
print(str12.center(20))
print("st12的原长度为%d" % (len(str12)))
print("str12处理后的长度为%d" % (len(str12.center(20))))

## lstrip()函数
print('=*'*10, 'lstrip()函数', '=*'*10)
str13 = "   Hello Walt Smith   "
print(str13.lstrip())

## rstrip()函数
print('=*'*10, 'rstrip()函数', '=*'*10)
str13 = "   Hello Walt Smith   "
print(str13.rstrip())

## strip()函数
print('=*'*10, 'rstrip()函数', '=*'*10)
str13 = "   Hello Walt Smith   "
print(str13.strip())
# strip()函数巧用
str131 = "var win({'a':'bc'});"
print(str131.strip('var win();'))

## partition()函数
print('=*'*10, 'partition()函数', '=*'*10)
str14 = "Are you believe in yourself?"
# "yourself"在字符串中
print(str14.partition("yourself"))
# "you"在字符串中有两个
print(str14.partition("you"))
# "walt"不在字符串中
print(str14.partition("walt"))

## join()函数
print('=*'*10, 'join()函数', '=*'*10)
str15 = "walt"
print(str15.join("ABC"))
iterable = ['YOU', 'THEY', 'WE']
print(str15.join(iterable))

## isspace()函数
print('=*'*10, 'isspace()函数', '=*'*10)
str16 = " t "
print(str16.isspace())

## isdigit()函数
print('=*'*10, 'isdigit()函数', '=*'*10)
str16 = "14250"
print(str16.isdigit())

## isalpha()函数
print('=*'*10, 'isalpha()函数', '=*'*10)
str17 = "HardWorking"
print(str17.isalpha())

## find()函数
print('=*'*10, 'find()函数', '=*'*10)
str = 'hello world'
# 'wo'在字符串中
print( str.find('wo') )
# 'wc'不在字符串中
print( str.find('wc') )

## index()函数
print('=*'*10, 'index()函数', '=*'*10)
str = 'hello world'
# 'wo'在字符串中
print( str.index('wo') )
# 'wc'不在字符串中,程序报错ValueError: substring not found
# print( str.index('wc') )

## count()函数
print('=*'*10, 'count()函数', '=*'*10)
str = 'hello world'
# 统计str中全部字母l的个数
print( str.count('l') )
# 统计str中从第5+1个字母到最后一个字母中，字母l的个数
print( str.count('l', 5, len(str)) )

## replace()函数
print('=*'*10, 'replace()函数', '=*'*10)
str = 'hello world hello world'
str1 = 'world'
str2 = 'waltsmith'
# 将所有的str1替换为str2
print( str.replace(str1, str2) )
# 只将前1个str1替换为str2
print( str.replace(str1, str2, 1) )