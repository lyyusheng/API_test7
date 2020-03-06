# 反射
class GetData:
    """类的反射可以动态的查看，增加，删除，更改类或者实例的属性"""
    COOKIES = 'jklgjkajklkh'


# 类属性
# print(GetData.COOKIES)
# print(GetData().COOKIES)

# 利用反射的方法拿值
# 1、获取
print(getattr(GetData, 'COOKIES'))  # 获取类属性的值

# 2、判断属性是否存在
print(hasattr(GetData, 'COOKIES'))  # 判断属性是非存在，返回值是bool

# 3、设置属性值
print(setattr(GetData, 'COOKIES', 123))  # 设置类的属型值（类名，属性，新的属性值）,无返回值
print(getattr(GetData, 'COOKIES'))  # 从新设置类的属性值之后，获取新的属性的值

# 4、删除类的属性值
# print(delattr(GetData, 'COOKIES'))  # 删除属性,不常用
# print(getattr(GetData, 'COOKIES'))  # 删除了在获取会报错，属性不存在了
