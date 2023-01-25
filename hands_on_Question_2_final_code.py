class Employee:
    def __init__(self,*arg): 
        self.name = arg[0] 
        self.desi = arg[1] 
        self.salary = arg[2] 
        self.timecon = arg[3] 
        self.timestat = False 
class Organization: 
    def overTime(self,eobjs,threshold): 
        overtimeemp = [] 
        for i in eobjs: 
            if sum(i.timecon.values()) >= threshold: 
                i.timestat = True 
                overtimeemp.append((i.name,i.timestat)) 
        return overtimeemp 
    def salcal(self,eobjs,rate): 
        sal = 0 
        for i in eobjs: 
            if i.timestat: 
                sal += sum(i.timecon.values())*rate 
        return sal 
n1 = int(input()) 
objs = [] 
for i in range(n1): 
    d = {} 
    name = input() 
    desi = input() 
    sal = int(input()) 
    n2 = int(input()) 
    for j in range(n2): 
        k = input() 
        v = int(input()) 
        d[k]=v 
    obj = Employee(name,desi,sal,d) 
    objs.append(obj)
threshold = int(input())
rate = int(input()) 
oobj = Organization() 
otemps = oobj.overTime(objs,threshold) 
otsal = oobj.salcal(objs,rate) 
for i in otemps: 
    print(i[0],i[1]) 
print(otsal)