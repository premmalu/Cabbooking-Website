#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn=pymysql.connect(host="localhost",user="root",password="",database="ridesharer")
cur=conn.cursor()
f = cgi.FieldStorage()      #Getting the data from database.
id = f.getvalue("id")       #Getting the  id.

q ="""select * from sregistoration where id = %s"""%(id)

cur.execute(q)
r = cur.fetchone()
#HTML and CSS
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
<h1>Welcome %s</h1>
<table>
<tr><td><img src = "images/%s" width = "100" height = "100"><b>profile</b></td></tr>
<tr><td><img src = "images/%s" width = "100" height = "100"><b>aadhar card</b></td></tr>
<tr><td><img src = "images/%s" width = "100" height = "100"><b>licence</b></td></tr>
<tr><td><b>Id</b>: %s</td><tr>
<tr><td><b>Username</b>: %s</td><tr>
<tr><td><b>Email</b>: %s</td><tr>
<tr><td><b>Password</b> : %s</td><tr>
<tr><td><b>Contact</b> : %s</td><tr>
<tr><td><b>Gender</b> : %s</td><tr>
<tr><td><b>Dob</b> : %s</td><tr>
<tr><td><b>Address</b> : %s</td><tr>
<tr><td><b>Distric</b> : %s</td><tr>
<tr><td><b>State</b> : %s</td><tr>
<tr><td><b>Vehicle Type</b> : %s</td><tr>
</table>
</body>
</html>
""" %(r[2],r[12],r[13],r[14],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11]))
