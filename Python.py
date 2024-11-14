#!c:\Python\python.exe
import cgi
import mysql.connector
print("connect-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Welcome</h1>")
#connecting to frontend to backend
form=cgi.FieldStorage()
name=form.getvalue("name")
mail=form.getvalue("mailid")
passw=form.getvalue("password")
print("<h1>",name,"</h1>")
print("<h1>",mail,"</h1>")
print("<h1>",passw,"</h1>")