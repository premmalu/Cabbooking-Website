#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
f = cgi.FieldStorage()      #Getting the data from Fieldstorage.
sid = f.getvalue("sid")     #Getting the in from database.
q = """select * from newsharer where accept='new'"""
cur.execute(q)
r = cur.fetchall()
cnt = 0
if sid != None:
    q1 = """update sregistoration set accept='Verified' where id=%s""" % (sid)
    cur.execute(q1)
    conn.commit()
    print("""
        <script>
          alert("Request accepted");
          location.href="customer.py";
          </script>
         """)
conn.close()

