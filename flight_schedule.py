#coding: utf-8

earliest_time = 600/100*60
latest_time = 2200/100*60
time = earliest_time
D = [360,360]
H = [360,360,360]
temp2 = 0
temp1 = 0
print ("tail_number,origin,destination,departure_time,arrival_time")
class Airport:
    def __init__(self, name,min_time,gates,landed_aircraft,permission_time):
        self.name = name
        self.min_time = min_time
        self.gates = gates
        self.landed_aircraft = landed_aircraft
        self.permission_time = permission_time
    def landedaircraft_number(self,a):
        if a == 1:
            self.landed_aircraft += 1
        elif a == -1:
            self.landed_aircraft -= 1
    def permissiontime_set (self,t):
        global temp2,temp1
        if self.name == "AUS":
            self.permission_time = t + self.min_time
        if self.name == "DAL":
            self.permission_time = min(D)
            D[temp1 % 2] = t +self.min_time
            temp1 += 1
        if self.name == "HOU":
            self.permissioin_time = min(H)
            H[temp2 % 3] = t + self.min_time
            temp2 += 1

def flighttime(a,b): 
    global flight_time
    if (a.name == "AUS" and b.name == "DAL") or (b.name == "AUS" and a.name == "DAL"):
        flight_time = 50
    elif (a.name == "AUS" and b.name == "HOU") or (b.name == "AUS" and a.name == "HOU"):
        flight_time = 45
    elif (a.name == "DAL" and b.name == "HOU") or (b.name == "DAL" and a.name == "HOU"):
        flight_time = 65

def military_time(n):
    a = int(n)//60*100+int(n)%60
    return '%04d' % a

AUS = Airport("AUS",25,1,1,latest_time)
DAL = Airport("DAL",30,2,2,earliest_time)
HOU = Airport("HOU",35,3,3,earliest_time)
class Aircraft:
    def __init__(self,tail_num,origin,destination,departure_time,arrival_time):
        self.tail_num = tail_num
        self.origin = origin
        self.departure_time = departure_time
        self.destination = destination
        self.arrival_time = arrival_time
    def destination_choose(self,t):
        if self.origin.name == "AUS":
            flighttime(AUS,HOU)
            self.arrival_time = t + flight_time
            if not (HOU.gates <= HOU.landed_aircraft and self.arrival_time <= HOU.permission_time):
                self.destination = HOU
            else:
                flighttime(AUS,DAL)
                self.arrival_time = t + flight_time 
                if not (self.arrival_time <= DAL.permission_time and DAL.gates <= DAL.landed_aircraft):
                    self.destination = DAL
        elif self.origin.name == "DAL":
            flighttime(HOU,DAL)
            self.arrival_time = t + flight_time
            if not (HOU.gates <= HOU.landed_aircraft and self.arrival_time <= HOU.permission_time):
                self.destination = HOU
            else:
                flighttime(DAL,AUS)
                self.arrival_time = t + flight_time 
                if not (self.arrival_time <= AUS.permission_time and AUS.gates <= AUS.landed_aircraft):
                    self.destination = AUS
        elif self.origin.name == "HOU":
            flighttime(AUS,HOU)
            self.arrival_time = t + flight_time
            if not (AUS.gates <= AUS.landed_aircraft and self.arrival_time <= AUS.permission_time):
                self.destination = AUS
            else:
                flighttime(DAL,HOU)
                self.arrival_time = t + flight_time 
                if not (self.arrival_time <= DAL.permission_time and DAL.gates <= DAL.landed_aircraft):
                    self.destination = DAL

T1 = Aircraft("T1",AUS,AUS,earliest_time,earliest_time + AUS.min_time)    
T2 = Aircraft("T2",DAL,DAL,earliest_time,earliest_time + DAL.min_time)
T3 = Aircraft("T3",DAL,DAL,earliest_time,earliest_time + DAL.min_time)
T4 = Aircraft("T4",HOU,HOU,earliest_time,earliest_time + HOU.min_time)
T5 = Aircraft("T5",HOU,HOU,earliest_time,earliest_time + HOU.min_time)
T6 = Aircraft("T6",HOU,HOU,earliest_time,earliest_time + HOU.min_time)

