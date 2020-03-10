#文件處理(掌握open（）函数，会读，其他的知道就行)
#open()  #打開或者創建文件
#file:要打開或者要創建的目標文件的文件名#mode：打開的模式
# 只读r
# 只写w ：file已经存在则清空再写（慎用），file不存在则新建文件再写
# 读写 r+
#读写 w+ 不好用，会清空
# 追加a 不可读
#追加a+ 可读
#a+ w+ 读取内容时，光标在最后面 所以读取不到任何内容
#encoding: 要读或者要写的内容包含中文，则要设置encoding=utf-8
file=open('xiaoshi.txt','r',encoding='utf-8')#打开的文件对象，存在file这个变量里
#res=file.read() #读操作，参数表示指定读的元素个数，例如read（5）就是读5个字，不写参数则默认全读
for i in range(1,20):
    res1=file.readline()#读一行,要注意的是，不能同时执行两个file.read(),会啥也读不出来，可能跟光标移动有关，所以执行这里时要把res注释掉
    #if i==3:
    print(res1)
#res2=file.readlines()#全读，返回结果是列表，每一行的值作为列表的一个元素
#读写操作
#file.write('lemonclass')
#移动光标
#file.seek(0,0)  #第一个参数 ：你要移动多少个偏移量
# 第二个参数：相对谁去移动（0头部，1，当前位置，2最末尾）
#res3=file.read()
#print(res2)
#print(res)
#print(res3)