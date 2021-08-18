#!C:/Users/YourName/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")
# impoting the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
# this is HTML and CSS.
print("""
<html>
<head>
<title>Forget Password</title>
</head>
<body>
<center>
<h3>Forget Password</h3>
    <form method = "post" action = "#">
        Username:
        <input type = "text" name = "username"><br><br>
        <input type = "submit" value = "OK" name = "submit"> <input type ="button" value ="cancel" onclick = "location.href = 'adminlogin.py'">
        </form>
        </center>
        </body>
        </html>""")

conn = pymysql.connect(host = "localhost",user="root",password = "",database="ridesharer")          #Connecting to phpmysql using Xampp database.
cur = conn.cursor()

f = cgi.FieldStorage()                  #Fetching entered data
username = f.getvalue("username")       #Fetching the username.
v = f.getvalue("submit")                #On click the fetched data send to mail is initiated

if v != None:
    q = """select password ,email from adminlogin where username = '%s'"""%(username)
    cur.execute(q)
    r = cur.fetchone()          #validating the entered username with database name for sequrity.

    if r[0] != None:
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        sender_address = '#Enter your mail id'
        sender_pass = '#Enter your mail password'
        to_address = r[1]
        msg = """
            hi Welcome %s,
                password : %s
            """%(username,r[0])

        receiver_address = to_address           #This is  recever address from admin mail
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'New Password'
        message.attach(MIMEText(msg, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address,sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail sent')
        print("""
            <script>
            alert("Please check your mail");
            </script>
            """)
