
import random,time

pai_list=list('3456789')+['10']+list('JQKA2SB')
    
def fapai():
    p=list("A23456789JQK"*4)+['10']*4+['S','B']
    for i in range(100):
        random.shuffle(p)
    player1=[]
    player2=[]
    player3=[]
    while len(p)>3:
        player1.append(p.pop(0))
        player2.append(p.pop(0))
        player3.append(p.pop(0))
    return p,player1,player2,player3

def disp(p):
    x=''
    for i in p:
        x += i+' '
    return x

def jiaodz(p1,p2,p3):   
    def  put(t):
        print('\n'*10 if z!=[] else '')
        x=input('玩家{}：\n你的牌是{}\n剩余的牌是：{}\n你是否叫地主？（Y/N）：'.format(t,disp(sort_pai(p[a.index(t)+1])),disp(sort_pai(rest))))
        while 1:
            if not(x=='n' or x=='N' or x=='Y' or x=='y'):
                print('输入有误哦，再来一次吧。（不区分大小写哦）')
                x=input('玩家{}是否叫地主？（Y/N）：'.format(t))
            if x=='Y' or x=='y':
                z.append(t)
                break
            elif x=='N' or x=='n':
                break
 
    c=0
    a=[p1,p2,p3]
    random.shuffle(a)
    while 1:
        p=fapai()
        rest,player1,player2,player3=p

        z=[]
        for i in a:
            put(i)
        if len(z) != 0 :
            if len(z) == 3:
                put(a[0])

            p[a.index(z[-1])+1].extend(rest)
            break
        else :
            c += 1
            if c==3:
                p[a.index(a[0])+1].extend(rest)
                break
            else:
                a=a[1:]+a[:1]
    player1=sort_pai(player1)
    player2=sort_pai(player2)
    player3=sort_pai(player3)
    return list(zip(a,[player1,player2,player3]))

def sort_v(t):
    return pai_list.index(t)

def sort_pai(pai,rev=False):
    pai=sorted(pai,key=lambda x:sort_v(x))
    if rev:
        pai=pai[::-1]
    return pai

def count_pai(pai):
    lp=list(set(pai))
    lp.sort(reverse=True,key=lambda x:sort_v(x))
    lc=[pai.count(i) for i in lp]
    lp_e=list(enumerate(lp))
    lc_e=list(enumerate(lc))
    lcs=sorted(lc_e,key=lambda x:x[1],reverse=True)
    lpt=[ j for i in lcs for j in lp_e if i[0]==j[0]  ]
    result_p=[lpt[i][1]for i in range(len(lpt))]
    result_c=[lcs[i][1]for i in range(len(lcs))]
    return result_p,result_c
    
def sort_pai_c(pai):
    p=count_pai(pai)[0]
    c=count_pai(pai)[1]
    lst=[i for i in p for j in range(c[p.index(i)])]
    return lst

def pai_type(pai):
    lp=count_pai(pai)[0]
    lc=count_pai(pai)[1]
    le=len(lp)
    cm=max(lc)
    if lc==[4]:
        return "炸弹"
    elif cm==3 :
        c3=lc.count(3)
        if c3==1:
            if lc==[3]:
                return '三张'
            elif lc==[3,1]:
                return '三带一'
            elif lc==[3,2]:
                return '三带二'
        elif c3>1:
            return '飞机{}'.format(c3)
    elif cm==2:
        if le==1:
            return '一对'
        elif le>2 :
            return '连对{}'.format(le)
    elif cm==1:
        if le==1:
            return '一张'
        elif le>=5 :
            return '顺子{}'.format(le)
        elif le==2 :
            if lp==['B','S']:
                return '王炸'

def err(pai,pl):
    pll=pl[:]
    def pp(lp,lc,n):
        for i in range(1,len(lp)):
            if  lc[i]==n:
                if sort_v(lp[i]) != sort_v(lp[i-1])-1:
                    return False
        else :
            return True
    for i in pai:
        try:
            pll.remove(i)
        except:
            return False
    lp=count_pai(pai)[0]
    lc=count_pai(pai)[1]
    cm=max(lc)
    for i in lc:
        if i>4:
            return False
    if pai.count('S')>1 or pai.count('B')>1:
        return False
    if cm==4 :
        if len(lp)!=1:
            return False
    elif cm==3 :
        if lc.count(3)!=(lc.count(2) or lc.count(1)) :
            return False
        return pp(lp,lc,cm)
    elif cm==2:
        if len(lp)==2 or (1 in lc):
            return False
        return pp(lp,lc,cm)
    elif cm ==1:
        if len(lp)==1:
            return True
        if len(lp)<5 :
            if 'S' not in lp and 'B' not in lp:
                return False
        return pp(lp,lc,cm)
    else:
        return True
 

