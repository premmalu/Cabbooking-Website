#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi,pymysql,cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host = "localhost",user="root",password = "",database="ridesharer")
cur = conn.cursor()
q1= """ select max(id) from newclient """
cur.execute(q1)
r=cur.fetchone()
if r[0] != None:
    n=r[0]
else:
    n=0
z=""
if n<10:
    z="000"
elif n<100:
    z="00"
elif n<1000:
    z="0"
else:
    z=""
shid="id" + z + str(n+1)
#HTML and CSS.
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client registoration</title>
    <style>
        body{
            text-align:left;
            padding-left: 40%;
            padding-top:10%;
            background-image:url("images/customer.jfif") ;
            
            overflow:visible;
        }
        form{
            background: lightcoral;
            width: 30%;
            padding:10px 50px ;
            border-radius: 20px;
        }
        .container{
            align-items: center;
        }
        a{
            text-decoration: none;
            color: black;
        }
    </style>
</head>
""")
print("""
<body>
    <h1>Client registoration</h1>
  <div class="container">  
    <form method = "post" action = "#" enctype = "multipart/form-data" autocomplete="on">
        <label for="shid">Seekerid:</label>
        <input type="text" name="shid" value="%s" readonly><br><br>
        <label for="name">Name:</label>
        <input type="text" id = "name" name="name" placeholder="Enter your name"><br><br>
        <label for="email">Email-id:</label>
        <input type="email" id = "email" name="email" placeholder="Enter your email"><br><br>
        <label for="contact">Contact:</label>
        <input type="tel" id = "contact" name="contact" placeholder="Enter your contact-number"><br><br>
        <p>Gender:</p>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label>
        <input type="radio" id="others" name="gender" value="others">
        <label for="others">Others</label><br><br>
        <label for="dob">DOB:</label>
        <input type="text" id = "dob" name="dob" placeholder="Enter your DOB"><br><br>
        <label for="address">Address</label>
        <input id = "address" name="address" placeholder="Enter your address" rows="6" cols="30"></input><br><br>
        <label for="username">Username:</label>
        <input type="text" id = "username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id = "password" name="password"><br><br>
        <label for="profile">Profile:</label>
        <input type="file" id = "profile" name="profile"><br><br>
        <button type="submit" name = "reg" id = "reg">Register</button>
        <button type="submit"><a href="mainpage.py">Cancel</a></button><br><br>
        <a href="Cloggin.py">Existing user click here to loggin? </a>
    </form>
  </div>
</body>
</html>
"""%(shid))
f = cgi.FieldStorage()
sub = f.getvalue("reg")
if sub !=None:      #Pushing datas into database
    shid=f.getvalue("shid")
    name=f.getvalue("name")
    email = f.getvalue("email")
    contact = f.getvalue("contact")
    gender = f.getvalue("gender")
    dob = f.getvalue("dob")
    address = f.getvalue("address")
    username = f.getvalue("username")
    password = f.getvalue("password")
    profile = f['profile']

    if profile != None:
        if profile.filename:
            import os

            fp = os.path.basename(profile.filename)
            open("images/" + fp, "wb").write(profile.file.read())

            q2 = """insert into cregistoration(shid,name,email,contact,gender,dob,address,username,password,profile) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(shid,name,email,contact,gender,dob,address,username,password,fp)
            cur.execute(q2)
            conn.commit()
            conn.close()

            print("""
                <script>
                    location.href = "cloggin.py"
                </script>
            """)
    else:
        print("""
            <script>
                alert("data not inserted");
                location.href = "cregistoration.py"
            </script>
        """)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = """Hello, %s
                                   USERNAME : %s,
                                   PASSWORD : %s
                            """ % (name, username, password)

sender_address = 'Mailname'
sender_pass = 'Password'
receiver_address = email
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Registration successfull '
message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail sent')