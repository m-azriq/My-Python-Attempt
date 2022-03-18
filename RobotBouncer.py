# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:16:19 2022

@author: Asus
"""

print("Hello! Welcome to Copa Cabana Club.")
name=input("Please write down your first and last name.\n")
if name == "Peter Parker":
    age = input("How old are you?\n")
    if age < str(18):
        print("You are not allowed to be here. Get out or I will shoot you!")
else:
    print("Welcome to the club, " + name + ". Enjoy!")
    