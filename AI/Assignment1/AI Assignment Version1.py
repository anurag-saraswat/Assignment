
def find_max(node,lst,final_list):
    detail = {'node':node,'val':0}
    for i in range(len(lst[node])):
        if (i not in final_list) and lst[node][i] > detail['val']:
            detail['val'] = lst[node][i]
            detail['node'] = i
    return detail['node']
        
def ShapingOutput(final_list,k,m,t):

    market=[[] for i in range(m)]
    count = 0
        
    for p in range(t):
        for q in range(m):
            for r in range(k):
                market[q].append(final_list[count])
                count += 1
    return market

def printOutput(market_list,k,m,t):
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

for f in range(t):
    for g in range(shops):
        if g not in final_list:
            final_list.append(g)
            break

    for h in range(m):
        for z in range(k-1):
            temp=find_max(final_list[-1],sim,final_list)
            final_list.append(temp)

        if( (len(final_list) != shops) and (h != m-1)):
            temp = find_max(final_list[-k],diff,final_list)
            final_list.append(temp)

market_list = ShapingOutput(final_list,k,m,t)
printOutput(market_list,k,m,t)




