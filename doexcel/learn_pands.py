import pandas as pd
df=pd.read_excel('python_hw.xlsx')#默認讀取第一個表單，如果出現讀取的内容對不上，就要檢查一下
#從0開始讀，而openpyxl是從1開始讀，要注意兩者區別
#按行读取，但是把第一行当作表头，所以第一行内容会消失。解决办法是多插入一行，第一行当作表头，且要填入数据，保存，空着还是读不到
print(df.values)
#報錯：ImportError: Install xlrd >= 1.0.0 for Excel support，執行pip install xlrd
#作为拓展，不掌握也行