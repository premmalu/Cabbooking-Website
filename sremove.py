#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn=pymysql.connect(host="localhost",user="root",password="",database="ridesharer")
cur=conn.cursor()
f=cgi.FieldStorage()    #Getting the data from Database.
id=f.getvalue("id")     #Getting the id from Database.
rid=f.getvalue("rid")   #Getting the registoration id.
q=""" delete from sregistoration where id='%s'"""%(rid)
cur.execute(q)
conn.commit()
print("""
    <script>
        location.href="sharer.py?id=%s";
    </script>"""%(id))
conn.close()

