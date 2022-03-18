# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:40:14 2022

@author: Asus
"""
def Sec2Day (t):
    return (t/60/60/24)
print(Sec2Day(43200))

def BoxVolume (a , b , c):
    return(a*b*c)
print(BoxVolume(2 , 3 , 4))

def Displacement (a , t, u):
    return (u*t + 1/2*a*t**2)
print(Displacement(4 , 10, 0))

def SurfaceArea (a, b, c):
    return (a*b*2 + b*c*2 + a*c*2)
print(SurfaceArea(1,1,1))
