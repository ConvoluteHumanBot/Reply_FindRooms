import numpy
import operator

class event():
    def __init__(self,name,start,end,people):
        self.name=name
        self.start=start
        self.end=end
        self.people=people
        self.score=0

class room():
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.lbound=0

def retrieve(E,rooms):
    for i,R in enumerate(rooms):
        if E.people <= R.size and E.people>R.lbound:
            return i

def main():

    """ OBTAIN DATA FROM FILE """

    f=open('data_5000_10.in','r')
    f2=open('output.txt','w+')
    data=f.readline()
    n_events=int(data.split()[0])
    data=f.readlines()
    events=[]
    rooms=[]
    for line in data[:n_events]:
        sname=line.split()[0]
        startt=int(line.split()[1])
        endt=int(line.split()[2])
        npeople=int(line.split()[3])
        E=event(sname,startt,endt,npeople)
        events.append(E)
    for line in data[n_events:]:
        sname=line.split()[0]
        ssize=int(line.split()[1])
        R=room(sname,ssize)
        rooms.append(R)
    """ DATA ACQUIRED """
    rooms=sorted(rooms,key=operator.attrgetter('size'))
    buffer=0
    for R in rooms:
        R.lbound=buffer
        buffer=R.size
    schedule=[[] for x in range(len(rooms))]
    for E in events:
        if (E.people<=buffer and E.people>0):
            schedule[retrieve(E,rooms)].append(E)
    for i,table in enumerate(schedule):
        if not table:
            continue
        table=sorted(table,key=operator.attrgetter('start'))
        f2.write('%s:' % rooms[i].name )
        for E in table:
            E.score=int(E.people*(E.end-E.start))
        E1=table[0]
        for E in table:
            if E.start>=E1.end:
                f2.write('%s '% E1.name)
                E1=E
            if E.score>E1.score and E.start<E1.end:
                E1=E
        f2.write('%s'% E1.name)
        f2.write('\n')
    f2.close()
    f.close()
    print('Done')
main()

