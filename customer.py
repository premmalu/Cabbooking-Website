#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
f = cgi.FieldStorage()      #Getting value from fieldstorage
id = f.getvalue("id")       #Getting the user  id
q = """select * from cregistoration"""
cur.execute(q)
r = cur.fetchall()
count=0
#HTML  and CSS
print("""
    <html>
    <head><title>Client profile</title></head>
    <style>
        body{ 
        background:url(images/simple_qnote.jpg);
        background-size:cover;
        }
        table,th,td{
        border-collapse:collapse;
        border:3px solid black;
        padding:20px;
        }
        
    </style>
    <body>
    <h1>Client Profile:</h1>
    <table border="2" width="50">
    <tr>
        <th>id</th>
        <th>Sharerid</th>
        <th>Name</th>
        <th>Email</th>
        <th>Contact</th>
        <th>Gender</th>
        <th>Dob</th>
        <th>Address</th>
        <th>Username</th>
        <th>Password</th><th>profile</th>
        <th>REMOVE</th>
        <th>CHANGE</th>
    </tr>""")
for i in r:
    count = count + 1
    print("""
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="images/%s" width="60" height="60"></td>
    <td><a href="cremove.py?rid=%s&id=%s">REMOVE</a></td>
    <td><a href="cedit.py?cid=%s&id=%s">CHANGE</a></td></tr>
    """ % (count,i[1],i[2],i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10], i[0], id, i[0], id))
conn.close()
