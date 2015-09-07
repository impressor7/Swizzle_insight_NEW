'''
The way to write something on file using python
'''

f = open('practice.html', 'w')

message = """ <html>
<head></head>
<body><p>Hello World!</p></body>
</html> print('hello world')"""


f.write(message)
f.close()


import cgi, cgitb
cgitb.enable(display=0,logdir = '1.html')

form = cgi.FieldStorage()
