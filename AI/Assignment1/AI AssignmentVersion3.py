

def chooseBest(final_list):
    temp = []
    max_val = 0
    for i in final_list:
        goodness_val = goodness(i)
        if goodness_val > max_val:
            temp = i

    market_list = ShapingOutput(temp)
    printOutput(market_list)
        

def calcSimlarity(lst):
    val = 0
    for i in lst :
        for j in range(len(lst)):
            for k in range(j+1,len(lst)):
                val += sim[j][k]
    return val

def calcDifference(lst):
    #print(lst)
    val = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for p in range(len(lst[i])):
                for q in range (len(lst[j])):
                    val = val + diff[lst[i][p]][lst[j][q]]                   
    return val

def goodness(final_list):
    count = 0
    sim_val = 0
    diff_val = 0 
    for p in range(t):
        temp1 = []
        for q in range(m):
            temp2=[]
            for r in range(k):
                temp2.append(final_list[count])
                count+=1
            temp1.append(temp2)   
        sim_val += calcSimlarity(temp1)
        diff_val += calcDifference(temp1)

    return sim_val + c * diff_val

def find_max(node,lst,final_list):
    detail = {'node':node,'val':0}
    for i in range(len(lst[node])):
        if (i not in final_list) and lst[node][i] > detail['val']:
            detail['val'] = lst[node][i]
            detail['node'] = i
    return detail['node']
        
def ShapingOutput(final_list):

    market=[[] for i in range(m)]
    count = 0
        
    for p in range(t):
        for q in range(m):
            for r in range(k):
                market[q].append(final_list[count])
                count += 1
    return market

def printOutput(market_list):
    count=0
    for p in range(m):
        num = 0
        for q in range(len(market_list[p])):  
            print(market_list[p][q]+1,end=" ") 
            num+=1   
            if((num%k==0) and (q != len(market_list[p])-1)):
                print("|",end = " ")
        print("")


k = int(input()) # total types of shops opening in one time slot in one market
m = int(input()) # number of parallel markets
t = int(input()) # number of time slots
c = float(input()) # trade-off constant 

diff = []
sim = []

l = [float(i) for i in (input().split(" "))]
shops = len(l)
diff.append(l)

l = [round((1-i),3) for i in l]
sim.append(l)

for i in range(0,shops-1):
    l = [float(i) for i in (input().split(" "))]
    diff.append(l)
    l = [round((1-i),4) for i in l]
    sim.append(l)

final_list = []
for val in range(k):
    temp_list = []
    for f in range(t):
        for g in range(shops):
            if g not in temp_list:
                temp_list.append(g)
                break
        for h in range(m):
            for z in range(k-1):
                temp=find_max(temp_list[-1],sim,temp_list)
                temp_list.append(temp)
            if( (len(final_list) != shops) and (h != m-1)):
                temp = find_max(temp_list[-k+val],diff,temp_list)
                temp_list.append(temp)
    final_list.append(temp_list)

chooseBest(final_list)