while time < latest_time:
    if time == T1.departure_time:
        T1.destination_choose(time)
        if T1.destination == T1.origin:
            T1.departure_time += 1
            if T1.origin.permission_time == time:
                T1.origin.permission_time += 1
        else:
            airport1 = T1.origin
            airport1.landedaircraft_number(-1)
            airport2 = T1.destination
            airport2.landedaircraft_number(1)
            flighttime(airport1,airport2)
            T1.arrival_time = T1.departure_time + flight_time
            airport2.permissiontime_set(T1.arrival_time)
            if T1.arrival_time > latest_time:
                pass
            else:
                print ('T1',',',airport1.name,',',airport2.name,',',military_time(T1.departure_time),',',military_time(T1.arrival_time))
    elif time == T1.arrival_time:
        T1.origin = T1.destination
        airport = T1.origin
        T1.departure_time = time + airport.min_time
    if time == T2.departure_time:
        T2.destination_choose(time)
        if T2.destination == T2.origin:
            T2.departure_time += 1
            if T2.origin.permission_time == time:
                T2.origin.permission_time += 1
        else:   
            airport1 = T2.origin
            airport1.landedaircraft_number(-1)
            airport2 = T2.destination
            airport2.landedaircraft_number(1) 
            flighttime(airport1,airport2)
            T2.arrival_time = T2.departure_time + flight_time 
            airport2.permissiontime_set(T2.arrival_time)
            if T2.arrival_time > latest_time:
                pass
            else:
                print ('T2',',',airport1.name,',',airport2.name,',',military_time(T2.departure_time),',',military_time(T2.arrival_time))
      
    elif time == T2.arrival_time:
        T2.origin = T2.destination
        airport = T2.origin
        T2.departure_time = time + airport.min_time
    if time == T3.departure_time:
        T3.destination_choose(time)
        if T3.destination == T3.origin:
            T3.departure_time += 1
            if T3.origin.permission_time == time:
                T3.origin.permission_time += 1
        else:
            airport1 = T3.origin
            airport1.landedaircraft_number(-1) 
            airport2 = T3.destination
            airport2.landedaircraft_number(1) 
            flighttime(airport1,airport2)
            T3.arrival_time = T3.departure_time + flight_time
            airport2.permissiontime_set(T3.arrival_time) 
            if T3.arrival_time > latest_time:
                pass
            else:
                print ('T3',',',airport1.name,',',airport2.name,',',military_time(T3.departure_time),',',military_time(T3.arrival_time))
      
    elif time == T3.arrival_time:
        T3.origin = T3.destination
        airport = T3.origin
        T3.departure_time = time + airport.min_time
    if time == T4.departure_time:
        T4.destination_choose(time)
        if T4.destination == T4.origin:
            T4.departure_time += 1
            if T4.origin.permission_time == time:
                T4.origin.permission_time += 1
        else:
            airport1 = T4.origin
            airport1.landedaircraft_number(-1) 
            airport2 = T4.destination
            airport2.landedaircraft_number(1)
            flighttime(airport1,airport2)
            T4.arrival_time = T4.departure_time + flight_time
            airport2.permissiontime_set(T4.arrival_time)
            if T4.arrival_time > latest_time:
                pass
            else:
                print ('T4',',',airport1.name,',',airport2.name,',',military_time(T4.departure_time),',',military_time(T4.arrival_time))
     
    elif time == T4.arrival_time:
        T4.origin = T4.destination
        T4.departure_time = time + T4.origin.min_time
    if time == T5.departure_time:
        T5.destination_choose(time)
        if T5.destination == T5.origin:
            T5.departure_time += 1
            if T5.origin.permission_time == time:
                T5.origin.permission_time += 1
        else:
            airport1 = T5.origin
            airport1.landedaircraft_number(-1) 
            airport2 = T5.destination
            airport2.landedaircraft_number(1) 
            flighttime(airport1,airport2)
            T5.arrival_time = T5.departure_time + flight_time
            airport2.permissiontime_set(T5.arrival_time)
            if T5.arrival_time >= latest_time:
                pass
            else:
                print ('T5',',',airport1.name,',',airport2.name,',',military_time(T5.departure_time),',',military_time(T5.arrival_time))
     
    elif time == T5.arrival_time:
        T5.origin = T5.destination
        T5.departure_time = time + T5.origin.min_time
    if time == T6.departure_time:
        T6.destination_choose(time)
        if T6.destination == T6.origin:
            T6.departure_time += 1
            if T6.origin.permission_time == time:
                T6.origin.permission_time += 1
        else:
            airport1 = T6.origin
            airport1.landedaircraft_number(-1) 
            airport2 = T6.destination
            airport2.landedaircraft_number(1) 
            flighttime(airport1,airport2)
            T6.arrival_time = T6.departure_time + flight_time
            airport2.permissiontime_set(T6.arrival_time)
            if T6.arrival_time >= latest_time:
                pass
            else:
                print ('T6',',',airport1.name,',',airport2.name,',',military_time(T6.departure_time),',',military_time(T6.arrival_time))
     
    elif time == T6.arrival_time:
        T6.origin = T6.destination
        T6.departure_time = time + T6.origin.min_time
    time += 1