print('''
你好！
这是一个有点小愚蠢的斗地主小游戏。
虽然有点小愚蠢，但还是可以玩的哦。
要开始吗？
''')

t=input('输入"Y"表示开始，输入"N"表示离开（不区分大小写）:')

while 1:
    t=t.upper()
    if t!='Y' and t!='N':
        print('你输了个啥？')
        t=input('再来一遍吧：')
    else:
        break
if t=='N':
    print('啊，这。')
    time.sleep(2)
    print('这。')
    time.sleep(2)
    print('那再见吧。')
    time.sleep(5)
elif t=='Y':
    print("""
那开始吧。
规则什么的就和斗地主一样，我就不说了。
只是我们的出牌方式是需要键盘输入的，但也是不区分大小写的。
其中，大王用'B'来表示，小王用'S'来表示。
对输入没有特殊要求哦。
现在，让我们开始吧！
       
    """)
    
        
    player1_name=input('请输入玩家1的名字：')
    player2_name=input('请输入玩家2的名字：')
    player3_name=input('请输入玩家3的名字：')
    player_name_list=[player1_name,player2_name,player3_name]
    
    
    #player_name_list=['shengrihui','python','spyder']
    t=jiaodz(*player_name_list)
    play=[[k,v] for k,v in t]
    for i in play:
        if len(i[1])==20 :
            i[0]='地主'+i[0]
            dzn=play.index(i)
        else:
            i[0]='农民'+i[0]
    play=play[dzn:]+play[:dzn]
    
    def isv():
        for i in play:
            if len(i[1])==0:
                return True
        else:
            return False
    
    
    def compare(a,b):
        if b==[] or pai_type(a)=='王炸':
            return True
        if pai_type(a)=='炸弹':
            return True
        elif pai_type(a)==pai_type(b):
            if sort_v(a[0])>sort_v(b[0]):
                 return True
        return False
    
    pas=0
    cp_be=[]
    lastcon=''
    for i in play*1000:
        cou=[[j[0],'还有%d张牌'%(len(j[1]))] for j in play if j[0]!=i[0] ]
        con='{0}{1}现在，{2}{3}，{4}{5}'.format(lastcon,'\n' if lastcon!='' else '',cou[0][0],cou[0][1],cou[1][0],cou[1][1])
        print('\n'*30+'{}：\n{},\n你的牌还有：{}'.format(i[0],con,disp(i[1])))
        
        cp_pai=input('{}请出牌：'.format(i[0]))
        while 1:
            if pas == 2:
                cp_be=[]
            if cp_pai=='pass' or cp_pai=='PASS':
                if cp_be ==[] :
                    print('你不能过哦。')
                    cp_pai=input('{}请出牌：'.format(i[0]))
                    continue 
                if  pas <2:
                    pas+=1
                    lastcon +='\n{}出牌：过'.format(i[0])
                    break
            try:
                cp_pai=cp_pai.upper()
                cptt=['10' for j in range(cp_pai.count('10'))]
                for j in cp_pai:
                    try:
                        if j in pai_list :
                            cptt.append(j)
                    except:
                        break
                cp_pai=cptt
                cp_pai=sort_pai_c(cp_pai)
            except:
                print('这牌出的不对哦。')
                cp_pai=input('{}请出牌：'.format(i[0]))
            else:
                if compare(cp_pai,cp_be) :
                    cp_be=cp_pai
                    for j in cp_pai:
                        i[1].remove(j)
                    la='{}出出牌：{} {}'.format(i[0],pai_type(cp_pai),disp(cp_pai))
                    lastcon += ('\n'+la if lastcon!='' else la)
                    pas=0
                    break
                else:
                    print('这牌没法打人家哦。')
                    cp_pai=input('{}请出牌：'.format(i[0]))
        if  isv():
            print('{}胜利！'.format(i[0]))
            break
          
     
    

