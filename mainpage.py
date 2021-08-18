#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb;cgitb.enable()
#connection with phpmysql using Xampp.
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer")
cur = conn.cursor()
#HTML and CSS
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <title>Comfi Rides</title>
    <style> 
    .main{
    padding: 0;
    margin: 0;
    background: #fff;
    width: 100%;
    height: 100%;
    }
    .main .topbar{
        position: relative;
        height: 80px;
        width: 100%;
        background:hsl(199, 100%, 14%);  
    }
    .topbar ul li:nth-child(1){
        float: left;
        padding-top: 10px;
    }
    .topbar ul li:nth-child(1):hover{
        background: transparent;
    }
    .topbar ul li{
        float: right;
        padding: 20px;
        padding-top: 30px;
    }
    .topbar ul li:hover{
        background: #05c9fa;
    }
    .topbar ul li{
        list-style: none;
    }
    .topbar ul li a
    {
        position: relative;
        display: block;
        width: 100%;
        display: inline;
        text-decoration: none;
        color:#fff;
    }
    .topbar .icon{
        color: coral;
        size: 30px;
    }
    .b_content img{
        width: 100%;
        height: 100%;
        margin-top: -20px;
    }
    </style>
</head>
<body>
    <div class="main">
        <div class="topbar">
            <ul>
                <li>
                    <a href="#">
                        <span class="title"><h2><span class="icon"><i class="fa fa-bus" aria-hidden="true"></i></span>  COMFI RIDES</h2></span>
                    </a>
                </li>
                <li>
                    <a href="adminlogin.py">
                        <span class="icon"><i class="fa fa-home" aria-hidden="true"></i></span>
                        <span class="title">ADMIN</span>
                    </a>
                </li>
                <li>
                    <a href="cloggin.py">
                        <span class="icon"><i class="fa fa-users" aria-hidden="true"></i></span>
                        <span class="title">Clients</span>
                    </a>
                </li>
                <li>
                    <a href="slogin.py">
                        <span class="icon"><i class="fa fa-comments" aria-hidden="true"></i></span>
                        <span class="title">Sharer</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    <div class="b_content">
       <img src="images/preview_taxi.jpeg" alt="content">
    </div>
</body>
</html>
""")