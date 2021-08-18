#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback
import cgi, pymysql, cgitb;

cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
# this is HTML and CSS.
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CS_Loggin</title>
    <style>
        body{
            background-image: url(images/customer.jfif);
            text-align: center;
        }
        form{
            border: 3px solid black;
            display: inline-block;
            padding: 30px;
            border-radius: 20px;
            background: coral;
        }
        label{
            color: black;
            text-shadow: lightcoral 3px;
        }
        input{
            border-radius: 2px;
            border: 3px solid;
        }
        a{
            text-decoration: none;
            color:black;
        }
        h1{
            color: white;
            top: 100px;
            left:30px;
        }
    </style>
</head>
<body>
    <h1>Customer Loggin </h1>
    <div class="main">
        <section class="content">
            <form autocomplete="off">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Password"><br><br>
                <a href="cforgotpassword.py">forgot password?</a><br><br>
                <a href="cregistoration.py">New User Click Here to Register!</a><br><br>
                <button type="submit" name = "login" value = "login">Login</button>
                <button type="submit" ><a href="mainpage.py">Cancel</a></button>
            </form>
        </section>
    <div></div>
</body>
</html>
""")

f = cgi.FieldStorage()              #to get field data from form.
username = f.getvalue("username")   #to get the value of username.
password = f.getvalue("password")   #to get to value of password.
v = f.getvalue("login")
if v!=None:
    q = """select id from cregistoration where username='%s' and password = '%s'""" %(username,password)
    cur.execute(q)                  #To fetch loggin details.
    r = cur.fetchone()              #check the loggin suxcess part.

    if r != None:
        print("""
            <script>
                alert("Login successfull");
                location.href = "clientprofile.py?id=%s";
            </script>
        """%(r[0]))
    else:
        print("""
            <script>
                alert("Login error")
            </script>
        """)