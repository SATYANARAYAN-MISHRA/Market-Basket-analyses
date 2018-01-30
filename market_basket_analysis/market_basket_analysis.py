import sys
import math
daata = [['i1','i2','i5'],['i2','i4'],['i2','i3'],['i1','i2','i4'],['i1','i3'],['i2','i3'],['i1','i3'],['i1','i2','i3','i5'],['i1','i2','i5']]


# ls = [['i1','i2','i5'],['i2','i4','i4','i5'],['i2','i3','i5'],['i1','i2','i4','i4'],['i1','i3'],['i2','i3'],['i1','i3'],['i1','i2','i3','i5'],['i1','i2','i3']]

def filterUniqueElementFromList(lss,support_count):

    frequent_elt_count = []
    ulist = []
    count = []
    freuent_st = []
    for i in lss:
        l = len(i)
        for j in range(0,l):
            if i[j] not in ulist:
                ulist.append(i[j])
                count.append(1)
            else:
                m = ulist.index(i[j])
                count[m] = count[m] + 1
    n = len(count)

    for i in range(0,n):
        if count[i] >= support_count:
            freuent_st.append(ulist[i])
            frequent_elt_count.append(count[i])
    return freuent_st, frequent_elt_count


def permu(xs):
    if xs:
        r , h = [],[]
        for x in xs:
            if x not in h:
                ts = xs[:]; ts.remove(x)
                for p in permu(ts):
                    r.append([x]+p)
            h.append(x)
        return r
    else:
        return [[]]



def checkduplicacy(ls, ms,fr_st):
    apnd_list = (ls + ms)
    perm = permu(apnd_list)
    for i in perm:
        if i in fr_st:
            return False
    return True



def findJoinSet(ls,lss):
    fr_set = []
    for i in ls:
        for j in lss:
            n = len(j)
            for k in range (0,n):
               if j[k] not in i:
                   if checkduplicacy(i,[j[k]],fr_set) == True:

                       fr_set.append(i + [j[k]])
    return fr_set


def findFrequentSet(candidate_set,data,support_count):
#    print "candidate set is",candidate_set,"\n"
#    print "data set is ",data
    final_count = []
    count = []
    frqnt_set = []
    for i in candidate_set:
        n = len(i)
        cnt = 0
        for j in data:
            m = len(j)
            if m >= n:
               a = set(i)
               b = set(j)
               if a.issubset(b) == True:
                   cnt = cnt + 1
        count.append(cnt)
#    print "count is",count
    k = len(count)
#    print "k is ",k
    for i in range(0,k):
        if count[i] >= support_count:
            frqnt_set.append(candidate_set[i])
            final_count.append(count[i])
    return frqnt_set ,final_count






def findUnionOfFrequentSet(freqnt_st,data,support_count,final_count):
    print " hi hr",freqnt_st
    output_frequent_set = []
    candidate_set_list = []
    frrqnt_st = map(lambda x: freqnt_st[1*x:(x+1)*1],range(len(freqnt_st)))
    print "frrqnt set is ",frrqnt_st
    while frrqnt_st != []:
#        print "in while"
        output_frequent_set.append(frrqnt_st)
#        print "local output is",output_frequent_set
#        frrqnt_st = []
        
        candidate_set = findJoinSet(frrqnt_st,frrqnt_st)
#        print "local candidate set is",candidate_set
        candidate_set_list.append(candidate_set)

        frrqnt_st,count_list = findFrequentSet(candidate_set,data,support_count)
        final_count.append(count_list)

#        candidate_set = []

    return output_frequent_set,final_count
    


if __name__ == "__main__":
    support_count = int(sys.argv[1])

#    file_pointer = open('/home/vaibhav/Desktop/ai/groceries.csv', 'r')

 #   data = file_pointer.readlines()
#    data = map(lambda x : (x.strip('\n')).split(','), data)
    input_data_len = len(daata)
    final_count = []
    frequent_set, count_list = filterUniqueElementFromList(daata,support_count)
    final_count.append(count_list)
    output_list,output_count = findUnionOfFrequentSet(frequent_set,daata,support_count,final_count)

    print "final output is", output_list
    print "final output_count",output_count
