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



print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Finding Easter </title> </head>')
print('<body>')
print('<h2>')
print("Easter will fall on the %s of %s %s" % (p, n, y))
print('</h2>')
print('</body>')
print('</html>')








