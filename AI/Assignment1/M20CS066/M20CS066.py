

def chooseBest(ans_list):
    '''
        This Function chooses best output which maximises the goodness
    '''
    temp = []
    max_val = 0
    for i in ans_list:
        goodness_val = goodness(i)
        if goodness_val > max_val:
            max_val = goodness_val
            temp = i
    market_list = ShapingOutput(temp)
    printOutput(market_list)
        


def goodness(final_list):
    '''
       This function calculats goodness
       It uses two function calcSimilarity and calcDifference
       G(list) = calcSimilarity + C* calcDifference
         Here c is goodness constant
    '''
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

def calcSimlarity(lst):
    '''
        It calculate similarity among elements
    '''
    val = 0
    for i in lst :
        for j in range(len(lst)):
            for k in range(j+1,len(lst)):
                val += sim[j][k]
    return val

def calcDifference(lst):
    '''
        It calculate difference among elements
    '''
    val = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for p in range(len(lst[i])):
                for q in range (len(lst[j])):
                    val = val + diff[lst[i][p]][lst[j][q]]                   
    return val

def ShapingOutput(final_list):
    '''
          It it supplementary function( for print output) to shape output. 
    '''
    market=[[] for i in range(m)]
    count = 0

    for p in range(t):
        for q in range(m):
            for r in range(k):
                market[q].append(final_list[count])
                count += 1
    return market

def printOutput(market_list):
    '''
          It is used to print output in desired format
    '''
    count=0
    for p in range(m):
        num = 0
        for q in range(len(market_list[p])):  
            print(market_list[p][q]+1,end=" ") 
            num+=1   
            if((num%k==0) and (q != len(market_list[p])-1)):
                print("|",end = " ")
        print("")

def find_max(lst, n):

    '''
        This for first market of each time slot. 
        This will return shop with maximum similarity in same market.
    '''
    detail = {'node':-1,'val':0}
    count = n
    for i in range(shops):
        avg = 0
        count = n
        if i not in final_list:
            while(count):
                avg = avg + lst[i][final_list[-count]]
                count -= 1
            avg = avg/n
            if(avg > detail['val']):
                detail['val'] = avg
                detail['node'] = i
    return detail['node']

def find_max1(n,itr):
    '''
        This is for all market except first market of each time slot. 
        This will return shop with maximum similarity in same market and maximum difference among other parallel market.
    '''
    detail = {'node':-1,'val':0}
    count = n
    for i in range(shops):
        s = 0
        d = 0
        count = n
    
        if i not in final_list:
            while(count):
                s = s + sim[i][final_list[-count]]
                count -= 1
        
            for mtr in range(itr,len(final_list)-n):
                d = d + diff[i][final_list[mtr]]
            good_ness = s+c*d
            
            
            if(good_ness > detail['val']):
                detail['val'] = good_ness
                detail['node'] = i

    return detail['node']
        

# -----------------Taking Input------------------------------------------------

k = int(input()) # total types of shops opening in one time slot in one market
m = int(input()) # number of parallel markets
t = int(input()) # number of time slots
c = float(input()) # trade-off constant 
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------

'''
    Preparing Matrix 
            diff : Contain difference cost among node
            sim  : Contain Similarity cost among node
            
'''
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
#--------------------------------------------------------------------------------

# Initialization of list which contain possible schedule
ans_list = []


#-------------------------------------------------------------------------------- 
'''
     Driver Code : To find possible schedule using Greedy Search 
'''
for val in range(shops):
    final_list = [val]
    for f in range(t):
        for g in range(shops):
            if (f!=0) and(g not in final_list):
                final_list.append(g)
                break

        for h in range(m):
            if (h==0):
                for z in range(1,k):
                    temp = find_max(sim,z)
                    final_list.append(temp)
            else:
                for z in range(1,k):
                    temp = find_max1(z,(f)*k*m)
                    final_list.append(temp)

        
            if( (len(final_list) != shops) and (h != m-1)):
                temp = find_max(diff,k)
                final_list.append(temp)
    ans_list.append(final_list)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
'''
    This Function call chooses the schedule which maximises the goodness and print output
'''
chooseBest(ans_list)

#-----------------------------------END-----------------------------------------