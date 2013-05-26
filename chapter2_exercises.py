# Exercises for chapter 2

# Name: Alex Choi

# 2.1
# When putting a "0" in front of the integer, it reads the value as an octal (base 8) number and converts it into a decimal (base 10) number.
# The value "02492" returned a syntax error because the value "9" doesn't exist in the octal numbering system.

# 2.2
# When the three statements below are run in script mode, there is no visible output.
5
x=5
x+1
# Below are the same three statements transformed into print statements.
print 5
print 'x=5'
print x+1
# An error for the third statement is outputted because x is not defined within the print statement.
# My solution to this is to define x in an expression that will not be visibly outputted:
print 5
x=5
print 'x=5'
print x+1

# 2.3
width=17
height=12.0
delimiter='.'
print width/2
# width/2 = 8
print width/2.0
# width/2.0 = 8.5
print height/3
# height/3 = 4.0
print 1+2*5
# 1+2*5 = 11
print delimiter*5
# delimiter*5 = .....

#2.4
#1
r=5
pi=3.14
print (4.0/3.0)*pi*(r**3)
# answer = 523.33
# If I don't use floats for 4 and 3, then 4/3 = 1, not 1.333 because of floor division.

#2
cover=24.95 	#cover price of a book
discount=cover*.6 	#wholesale price bookstores receive after 40% discount
totalbooks=discount*60.0 	#total wholesale cost of 60 books
totalshipping=0.75*59+3 	#total wholesale shipping cost of 60 books

print totalbooks+totalshipping
# answer = $945.45

#3
startingTime=(6*60+52)*60 		#6:52 in seconds
mileEasy=8*60+15 	#easy pace in seconds
mileTempo=7*60+12 	#tempo pace in seconds
returnTimeSec=startingTime+2*mileEasy+3*mileTempo 	#return time in seconds
print returnTimeSec
returnTimeMin=returnTimeSec/60.0	#return time in minutes
print returnTimeMin
returnTimeHour=returnTimeMin/60.0 	#return time in hours
print returnTimeHour
print returnTimeMin-7*60	#after 7 hours subtracted from return time, remaining is 30.1 minutes
print 0.1*60 	#after 30 minutes subtracted from 30.1, remaining is 0.1 minutes, which is 6 seconds
# answer = 7 hours 30 minutes 6 seconds (aka 7:30am + 6 seconds) 