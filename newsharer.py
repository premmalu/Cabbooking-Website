#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb;

cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
f = cgi.FieldStorage()  #Getting the data from Fieldstorage.
sid = f.getvalue("sid") #Getting the id.
q ="""select * from sregistoration where accept='new'"""
cur.execute(q)
r = cur.fetchall()
#HTML and CSS
print("""
    <html>
    <head><title>Sharer profile</title>
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
    </head>
    <body>
    <h1>Sharer Profile:</h1>
    <table border="2" width="50">
    <tr>
        <th>username</th>
        <th>email</th>
        <th>password</th>
        <th>contact</th>
        <th>gender</th>
        <th>dob</th>
        <th>address</th>
        <th>district</th>
        <th>state</th>
        <th>vehicletype</th>
        <th>profile</th>
        <th>aadharcard</th>
        <th>licence</th>
        <th>REMOVE</th>
        <th>CHANGE</th>
    </tr>""")
for i in r:
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
    <td><img src="images/%s" width="60" height="60"></td>
    <td><img src="images/%s" width="60" height="60"></td>
    <td><a href="sremove.py?rid=%s">REMOVE</a></td>
    <td><a href="shareraccept.py?sid=%s">accept</a></td></tr>
    """ % (i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[0], i[0]))
if sid!=None:
    q1="""update sregistoration set accept='Verified' where id=%s"""%(sid)
    cur.execute(q1)
    conn.commit()
    print("""
        <script>
          alert("Request accepted");
          location.href="customer.py";
          </script>
         """)
conn.close()