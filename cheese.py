from tkinter import *
fig=["♕♔♖♗♘♙","♛♚♜♝♞♟"]
p=0
f=0
f0=[0,0]
psh=[-1,-1,-1]
kr=[1,1]
l=[[1,1],[1,1]]
kkr=[[7,3],[0,3]]
bf=" "
pish=[[[1,-1],[1,1]],[[-1,-1],[-1,1]]]
kin=[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
kor=[[1,0],[1,1],[-1,0],[-1,1],[0,1],[1,-1],[0,-1],[-1,-1]]
matt=0
k3=[1,1]
kf=[16,16]
k=(not p) * 7
shag=-1
tur=[]
lad=[]
for i in range(8):
    tur.append([0,i])
    tur.append([i,0])
    tur.append([0, i*(-1)])
    tur.append([i*(-1), 0])
    lad.append([i, i])
    lad.append([i, i*(-1)])
    lad.append([i*(-1), i * (-1)])
    lad.append([i * (-1), i])
def rest():
    global a
    global p
    global f
    global fig
    global f0
    global k
    global k3
    global shag
    global psh
    global kr
    global b
    global matt
    global kkr
    global l
    matt=0
    p = 0
    f = 0
    f0 = [0, 0]
    psh = [-1, -1, -1]
    kr = [1, 1]
    l = [[1, 1], [1, 1]]
    kkr = [[7, 3], [0, 3]]
    k3 = [1, 1]
    k = (not p) * 7
    shag = -1
    lab3.pack_forget()
    for i in range(8):
        for j in range(8):
            a[i][j].config(bg="#ffffff"*((i+j)%2==1)+"#aaaaaa"*((i+j)%2==0),font=("","20"),text=fig[0][2]*(i==7 and (j==0 or j==7))+fig[1][2]*(i==0 and (j==0 or j==7))+fig[0][4]*(i==7 and (j==1 or j==6))+fig[1][4]*(i==0 and (j==1 or j==6))+fig[0][3]*(i==7 and (j==2 or j==5))+fig[1][3]*(i==0 and (j==2 or j==5))+fig[0][1]*(i==7 and j==4)+fig[1][1]*(i==0 and j==4)+fig[0][0]*(i==7 and j==3)+fig[1][0]*(i==0 and j==3)+fig[0][5]*(i==6)+fig[1][5]*(i==1)+" "*(1<i<6))
    for i in range(4):
        b[0][i].config(bg="#ffffff")
        b[1][i].config(bg="#ffffff")
    b[0][0].config(bg="#bbffbb")
    b[1][0].config(bg="#bbffbb")
def zm(x,p3):
    global b
    b[p3][k3[p3]-1].config(bg="#ffffff")
    b[p3][x].config(bg="#bbffbb")
    k3[p3]=x+1
def bezp(fp,ps):
    v=[]
    if a[fp[0]][fp[1]]["text"]==" ":
        if 8>fp[0]+ps*2-1>-1:
            if fig[not ps][5]==a[fp[0]+ps*2-1][fp[1]]["text"]:
                v.append([fp[0]+ps*2-1,fp[1]])
            elif fp==3+ps:
                if fig[not ps][5] == a[fp[0] + ps * 4 - 2][fp[1]]["text"]and " "== a[fp[0] + ps * 2 - 1][fp[1]]["text"]:
                    v.append([fp[0] + ps * 4 - 2, fp[1]])
    for i in range(len(kin)):
        if i<len(pish[ps]):
            fa=[fp[0]-pish[ps][i][0],fp[1]-pish[ps][i][1]]
            if -1 < fa[0] < 8 and -1 < fa[1] < 8:
                if fig[(not ps)][5]==a[fa[0]][fa[1]]['text']and fig[ps].count(a[fp[0]][fp[1]]["text"])==1:
                    v.append(fa)
        if i<len(kin):
            fa=[kin[i][0]+fp[0],kin[i][1]+fp[1]]
            if -1<fa[0]<8 and -1<fa[1]<8:
                if fig[(not ps)][4]==a[fa[0]][fa[1]]['text']:
                    v.append([fa[0],fa[1],"k"])
        if i<len(kor):
            fa=[kor[i][0]+fp[0],kor[i][1]+fp[1]]
            if -1 < fa[0] < 8 and -1 < fa[1] < 8:
                if fig[(not ps)][0]==a[fa[0]][fa[1]]['text']:
                    v.append(fa)
    i=fp[0]+1
    j=fp[1]+1
    while i<8 and j<8:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][3] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text']!=" ":
            if a[fp[0]][fp[1]]["text"]==" ":
                if a[i][j]['text'] !=fig[ps][0]:
                    break
            else:
                break
        i+=1
        j+=1
    i = fp[0] - 1
    j = fp[1] + 1
    while i >-1 and j < 8:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][3] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        i -= 1
        j += 1
    i = fp[0] + 1
    j = fp[1] - 1
    while i < 8 and j >-1:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][3] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        i += 1
        j -= 1
    i = fp[0] - 1
    j = fp[1] - 1
    while i > -1 and j >-1:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][3] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        i -= 1
        j -= 1
    i = fp[0]
    j = fp[1] + 1
    while j < 8:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][2] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        j += 1
    i = fp[0] - 1
    j = fp[1]
    while i > -1:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][2] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        i -= 1
    i = fp[0] + 1
    j = fp[1]
    while i < 8 :
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][2] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        i += 1
    i = fp[0]
    j = fp[1] - 1
    while j > -1:
        if fig[(not ps)][1] == a[i][j]['text'] or fig[(not ps)][2] == a[i][j]['text']:
            v.append([i,j])
            break
        elif a[i][j]['text'] != " ":
            if a[fp[0]][fp[1]]["text"] == " ":
                if a[i][j]['text'] != fig[ps][0]:
                    break
            else:
                break
        j -= 1
    if v==[]:
        return [-1,-1]
    else:
        return v
