# Exercises for chapter 3:

# Name: Alex Choi

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()

# 3.1
# When the last line is moved to the top, I get a Name Error message that says name 'repeat_lyrics' is not defined.

# 3.2
# I receive the same output when I run this program as I received when the definition of 'print_lyrics' was before the definition of 'repeat_lyrics'.

# 3.3
def right_justify(s):
	spacesToAdd=70-len(s)
	print ' '*spacesToAdd+s

right_justify('allen') 	#This is a test example.
right_justify('Super California') 	#This is a text example.

# 3.4
# 1.
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

# 2.
def do_twice(a):
	print a
	print a

do_twice('a') 	#This is a test example.
do_twice(17)	#This is a test example.

# 3.
def print_twice(spam):
	print spam
	print spam

print_twice('spam')

# 4.
def do_twice(spam):
	print_twice('spam')
	print_twice('spam')
do_twice('spam')

#5.
def do_four(s):
	print_twice(s)
	print_twice(s)
do_four('potato')



