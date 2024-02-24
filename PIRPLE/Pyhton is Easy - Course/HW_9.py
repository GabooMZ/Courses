# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:44:08 2020

@author: Gabriel Melendez
"""

#%%

'''

HW_9_Pirple 

Classes

by Gabriel M
'''

class Vehicle:
    def __init__(self, Make, Model, Year, Weight, TripsSinceMaintenance = 0, NeedsMaintenance = False):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
        if self.TripsSinceMaintenance >= 100 or self.NeedsMaintenance != False:
            self.NeedsMaintenance = True
        else:
            self.NeedsMaintenance = False
            self.TripsToMaintenance =   100 - self.TripsSinceMaintenance

        
class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, TripsSinceMaintenance = 0, NeedsMaintenance = False):
        Vehicle.__init__(self,Make, Model, Year, Weight, TripsSinceMaintenance, NeedsMaintenance)
        self.isDriving = False
        
    def Drive(self):
        if self.NeedsMaintenance == True:
            print('Your',self.Make, self.Model,' needs Maintenance')
        if self.isDriving == False:
            self.isDriving = True
            print('Youre Driving your',self.Make, self.Model,)
        else:
            print('Your',self.Make, self.Model,'is already Driving')
    
    def Stop(self):
        if self.isDriving == True:
            self.TripsSinceMaintenance += 1
            self.isDriving = False
            print('Your',self.Make, self.Model,'is Stopped')
        else:
            print('Your',self.Make, self.Model,'is already stopped')
            
        if self.TripsSinceMaintenance >= 100 or self.NeedsMaintenance != False:
            self.NeedsMaintenance = True
        else:
            self.NeedsMaintenance = False
            self.TripsToMaintenance =   100 - self.TripsSinceMaintenance
        if self.NeedsMaintenance == True:
            print('Your',self.Make, self.Model,'needs Maintenance')
       
    def RepairCar(self):
        print('You repaired your',self.Make, self.Model,'\n')
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
        self.TripsToMaintenance =  100 - self.TripsSinceMaintenance
        
    def __str__(self):
        if self.NeedsMaintenance == False:
            return ('\nYour Vehicle is a '+self.Make+' model '+self.Model+' Year '+self.Year+' and weights '+self.Weight+'\nand does not need maintenance until '+str(self.TripsToMaintenance)+' more drives\n') 
        else:
            return ('\nYour Vehicle is a '+ self.Make +' model ' + self.Model + ' Year '+ self.Year + ' and weights ' + self.Weight+'\nand needs maintenance\n')
        
class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight, TripsSinceMaintenance = 0, NeedsMaintenance = False):
        Vehicle.__init__(self,Make, Model, Year, Weight, TripsSinceMaintenance, NeedsMaintenance)
        self.isFlying = False
        
    def Fly(self):
        if self.NeedsMaintenance == True:
            print('Your',self.Make, self.Model,' needs Maintenance')
        if self.isFlying == False:
            self.isFlying = True
            print('Youre Flying your',self.Make, self.Model,)
        else:
            print('Your',self.Make, self.Model,'is already Driving')
    
    def Land(self):
        if self.isFlying == True:
            self.TripsSinceMaintenance += 1
            self.isFlying = False
            print('Your',self.Make, self.Model,'is landed')
        else:
            print('Your',self.Make, self.Model,'is already landed')
            
        if self.TripsSinceMaintenance >= 100 or self.NeedsMaintenance != False:
            print('The Plane can not fly until it is repaired')
            self.NeedsMaintenance = True
            
    def __str__(self):
        if self.NeedsMaintenance == False:
            return ('\nYour Plane is a '+self.Make+' model '+self.Model+' Year '+self.Year+' and weights '+self.Weight+'\nand does not need maintenance until '+str(self.TripsToMaintenance)+' more flights\n') 
        else:
            return ('\nYour Plane is a '+ self.Make +' model ' + self.Model + ' Year '+ self.Year + ' and weights ' + self.Weight+'\nand needs maintenance\n')
        
##Testing##
            
        
MyCar1 = Cars('Nissan', 'A01', '2005', '700kg', 80)####

print(MyCar1)

MyCar1.Stop()

MyCar1.Drive()

MyCar1.Stop()

print(MyCar1)

MyCar2 = Cars('Volvo', 'S40', '2004', '750kg', 0, True)####2

print(MyCar2)

MyCar2.RepairCar()

print(MyCar2)

MyCar3 = Cars('Chevrolet', 'Grand Cherokee', '1994', '1ton',98)####3

print(MyCar3)

MyCar3.Drive()

MyCar3.Stop()

MyCar3.Drive()

MyCar3.Stop()

print(MyCar3)

MyCar3.RepairCar()

print(MyCar3)

MyPlane = Planes('Boeing', '777', '1994', '150tons', 99)

print(MyPlane)

MyPlane.Fly()

MyPlane.Land()

print(MyPlane)