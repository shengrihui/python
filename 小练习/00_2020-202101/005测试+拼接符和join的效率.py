import time
c=10**6

a=''
time1=time.time()
for i in range(c):
    a+='srh'
time2=time.time()
print('+拼接符运行时间：%f' %(time2-time1))

li=[]
time3=time.time()
for i in range(c):
    li.append('srh')
b=''.join(li)
time4=time.time()
print('join运行时间：%f' %(time4-time3))
