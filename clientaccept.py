#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback
import cgi, pymysql, cgitb;cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
#connection with phpmysql using Xampp.
cur = conn.cursor()
f = cgi.FieldStorage()
sid = f.getvalue("sid")
#This informations are validated by admin and accepted.
q = """select * from newclient where accept='new'"""
cur.execute(q)
r = cur.fetchall()
cnt = 0
if sid != None:
    q1 = """update cregistoration set accept='Verified' where id=%s""" % (sid)
    cur.execute(q1)
    conn.commit()
    print("""
        <script>
          alert("Request accepted");
          location.href="customer.py";
          </script>
         """)
conn.close()

