#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-13


## 查看python中的关键字
print('=*'*10, '查看python中的关键字', '=*'*10)
import keyword
print(keyword.kwlist)

### 左移与右移运算
print('=*'*10, '左移与右移运算', '=*'*10)
## 输出二进制数字
a = 15
b = 3
print("%d的二进制为：%s" % (a, "{:b}".format(a).rjust(8, '0')) )
print("%d的二进制为：%s" % (b, "{:b}".format(b).rjust(8, '0')) )
# 将a左移b位
print('=*'*10, '将a左移b位', '=*'*10)
l3 = a << b
print("%d的二进制为：%s" % (l3, "{:b}".format(l3).rjust(8, '0')) )
# 将a右移b位
print('=*'*10, '将a右移b位', '=*'*10)
r3 = a >> b
print("%d的二进制为：%s" % (r3, "{:b}".format(r3).rjust(8, '0')) )

## 负数的左右移操作
c = -7
print("\n%d的二进制为：%s" % (b, "{:b}".format(b).rjust(8)) )
print("%d二进制为：%s" % (c, "{:b}".format(c).rjust(8)) )
# 将c左移b位
print('=*'*10, '将c左移b位', '=*'*10)
nl3 = c << b
print("%d的二进制为：%s" % (nl3, "{:b}".format(nl3).rjust(8)) )
# 将c右移b位
print('=*'*10, '将c右移b位', '=*'*10)
nr3 = c >> b
print("%d的二进制为：%s" % (nr3, "{:b}".format(nr3).rjust(8)) )
