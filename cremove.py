#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn=pymysql.connect(host="localhost",user="root",password="",database="ridesharer")
cur=conn.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
rid=f.getvalue("rid")   #This delets the data from database.
q=""" delete from cregistoration where id='%s'"""%(rid)
cur.execute(q)
conn.commit()
print("""
    <script>
        location.href="customer.py?id=%s";
        alert("removed successfully");
    </script>"""%(id))
conn.close()

