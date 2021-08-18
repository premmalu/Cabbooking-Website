#!C:/Users/YourfileName/AppData/Local/Programs/Python/Python39/python.exe
# impotring the common Gateway interface,sql,cgi trackback.
print("Content-type: text/html\n")

import cgi,pymysql,cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host = "localhost",user="root",password = "",database="ridesharer")
cur = conn.cursor()
q1= """ select max(id) from sregistoration """
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
#CSS
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sharer_reg</title>
    <style>
        body{
            text-align:left;
            padding-left: 40%;
            padding-top:10%;
            background-image:url("images/taxi1.jpg") ;
            background-size: cover;
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
""")
#HTML
print("""
</head>
<body>
  <div class="container">  
    <h1>Ride Sharer Registoration</h1>
    <form method = "post" action = "#" enctype = "multipart/form-data" autocomplete="on">
        <label for="shid">Sharer_id:</label>
        <input type="text" name="shid" value="%s" readonly><br><br>
        <label for="username">Username:</label>
        <input type="text" id = "username" name="username" placeholder="Enter your name"><br><br>
        <label for="email">E-mail:</label>
        <input type="email" id = "email" name="email" placeholder="Enter your email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id = "password" name="password" placeholder="Password"><br><br>
        <label for="contact">Contact:</label>
        <input type="tel" id = "contact" name="contact" placeholder="Enter your contact-number"><br><br>
        <p>Gender:</p>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label>
        <input type="radio" id="others" name="gender" value="others">
        <label for="others">Others</label><br><br>
        <label for="dob">Dob:</label>
        <input type="text" id = "dob" name="dob" placeholder="Enter your dob"><br><br>
        <label for="address">Address</label>>
        <input id = "address" name="address" placeholder="Enter your address" rows="6" cols="30"></input><br><br>
        <label for="distric">Distric:</label>
        <input type="text" id = "distric" name="distric"><br><br>
        <label for="state">State:</label>
        <input type="text" id = "state" name="state"><br><br>
        <label for="vehicletype">Vehicle:</label>
        <input type="text" id = "vehicletype" name="vehicletype"><br><br>
        <label for="profile">Profile:</label>
        <input type="file" id = "profile" name="profile"><br><br>
        <label for="aadharcard">Aadharcard:</label>
        <input type="file" id = "aadharcard" name="aadharcard"><br><br>
        <label for="licence">Licence:</label>
        <input type="file" id = "licence" name="licence"><br><br>
        <button type="submit" name = "reg" id = "reg">Register</button>
        <button type="submit">Cancel</button><br><br>
        <a href="sh_loggin.html">Existing user click here to loggin? </a>
        </div> 
    </form>
  </div>
</body>
</html>
"""%(shid))
f = cgi.FieldStorage()
sub = f.getvalue("reg")
if sub !=None:
    shid=f.getvalue("shid")
    username = f.getvalue("username")
    email = f.getvalue("email")
    password = f.getvalue("password")
    contact = f.getvalue("contact")
    gender = f.getvalue("gender")
    dob = f.getvalue("dob")
    address = f.getvalue("address")
    distric = f.getvalue("distric")
    state = f.getvalue("state")
    vehicletype = f.getvalue("vehicletype")
    profile = f['profile']
    aadharcard = f['aadharcard']
    licence = f['licence']

    if profile != None:
        if profile.filename:
            import os

            fp = os.path.basename(profile.filename)
            open("images/" + fp, "wb").write(profile.file.read())
            fp1 = os.path.basename(aadharcard.filename)
            open("images/" + fp, "wb").write(aadharcard.file.read())
            fp2 = os.path.basename(licence.filename)
            open("images/" + fp, "wb").write(licence.file.read())
            q2 = """insert into sregistoration(shid,username,email,password,contact,gender,dob,address,distric,state,vehicletype,profile,aadharcard,licence) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(shid,username,email,password,contact,gender,dob,address,distric,state,vehicletype,fp,fp1,fp2)
            cur.execute(q2)
            conn.commit()
            conn.close()

            print("""
                <script>
                    location.href = "slogin.py";
                </script>
            """)
    else:
        print("""
            <script>
                location.href = "cregistoration.py";
                alert("data not inserted");
                
            </script>
        """)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = """Hello,       USERNAME : %s,
                                   
                                   PASSWORD : %s
                            """ % (username, password)

sender_address = 'Mail Name'
sender_pass = 'Password'
receiver_address = email
message = MIMEMultipart()
message['From'] = sender_address        #This is sender address.
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
