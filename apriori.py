def calfreq(s1):
        freq = 0 
        for j in data:
                if s1 == s1.intersection(j):
                        freq = freq+1
        return freq

def removelessthanminsup():
        list = []
        for i in items:
                if calfreq(i) >= minsup:
                        list.append(i)
        return list 
                        

def makenewsets(size):
        list = []
        for i in items:
                for j in items:
                        temp = i.union(j)
                        if len(temp) == size:
                                if temp not in list:
                                        list.append(temp)
        return list

minsup = int(input("Enter the minimum support: "))
c = 1
items = [set([1]),set([2]),set([3]),set([4]),set([5]),set([6])]
data = [set([1,2,3]),set([5,2,4]),set([1,5,2,4]),set([5,4]),set([6])]
items = removelessthanminsup()
while(len(items) > 1):
        c = c+1
        items = makenewsets(c)
        items = removelessthanminsup()
print(items)






