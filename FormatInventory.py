#!/usr/bin/python
import time
import sys
import os
#
#
#To run this script python > 3.6 must be installed
#Both this and the batch file must be on the Desktop
#The file entered must be a .txt
#
#
current_path = os.getcwd()
seconds = str(time.time())
seconds = seconds[:10]

path = input("Please enter the path of the .txt file (or drag it here): ")
stripchar = input("Please enter the characters you wish to strip from retail price, price, and quantity: ")


a_file = open(path)

lines = a_file.readlines()
i=-1
errors = 0
success = 0

for line in lines:
    i+=1

    #print(str(i)+ " " + line)
    #tokenize them
    tokens = line.split(',')


    #if more than six columns throw an error.
    if len(tokens)>6:
        print ("Too Many Fields: Error at " + str(i))
        print(tokens)
        errors+=1
        continue
        #if less than six columns throw error.
    if len(tokens)<6:
        print ("Incomplete: Error at " + str(i))
        print(tokens)
        errors+=1
        continue

    #sanitize
    #cuts 1st field so that its only 30 char and checks to see if it has names
    token0 = tokens[0]
    token0 = token0.strip('$%-')
    token0 = token0.replace('"', '')
    token0 = token0[:30]
    if (token0 == ''):
        token0 = 'NoName'
        print("No Name for line: " + str(i))
    tokens[0] = token0

    #makes it so 2nd field is 20char and if has a name
    token1 = tokens[1]
    token1 = token1.strip(' ')
    token1 = token1[:20]
    if (token1 == ''):
        token1 = 'NoName' + str(i)
        print("No Item Number for line: " + str(i))
    tokens[1] = token1

    #checks to see if not empty and a number
    token2 = tokens[2]
    token2 = token2.strip(stripchar)
    token2 = token2.replace(" ", "")
    token2 = token2[:30]
    if (token2 == ''):
        token2 = '0'
    tokens[2] = token2
    try:
        isfloat = float(token2)
    except ValueError:
        print ("Error at " + str(i))
        print(tokens)
        errors+=1
        continue


    token3 = tokens[3]
    token3 = token3.strip(stripchar)
    token3 = token3.replace(" ", "")
    token3 = token3[:30]
    if (token3 == ''):
        token3 = '0'
    tokens[3] = token3
    try:
        isfloat = float(token3)
    except ValueError:
        print ("Error at " + str(i))
        print(tokens)
        errors+=1
        continue

    token4 = tokens[4]
    token4 = token4.strip(stripchar)
    token4 = token4.replace(" ", "")
    token4 = token4[:30]
    if (token4 == ''):
        token4 = '0'
    tokens[4] = token4
    try:
        isfloat = float(token4)
    except ValueError:
        print ("Error at " + str(i))
        print(tokens)
        errors+=1
        continue
        # amkes dept id 8 char
    token5 = tokens[5]
    token5 = token5.replace(" ", "")
    if (token5 == '\n'):
        token5 = 'NDept'
    token5 = token5.strip(' $%-\n')
    token5 = token5[:8]
    tokens[5] = token5

    sanitzed_string = ','.join(tokens)
    sanitzed_string = sanitzed_string + ','

    success+=1

    with open(current_path + '\sanitized'+seconds+'.txt', 'a') as f:

        f.write(sanitzed_string)
        f.write('\n')

    #print(sanitzed_string)


print("Errors found: " + str(errors))
print("Successfully cleaned and placed: " + str(success))
a_file.close()
