#!/usr/bin/python3
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()
theYear = int(form.getvalue('theYear'))
format_option = form.getvalue("format")

def Easter(y):
	a = y % 19
	b = y // 100
	c = y % 100
	d = b // 4
	e = b % 4
	g = (8 * b + 13) // 25
	h = (19 * a + b - d - g + 15) % 30
	j = c // 4
	k = c % 4
	m = (a + 11 * h) // 319
	r = (2 * e + 2 * j - k - h + m + 32) % 7
	n = (h - m + r + 90) // 25
	p = (h - m + r + n + 19) % 32
	return p,n,y

p, n, y = Easter(theYear)

def March(n):
	return "March"
def April(n):
	return "April"
def sup(p):
	if p == 1 and 21 and 31:
		return "st"
	elif p == 2 and 22:
		return "nd"
	elif p == 3 and 23:
		return "rd"
	else:
		return "th"




print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title>')
print(' Finding Easter </title>')
print('<style>')
print('body {background-color: skyblue;}')
print('h2 {font-family: verdana; text-align: center;}')
print('</style>')
print('</head>')
print('<body>')
print('<h2>')
if format_option == "numerically":
	print("Easter will fall on %s / %s / %s" % (p, n, y))
elif format_option == "verbosely":
	if n == 3:
		print('Easter will fall on the', p,"<sup>",sup(p), "</sup>", 'of', March(n), y)
	elif n == 4:
		print('Easter will fall on the', p,"<sup>",sup(p), "</sup>", 'of', April(n), y)
else:
	if n == 3:
		print('Easter will fall on the', p,"<sup>",sup(p), "</sup>", 'of', March(n), y)
	elif n == 4:
		print('Easter will fall on the', p,"<sup>",sup(p), "</sup>", 'of', April(n), y)
	print('<br>')
	print("or %s / %s / %s" % (p, n, y))
	
print('</h2>')
print('</body>')
print('</html>')








