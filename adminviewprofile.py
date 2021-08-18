#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="ridesharer")
cur=conn.cursor()
f = cgi.FieldStorage()
id = f.getvalue("id")

q ="""select * from adminlogin"""

cur.execute(q)
r = cur.fetchone()
#HTML and CSS.
print("""
<html>
<head>
<style>
*{
background-color:aqua;
}
h1{
float:left;
margin-top:30px ;
text-transform:uppercase;
font-size:60px;
font-family: 'Girassol', cursive;
}
table{
float:right;
margin-right:100px;
margin-top:80px;
}
table,tr,th,td,b{
background-color:lightgrey;
font-size:25px;
padding:15px;
}
b{
text-transform:uppercase;
}
</style>
</head>
<body>
<h1>ADMIN:</h1>
<h1>Welcome %s</h1>
<table>
<tr><td><b>Username</b>: %s</td><tr>
<tr><td><b>Email</b>: %s</td><tr>
<tr><td><b>Password</b> : %s</td><tr>   

</table>

</body>
</html>
""" %(r[1],r[1],r[2],r[3]))         #Provide this according to database created order.
