# -*- coding: utf-8 -*-
"""Simple_Arbitrage_Betting_Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qHRBvVuj_xEBLywFOAcafWOGqiW_Q_PH

Gets the user input for the odds
"""

print("Betting platform 1:")
o1 = float(input("Enter team one odds: "))
o2 = float(input("Enter draw odds: "))
o3 = float(input("Enter team two odds: "))

print("\nBetting platform 2:")
o4 = float(input("Enter team one odds: "))
o5 = float(input("Enter draw odds: "))
o6 = float(input("Enter team two odds: "))

print("\nBetting platform 3:")
o7 = float(input("Enter team one odds: "))
o8 = float(input("Enter draw odds: "))
o9 = float(input("Enter team two odds: "))

r1 = ((1 / o1) + (1 / o2) + (1 / o3)) * 100;
r2 = ((1 / o4) + (1 / o5) + (1 / o6)) * 100;
r3 = ((1 / o7) + (1 / o8) + (1 / o9)) * 100;
r4 = ((1 / o1) + (1 / o5) + (1 / o9)) * 100;
r5 = ((1 / o3) + (1 / o5) + (1 / o7)) * 100;
r6 = ((1 / o1) + (1 / o5) + (1 / o6)) * 100;
r7 = ((1 / o1) + (1 / o8) + (1 / o9)) * 100;
r8 = ((1 / o5) + (1 / o6) + (1 / o7)) * 100;
r9 = ((1 / o2) + (1 / o3) + (1 / o7)) * 100;
r10 = ((1 / o1) + (1 / o5) + (1 / o3)) * 100;
r11 = ((1 / o1) + (1 / o8) + (1 / o3)) * 100;
r12 = ((1 / o7) + (1 / o5) + (1 / o9)) * 100;
r13 = ((1 / o7) + (1 / o2) + (1 / o9)) * 100;
r14 = ((1 / o7) + (1 / o2) + (1 / o6)) * 100;
r15 = ((1 / o1) + (1 / o8) + (1 / o6)) * 100;
r16 = ((1 / o4) + (1 / o2) + (1 / o9)) * 100;
r17 = ((1 / o4) + (1 / o8) + (1 / o6)) * 100;
r18 = ((1 / o4) + (1 / o8) + (1 / o3)) * 100;
r19 = ((1 / o4) + (1 / o2) + (1 / o3)) * 100;

print('num\t' + 'odd\t' + 'odd\t' + 'odd\t' + 'probability\n')

if r1 < 100 :
  print('1\t' + str(o1) + '\t' + str(o2) + '\t' + str(o3) + '\t' + str(r1) + '\n')

if r2 < 100 :
  print('2\t' + str(o4) + '\t' + str(o5) + '\t' + str(o6) + '\t' + str(r2) + '\n')

if r3 < 100 :
  print('3\t' + str(o7) + '\t' + str(o8) + '\t' + str(o9) + '\t' + str(r3) + '\n')

if r4 < 100 :
  print('4\t' + str(o1) + '\t' + str(o5) + '\t' + str(o9) + '\t' + str(r4) + '\n')

if r5 < 100 :
  print('5\t' + str(o3) + '\t' + str(o5) + '\t' + str(o7) + '\t' + str(r5) + '\n')

if r6 < 100 :
  print('6\t' + str(o1) + '\t' + str(o5) + '\t' + str(o6) + '\t' + str(r6) + '\n')

if r7 < 100 :
  print('7\t' + str(o1) + '\t' + str(o8) + '\t' + str(o9) + '\t' + str(r7) + '\n')

if r8 < 100 :
  print('8\t' + str(o5) + '\t' + str(o6) + '\t' + str(o7) + '\t' + str(r8) + '\n')

if r9 < 100 :
  print('9\t' + str(o2) + '\t' + str(o3) + '\t' + str(o7) + '\t' + str(r9) + '\n')

if r10 < 100 :
  print('10\t' + str(o1) + '\t' + str(o5) + '\t' + str(o3) + '\t' + str(r10) + '\n')

if r11  < 100 :
  print('11\t' + str(o1) + '\t' + str(o8) + '\t' + str(o3) + '\t' + str(r11) + '\n')

if r12 < 100 :
  print('12\t' + str(o7) + '\t' + str(o5) + '\t' + str(o9) + '\t' + str(r12) + '\n')

if r13 < 100 :
  print('13\t' + str(o7) + '\t' + str(o2) + '\t' + str(o9) + '\t' + str(r13) + '\n')

if r14 < 100 :
  print('14\t' + str(o7) + '\t' + str(o2) + '\t' + str(o6) + '\t' + str(r14) + '\n')

if r15 < 100 :
  print('15\t' + str(o1) + '\t' + str(o8) + '\t' + str(o6) + '\t' + str(r15) + '\n')

if r16 < 100 :
  print('16\t' + str(o4) + '\t' + str(o2) + '\t' + str(o9) + '\t' + str(r16) + '\n')

if r17 < 100 :
  print('17\t' + str(o4) + '\t' + str(o8) + '\t' + str(o6) + '\t' + str(r17) + '\n')

if r18 < 100 :
  print('18\t' + str(o4) + '\t' + str(o8) + '\t' + str(o3) + '\t' + str(r18) + '\n')

if r19 < 100 :
  print('19\t' + str(o4) + '\t' + str(o2) + '\t' + str(o3) + '\t' + str(r19) + '\n')