def index(lst2):
    temp = []
    for i in range(len(lst2)):
        if(lst2[i] == '1'):
            temp.append(i)
    return temp

def genPer(node,depd_lst,val):
    depd_lst.insert(0,node)
    temp = [[i] for i in val[depd_lst[-1]]]

    for i in range(len(depd_lst)-2,-1,-1):
        temp1 = temp[:]
        temp=[]
        for j in val[depd_lst[i]]:
            for k in range(len(temp1)):
                t = temp1[k][:]
                t.insert(0,j)
                temp.append(t)
    return temp

n = int(input())


val = []
for i in range(n):
    f_val = input().split(",")
    for j in range(len(f_val)):
        if(f_val[j][0]==' '):
            f_val[j] = f_val[j][1:]
    val.append(f_val)

matrix = []
for i in range(n):
    temp = input().split(" ")
    matrix.append(temp)

# Taking Transpose
matrix = list(map(list, zip(*matrix))) 

lst1 = []
num = int(input())
for i in range(num):
    temp = input().split(",")
    lst1.append(temp)


for i in range(n):
    lst3 = index(matrix[i])
    if(lst3 == []):
        result = [];
        for k in range(len(val[i])):
            result.append(0)

        for j in range(num):
            for k in range(len(val[i])):
                if(lst1[j][i] == val[i][k]):
                    result[k] +=1
        for j in range(len(result)):
            if(j==len(result)-1):
                print(format(result[j]/num, '.4f'))
            else:
                print(format(result[j]/num, '.4f'),end = " ")
        
    else:
        permu = genPer(i,lst3,val)
        result = []

        for p in range(len(permu)):
            t_val = 0
            total = 0
            for e in lst1:
                count = 0
                count1 = 0
                for q in range(len(lst3)):
                    if(e[lst3[q]] == permu[p][q]):
                        if(q!=0):
                            count1+=1
                        count+=1
            
                if(count == len(lst3)):
                    t_val += 1
                if(count1 == len(lst3)-1):
                    total += 1
            if(total == 0):
                result.append(0)
            else:
                result.append(t_val/total)

        for q in range(len(result)):
            if(q == len(result)-1):
                print(format(result[q], '.4f'))
            else:
                print(format(result[q], '.4f'),end=" ")
                    





        