def bezp2(vf,fp):
    bf=a[fp[0]][fp[1]]["text"]
    for j in range(len (vf)):
        i=vf[0]
        a[fp[0]][fp[1]]["text"]=a[i[0]][i[1]]["text"]
        if a[fp[0]][fp[1]]["text"]==fig[p][0]:
            kkr[p]=fp
        a[i[0]][i[1]]["text"]=' '
        d=bezp(kkr[p],p)
        if a[fp[0]][fp[1]]["text"]==fig[p][0]:
            kkr[p]=i
        a[i[0]][i[1]]["text"]=a[fp[0]][fp[1]]["text"]
        a[fp[0]][fp[1]]["text"] = bf
        if d!=[-1,-1]:
            vf.remove(i)
        else:
            break
    return vf
def mat(kl):
    global lab3
    global matt
    for i in kor:
        if 8>kkr[p][0]+i[0]>-1and 8>kkr[p][1]+i[1]>-1:
            a[kkr[p][0]+i[0]][kkr[p][1]+i[1]]["text"]==fig[p][5]
            if bezp([kkr[p][0]+i[0],kkr[p][1]+i[1]],p)==[-1,-1]and fig[p].count(a[kkr[p][0]+i[0]][kkr[p][1]+i[1]]["text"])==0:
                a[kkr[p][0] + i[0]][kkr[p][1] + i[1]]["text"] == " "
                return 0
            a[kkr[p][0] + i[0]][kkr[p][1] + i[1]]["text"] == " "
    for i in kl:
        if len(i)<3:
            j=kkr[p][0]+int(abs(i[0]-kkr[p][0])/(i[0]-kkr[p][0]+1*(i[0]==kkr[p][0])))
            g=kkr[p][1]+int(abs(i[1]-kkr[p][1])/(i[1]-kkr[p][1]+1*(i[1]==kkr[p][1])))
            while j!=i[0]and g!=i[1]:
                if bezp([j,g],int(not p))!=[-1,-1]:
                    if bezp([j,g],int(not p)).count(kkr[p])and len(bezp([j,g],int(not p)))==1:
                        if bezp([j,g],p)==[-1,-1]:
                            return 0
                    else:
                        return 0
                j += int(abs(i[0] - kkr[p][0]) / (i[0] - kkr[p][0] + 1 * (i[0] == kkr[p][0])))
                g += int(abs(i[1] - kkr[p][1]) / (i[1] - kkr[p][1] + 1 * (i[1] == kkr[p][1])))
            if bezp([j, g], int(not p)) != [-1, -1]:
                if bezp([j, g], int(not p)).count(kkr[p]) and len(bezp([j, g], int(not p))) == 1:
                    if bezp([j, g], p) == [-1, -1]:
                        return 0
                else:
                    return 0
        else:
            j=i[0]
            g=i[0]
            if bezp([j, g], int(not p)) != [-1, -1]:
                if bezp([j, g], int(not p)).count(kkr[p]) and len(bezp([j, g], int(not p))) == 1:
                    if bezp([j, g], p) == [-1, -1]:
                        return 0
                else:
                    return 0
    lab3.config(text="Гравець "+str((not p)+1)+" виграв!")
    lab3.pack(expand=1)
    matt=1
    return 1
