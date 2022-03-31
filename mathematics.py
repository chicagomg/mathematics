#!/usr/bin/env python3
import random
import os
from num2words import num2words

n = 0
points = 50     # количество попыток
language = "ru" # язык приложения
RED='\033[1;31m'
GRN='\033[1;32m'
YEL='\033[1;33m'
BLU='\033[1;34m'
NC='\033[0m' # No Color
def main():
	global n
	if language == "en":
		plus = "plus"
		minus = "minus"
		equal = "equal"
		done = "solved"
		multiply = "multiply"
		divide = "divide"
	elif language == "pt":
		plus = "mais"
		minus = "menos"
		equal = "é igual a"
		done = "decidiu"
		multiply = "multiply"
		divide = "divide"
	elif language == "ru":
		plus = "плюс"
		minus = "минус"
		equal = "равно"
		done = "РЕШЕНО"
		multiply = "умножить на"
		divide = "поделить на"

	a = random.randint(1,50)
	b = random.randint(1,50)
	digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	action_plus = a+b
	action_minus = a-b
	action_multiply = a*b
	action_divide = a/b
	action = [action_plus, action_minus]
	c = action_plus #random.choice(action)
	if c == action_plus:
		print(YEL, num2words(a, lang=language), plus, num2words(b, lang=language), equal, NC)
		print(a, "+", b, "=")
	elif c == action_minus:
		print(YEL, num2words(a, lang=language), minus, num2words(b, lang=language), equal, NC)
		print(a, "-", b, "=")
	elif c == action_multiply:
		print(YEL, num2words(a, lang=language), multiply, num2words(b, lang=language), equal, NC)
		print(a, "*", b, "=")
	elif c == action_divide:
		print(YEL, num2words(a, lang=language), divide, num2words(b, lang=language), equal, NC)
		print(a, "/", b, "=")
	value = int(input())
	
	if n == points-1:
		os.system('cls||clear')
		print(done)
		exit(1)
	else:
		if value == c:
		  n += 1
		  os.system('cls||clear')
		  itog=num2words(n,lang=language)
		  print(GRN, itog, NC)
		  print("")
		  return(n)
		else:
		  n -= 2
		  os.system('cls||clear')
		  itog=num2words(n,lang=language)
		  print(RED, itog, NC)
		  print("")
		  return(n)

os.system('cls||clear')

while n < points:
	main()
