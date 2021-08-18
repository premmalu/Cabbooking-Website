#!C:/Users/prem/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html \r\n\r\n")
# impotring the common Gateway interface,sql,cgi trackback.
import cgi, pymysql, cgitb ;

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="ridesharer") #connection with phpmysql using Xampp.
cur = conn.cursor()
#HTML and CSS.
print("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<style>
body {
  font-family: "Lato", sans-serif;
  background-image:url(images/peace.jpg);
  background-size:cover;
}
.sidenav {
  height: 100%;
  width: 60px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #003147;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
  border-right:5px solid #818181 ;
}

.sidenav a {
  padding: 8px 8px 8px 22px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: flex;
  transition: 0.3s;
}
.sidenav a h5{
  margin-left: 20px;
  margin-top: 0px;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 60px;
  font-size: 36px;
  margin-left: 20px;
  display: flex;
}

#main {
  transition: margin-left 0.5s;
  margin-left: 75px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
#pane1{
  display: none;
  margin-top: -30px;
}
#pane1 a{
  font-size: 20px;
}
#pane1.active{
  display: flex;
}
#pane1 li{
  color: #f1f1f1;
  list-style: none;
  display: flex;
}
#pane2{
  display: none;
  margin-top: -30px;
}
#pane2 a{
  font-size: 20px;
}
#pane2.active{
  display: flex;
}
#pane2 li{
  color: #f1f1f1;
  list-style: none;
  display: flex;
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="mainpage.py"><i class="fa fa-home" aria-hidden="true"></i> <h5>Home</h5></a>
  <a href="adminviewprofile.py"><i class="fa fa-users" aria-hidden="true"  ></i><h5>Admin</h5></a>
  <li onclick="onenslide1()" style="list-style:none"><a href="#"><i class="fa fa-cogs" aria-hidden="true"></i> <h5 id="slide1">Sharer</h5></a>
    <div id="pane1" ><ul>
      <a href="newsharer.py"> <i class="fa fa-play" aria-hidden="true"></i>New</a>
      <a href="sharer.py"> <i class="fa fa-play" aria-hidden="true"></i>Existing</a>
    </ul></div></li>
  <li onclick="onenslide2()" style="list-style:none"><a href="#"><i class="fa fa-comments" aria-hidden="true"></i><h5 id="slide2">Client</h5></a>
    <div id="pane2" ><ul>
      <a href="newclient.py"> <i class="fa fa-play" aria-hidden="true"></i>New</a>
      <a href="customer.py"> <i class="fa fa-play" aria-hidden="true"></i>Existing</a>
    </ul></div></li>
  <a href="adminlogin.py"><i class="fa fa-sign-out" aria-hidden="true"></i> <h5>logout</h5></a>
</div>
<div id="main">
  <span style="font-size:30px;cursor:pointer;color: #f1f1f1;" onclick="openNav()">&#9776;</span>
</div>

<script>
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "80px";
};
function closeNav() {
  document.getElementById("mySidenav").style.width = "60px";
  document.getElementById("main").style.marginLeft= "75px";
}
function onenslide1() {
  let navigation=document.querySelector('#slide1');
  navigation.classList.toggle('active');
  let navigation1=document.querySelector('#pane1');
  navigation1.classList.toggle('active');
}
function onenslide2() {
  let toggle1=document.querySelector('#slide2');
  toggle1.classList.toggle('active');
  let toggle2=document.querySelector('#pane2');
  toggle2.classList.toggle('active');
}
</script>
   
</body>
</html> 

""")