def pat(p):
    global matt
    for i in range(8):
        for j in range(8):
            h = []
            if psh [2]== [(not p)]:
                if psh[1] > 0:
                    if a[psh[0]][psh[1] - 1]['text'] == fig[p][5]:
                        h.append(psh[:2])
            if fig[p].count(a[i][j]["text"])!=1:
                h+=bezp([i,j],int(not p))
                for x in range(h.count(-1)):
                    h.remove(-1)
                if a[i-(p*2-1)][j]['text']==fig[p][5]and a[i][j]["text"]==" ":
                    h.append([i-p*2+1,j])
                if a[1+5*p][j]['text']==fig[p][5]and a[i][j]["text"]+a[i-(p*2-1)][j]["text"]=="  "and i==3+p:
                    h.append([1+5*p,j])
                if len(bezp2(h,[i,j]))!=0:
                    return 0
    lab3.config(text="Нічия")
    lab3.pack(expand=1)
    matt = 1
    return 1
def prav(f0,f1):
    global tur
    global lad
    global pish
    global kin
    global kor
    global psh
    global kr
    if psh[2]==p:
        psh=[-1,-1,-1]
    if fig[p][5]==a[f0[0]][f0[1]]["text"]:
        if [0, p * 4 - 2] == [(f1[1] - f0[1]) ,f1[0] - f0[0] ]and f0[0]==(not p)*7+(p*2-1):
            if a[f1[0]][f1[1]]["text"] == ' 'and a[f1[0]-p*2+1][f1[1]]["text"] == ' ':
                psh=[f1[0],f1[1],p]
                return 1
        if 0==f1[1]-f0[1] and (f1[0]-f0[0])*(p*2-1)==1:
            if a[f1[0]][f1[1]]["text"]==' ':
                if f1[0]==p*7:
                    return 3
                return 1
        elif pish[not p].count([f1[0]-f0[0],f1[1]-f0[1]]):
            if a[f1[0]][f1[1]]["text"]!=' ':
                if f1[0]==p*7:
                    return 3
                return 1
            elif a[f0[0]][f1[1]]["text"]!=' 'and psh==[f0[0],f1[1],(not p)]:
                return 2
    if fig[p][2] == a[f0[0]][f0[1]]["text"]:
        if tur.count([f1[1]-f0[1],f1[0]-f0[0]]):
            if f0[0] == f1[0]:
                for i in range(f0[1] + int((f1[1] - f0[1]) / abs(f1[1] - f0[1])), f1[1],int((f1[1] - f0[1]) / abs(f1[1] - f0[1]))):
                    if a[f0[0]][i]["text"] != " ":
                        return 0
                if f0 == [0, 0]:
                    l[p][0] = 0
                if f0 == [0, 7]:
                    l[p][1] = 0
                if f0 == [7, 0]:
                    l[p][0] = 0
                if f0 == [7, 7]:
                    l[p][1] = 0
                return 1
            elif f0[1] == f1[1]:
                for i in range(f0[0] + int((f1[0] - f0[0]) / abs(f1[0] - f0[0])), f1[0],int((f1[0] - f0[0]) / abs(f1[0] - f0[0]))):
                    if a[i][f0[1]]["text"] != " ":
                        return 0
                if f0 == [0, 0]:
                    l[p][0] = 0
                if f0 == [0, 7]:
                    l[p][1] = 0
                if f0 == [7, 0]:
                    l[p][0] = 0
                if f0 == [7, 7]:
                    l[p][1] = 0
                return 1
    if fig[p][3] == a[f0[0]][f0[1]]["text"]:
        if lad.count([f1[1] - f0[1], f1[0] - f0[0]]):
            fx = [0, 0]
            fx[0] = f0[0]
            fx[1] = f0[1]
            fx[0] += int(abs(f1[0] - fx[0]) / (f1[0] - fx[0]))
            fx[1] += int(abs(f1[1] - fx[1]) / (f1[1] - fx[1]))
            while fx != f1:
                if a[fx[0]][fx[1]]["text"] != " ":
                    return 0
                fx[0] += int(abs(f1[0] - fx[0]) / (f1[0] - fx[0]))
                fx[1] += int(abs(f1[1] - fx[1]) / (f1[1] - fx[1]))
            return 1
    if fig[p][4] == a[f0[0]][f0[1]]["text"]:
        if kin.count([f1[1] - f0[1], f1[0] - f0[0]]):
            return 1
    if fig[p][1] == a[f0[0]][f0[1]]["text"]:
        if tur.count([f1[1]-f0[1],f1[0]-f0[0]]):
            if f0[0] == f1[0]:
                for i in range(f0[1] + int((f1[1] - f0[1]) / abs(f1[1] - f0[1])), f1[1],int((f1[1] - f0[1]) / abs(f1[1] - f0[1]))):
                    if a[f0[0]][i]["text"] != " ":
                        return 0
                return 1
            elif f0[1] == f1[1]:
                for i in range(f0[0] + int((f1[0] - f0[0]) / abs(f1[0] - f0[0])), f1[0],int((f1[0] - f0[0]) / abs(f1[0] - f0[0]))):
                    if a[i][f0[1]]["text"] != " ":
                        return 0
                return 1
        elif lad.count([f1[1] - f0[1], f1[0] - f0[0]]):
            fx = [0, 0]
            fx[0] = f0[0]
            fx[1] = f0[1]
            fx[0] += int(abs(f1[0] - fx[0]) / (f1[0] - fx[0]))
            fx[1] += int(abs(f1[1] - fx[1]) / (f1[1] - fx[1]))
            while fx != f1:
                if a[fx[0]][fx[1]]["text"] != " ":
                    return 0
                fx[0] += int(abs(f1[0] - fx[0]) / (f1[0] - fx[0]))
                fx[1] += int(abs(f1[1] - fx[1]) / (f1[1] - fx[1]))
            return 1
    if fig[p][0] == a[f0[0]][f0[1]]["text"]:
        if kor.count([f1[1] - f0[1], f1[0] - f0[0]]):
            kr[p]=0
            kkr[p]=f1
            return 1
        elif kr[p]and f1[0] == f0[0]:
            if f1[1] == 1and l[p][0]:
                if a[k][2]["text"] == " " and a[k][1]["text"] == " ":
                    kr[p] = 0
                    kkr[p] = f1
                    return 4
            if f1[1]==5 and l[p][1]:
                if a[k][4]["text"] == " " and a[k][5]["text"] == " " and a[k][6]["text"] == " ":
                    kr[p] = 0
                    kkr[p] = f1
                    return 5
    return 0
