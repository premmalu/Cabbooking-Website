#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
f = cgi.FieldStorage()      #Getting the data from Fieldstorage.
id = f.getvalue("id")       #Getting the id.

if len(f) == 2:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
else:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
    username = f.getvalue("username")
    email = f.getvalue("email")
    password = f.getvalue("password")
    contact = f.getvalue("contact")
    dob = f.getvalue("dob")
    address = f.getvalue("address")
    distric = f.getvalue("distric")
    state = f.getvalue("state")
    vehicletype = f.getvalue("vehicletype")
    profile = f['profile']
    aadharcard = f['aadharcard']
    licence = f['licence']

    if profile.filename:
        import os

        fp = os.path.basename(profile.filename)
        open("images/" + fp, "wb").write(profile.file.read())
        fp1 = os.path.basename(aadharcard.filename)
        open("images/" + fp1, "wb").write(aadharcard.file.read())
        fp2 = os.path.basename(licence.filename)
        open("images/" + fp2, "wb").write(licence.file.read())
        q1 = """update sregistoration set username = '%s',email = '%s',password='%s',contact = '%s',dob = '%s',address = '%s',distric = '%s',state = '%s',vehicletype='%s',profile = '%s',aadharcard='%s',licence='%s' where id = '%s'""" % (
            username, email, password, contact, dob, address, distric, state, vehicletype, fp, fp1, fp2, cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "sharer.py?id=%s";
            </script>
            """ % (id))
    else:
        q1 = """update sregistoration set username = '%s',email = '%s',password='%s',contact = '%s',dob = '%s',address = '%s',distric = '%s',state = '%s',vehicletype='%s' where id = '%s'""" % (
            username, email, password, contact, dob, address, distric, state, vehicletype, cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "sharer.py?id=%s";
            </script>
            """ % (id))

q = """select * from sregistoration where id='%s'""" % (cid)
cur.execute(q)
r = cur.fetchone()
#HTML and CSS
print("""
<html>
<head>
    <title>Sharer Registration</title>
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
    </style>
""")
print("""
</head>
<body>
    <h1>SHARER REGISTORATION FORM</h1>
    <form method = "post" action = "sedit.py" enctype = "multipart/form-data" autocomplete="off>
        <div>
        <input type="hidden" name="id" value="%s">
        <input type="hidden" name="cid" value="%s">
        <label for="username">Username:</label><br>
        <input type="text" id = "username" name="username" placeholder="Enter your username" value="%s"><br><br>
        <label for="email">Email</label><br>
        <input type="email" id = "email" name="email" placeholder="Enter your email" value="%s"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id = "password" name="password" value="%s"><br><br>
        <label for="contact">Contact:</label><br>
        <input type="tel" id = "contact" name="contact" placeholder="Enter your contact-number" value="%s"><br><br>
        <label for="dob">Dob:</label><br>
        <input type="text" id = "dob" name="dob" placeholder="Enter your dob" value="%s" ><br><br>
        <label for="address">Address</label><br>
        <input type="text" id = "address" name="address" placeholder="Enter your address" value="%s"><br><br>
        <label for="distric">Distric:</label><br>
        <input type="text" id = "distric" name="distric" value="%s"><br><br>
        <label for="state">State:</label><br>
        <input type="text" id = "state" name="state" value="%s"><br><br>
        <label for="profile" >Profile:</label><br>
        <img src="images/%s" width="50px" height="50px">
        <input type="file" id = "profile" name="profile"><br><br>

        <label for="aadharcard" >aadharcard:</label><br>
        <img src="images/%s" width="50px" height="50px">
        <input type="file" id = "aadharcard" name="aadharcard"><br><br>

        <label for="licence" >licence:</label><br>
        <img src="images/%s" width="50px" height="50px">
        <input type="file" id = "licence" name="licence"><br><br>
        
        <button type="submit" name = "reg" id = "reg">Register</button>
        <button type="submit">Cancel</button>
        </div> 
    </form>
</body>
</html>
""" % (id, cid, r[2], r[3], r[4], r[5], r[7], r[8], r[9], r[10], r[11], r[12], r[13]))
conn.close()