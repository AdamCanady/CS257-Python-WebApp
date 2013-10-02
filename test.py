#!/usr/bin/python

''' Code from Jeff Ondich's class '''

import cgi

# Get the user input
form = cgi.FieldStorage()
if form.has_key('animal') and form['animal'].value:
	animal = form['animal'].value
if form.has_key('badanimal') and form['badanimal'].value:
	badAnimal = form['badanimal'].value
# ***** SANITIZE USER INPUT HERE ****

output = '''<DOCTYPE HTML>
<html>
<head>
    <title>Tiny web app results</title>
</head>

<body>
    <p>I like %ss, too.</p>
    <p>Also, %ss are gross.</p>
</body>
</html>''' % (animal, badAnimal)

print "Content-type: text/html\r\n\r\n"
print output