def funk(x,y):
    global bf
    global a
    global lab4
    global p
    global f
    global fig
    global f0
    global k
    global k3
    global kf
    global shag
    if not matt:
        if f==0:
            if fig[p].count(a[x][y]["text"])==1:
                if ((a[x][y]["bg"] == "#ffffff") or (a[x][y]["bg"] == "#aaaaaa")):
                    a[x][y].config(bg="#bbbbff"*((x+y)%2==1)+"#9999cc"*((x+y)%2==0))
                f=1
                f0=[x,y]
        elif fig[p].count(a[x][y]["text"]) == 0:
            h=prav(f0,[x,y])
            if h:
                if h==2:
                    a[f0[0]][y].config(text=" ")
                elif h==3:
                    a[f0[0]][f0[1]].config(text=fig[p][k3[p]])
                elif h==4:
                    a[(not p)*7][2].config(text=fig[p][2])
                    a[(not p) * 7][0].config(text=" ")
                elif h==5:
                    a[(not p)*7][4].config(text=fig[p][2])
                    a[(not p) * 7][7].config(text=" ")
                bf=a[x][y]['text']
                a[x][y].config(text=a[f0[0]][f0[1]]["text"])
                a[f0[0]][f0[1]].config(text=" ")
                if ((a[f0[0]][f0[1]]["bg"]=="#bbbbff")or (a[f0[0]][f0[1]]["bg"]=="#9999cc")):
                    a[f0[0]][f0[1]].config(bg=("#ffffff" * ((f0[0] + f0[1]) % 2 == 1) + "#aaaaaa" * ((f0[0] + f0[1]) % 2 == 0)))
                if shag==p or(shag!=p and bezp(kkr[p],p)!=[-1,-1]):
                    if bezp(kkr[p],p)!=[-1,-1]:
                        if h==2:
                            a[f0[0]][y]["text"]=fig[int(not p)][5]
                        if h==3:
                            a[x][y]["text"]=fig[p][5]

                        a[f0[0]][f0[1]]['text']=a[x][y]["text"]
                        a[x][y].config(text=bf)
                        if (a[f0[0]][f0[1]]["bg"] == "#ffffff") or (a[f0[0]][f0[1]]["bg"] == "#aaaaaa"):
                            a[f0[0]][f0[1]].config(bg="#bbbbff" * ((f0[0] + f0[1]) % 2 == 1) + "#9999cc" * ((f0[0] + f0[1]) % 2 == 0))
                    else:
                        shag=-1
                        a[kkr[p][0]][kkr[p][1]].config(bg="#ffffff" * ((kkr[p][0] + kkr[p][1]) % 2 == 1) + "#aaaaaa" * ((kkr[p][0] + kkr[p][1]) % 2 == 0))
                        for i in kor:
                            if -1<kkr[p][0]+i[0]<8and-1<kkr[p][1]+i[1]<8:
                                a[kkr[p][0]+i[0]][kkr[p][1]+i[1]].config(bg="#ffffff" * ((kkr[p][0]+i[0] + kkr[p][1]+i[1]) % 2 == 1) + "#aaaaaa" * ((kkr[p][0]+i[0] + kkr[p][1]+i[1]) % 2 == 0))
                        p = not p
                        k = (not p) * 7
                        if bezp(kkr[p], p) != [-1, -1]:
                            shag = p
                            if mat(bezp(kkr[p], p)):
                                return 0
                            a[kkr[p][0]][kkr[p][1]].config(bg="#ffffbb" * ((kkr[p][0] + kkr[p][1]) % 2 == 1) + "#cccc99" * ((kkr[p][0] + kkr[p][1]) % 2 == 0))
                        if pat(p):
                            return 0
                        f = 0
                else:
                    p = not p
                    k = (not p) * 7
                    if bezp(kkr[p],p)!=[-1,-1]:
                        shag=p
                        if mat(bezp(kkr[p], p)):
                            return 0
                        a[kkr[p][0]][kkr[p][1]].config(bg="#ffffbb" * ((kkr[p][0] + kkr[p][1]) % 2 == 1) + "#cccc99" * ((kkr[p][0] + kkr[p][1]) % 2 == 0))
                    if pat(p):
                        return 0
                    f=0
        else:
            if ((a[f0[0]][f0[1]]["bg"]=="#bbbbff")or (a[f0[0]][f0[1]]["bg"]=="#9999cc")):
                a[f0[0]][f0[1]].config(bg=("#ffffff" * ((f0[0] + f0[1]) % 2 == 1) + "#aaaaaa" * ((f0[0] + f0[1]) % 2 == 0)))
            if ((a[x][y]["bg"]=="#ffffff")or (a[x][y]["bg"]=="#aaaaaa")):
                a[x][y].config(bg=("#bbbbff" * ((x + y) % 2 == 1) + "#9999cc" * ((x + y) % 2 == 0)))
            f0 = [x, y]
    if p:
    	lab4.config(bg='#000000')
    else:
    	lab4.config(bg='#ffffff')
