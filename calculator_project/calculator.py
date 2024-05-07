import turtle
import pygame
import time

def add(x, y):
	return x + y

def minus(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

#set up screen
screen = turtle.Screen() #initialize screen
screen.setup(width = 500, height = 500) #set up dimensions
screen.title("Calculator") #set up the name of the app
time.sleep(5) #check whether it works