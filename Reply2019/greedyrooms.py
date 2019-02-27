import numpy
import operator

class event():
    def __init__(self,name,start,end,people):
        self.name=name
        self.start=start
        self.end=end
        self.people=people
        self.score=people*(end-start)

class room():
    def __init__(self,name,size):
        self.name=name
        self.size=size

def retrieve(E,rooms):
    for i,R in enumerate(rooms):
        if E.people <= R.size and E.people>R.lbound:
            return i

def main():

    """ OBTAIN DATA FROM FILE """

    f=open('data_50000_10.in','r')
    f2=open('output2.txt','w+')
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
    events=sorted(events,key=operator.attrgetter('people'))
    schedule=[[] for x in range(len(rooms))]
    garbage=[]
    for i,table in enumerate(schedule):
        for E in events:
            if (E.people!=0 and E.people<=rooms[i].size):
                table.append(E)
        if not table:
            continue
        table=sorted(table,key=operator.attrgetter('start'))
        f2.write('%s:' % rooms[i].name )
        E1=table[0]
        for E in table:
            if E.start>=E1.end and (E not in garbage):
                f2.write('%s '% E1.name)
                E1=E
                garbage.append(E)
            elif E.score>E1.score and (E not in garbage):
                E1=E
                garbage.append(E)
        f2.write('%s'% E1.name)
        f2.write('\n')
    f2.close()
    f.close()
    print('Done')
main()