w=Tk(className="Шахи")
w.geometry("800x640")
w.resizable(0,0)
a=[[]for i in range(8)]
for i in range(8):
    for j in range(8):
        a[i].append(Button(w,bg="#ffffff"*((i+j)%2==1)+"#aaaaaa"*((i+j)%2==0),font=("","20"),text=fig[0][2]*(i==7 and (j==0 or j==7))+fig[1][2]*(i==0 and (j==0 or j==7))+fig[0][4]*(i==7 and (j==1 or j==6))+fig[1][4]*(i==0 and (j==1 or j==6))+fig[0][3]*(i==7 and (j==2 or j==5))+fig[1][3]*(i==0 and (j==2 or j==5))+fig[0][1]*(i==7 and j==4)+fig[1][1]*(i==0 and j==4)+fig[0][0]*(i==7 and j==3)+fig[1][0]*(i==0 and j==3)+fig[0][5]*(i==6)+fig[1][5]*(i==1)+" "*(1<i<6)))
        a[i][j].place(relx=j*0.1,rely=i*0.125,relwidth=0.1, relheight=0.125)
        a[i][j].config(command=lambda x=i,y=j:funk(x,y))
b=[[],[]]
lab1=Label(w,font=("","5"),text='Пішак\nзамінюється на:')
lab1.place(relx=0.8,rely=0.3125,relwidth=0.2, relheight=0.0625)
lab2=Label(w,font=("","4"),text='!Налаштуйте фігуру\nдля заміни до\nперетворення пішака!')
lab2.place(relx=0.8,rely=0.875,relwidth=0.2, relheight=0.125)
lab3=Label(w,font=("","20"))
lab3.place_forget()
lab4=Label(w,bg="#ffffff")
lab4.place(relx=0.8,rely=0.0625,relwidth=0.2, relheight=0.1875)
res=Button(w,font=("","5"),text="Нова гра",command=lambda :rest())
res.place(relx=0.8,rely=0,relwidth=0.2, relheight=0.0625)
Button(w,font=("","15"),text="Вихід",command=lambda :w.destroy()).place(relx=0.8,rely=0.25,relwidth=0.2, relheight=0.0625)
for i in range(4):
    b[0].append(Button(w,font=("","20"),text=fig[0][i+1]))
    b[1].append(Button(w, font=("", "20"), text=fig[1][i + 1]))
    b[0][i].place(relx=0.8,rely=0.375+i*0.125,relwidth=0.1, relheight=0.125)
    b[1][i].place(relx=0.9, rely=0.375 + i * 0.125, relwidth=0.1, relheight=0.125)
    b[0][i].config(command=lambda x=i:zm(x,0))
    b[1][i].config(command=lambda x=i: zm(x, 1))
    b[0][0].config(bg="#bbffbb")
    b[1][0].config(bg="#bbffbb")
w.mainloop()