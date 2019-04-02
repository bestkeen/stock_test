import sys
import tushare as ts
code = sys.argv[1]
svol  = int(sys.argv[2])
#print (code)
#print (vol)
df = ts.get_sina_dd(code, date='2019-04-02',vol=svol)
print (df)
