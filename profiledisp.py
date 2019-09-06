import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='aump')
a=conn.cursor()
print ("content-type:text/html\r\n\r\n")
res=cgi.FieldStorage()
email=str(res.getvalue('username'))
sql="select * from stdreg 
a.execute(sql)
data=a.fetchall()

print("<html>")
print("<body>")
print("<form>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Profile Display</font></caption>")
print("<tr><td>Name</td><td>Father Name</td><td>Address</td><td>Gender</td><td>State</td><td>City</td><td>DOB</td><td>Pincode</td><td>Course</td><td>Email</td></tr>")

for i in data:
    print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td>"+str(i[7])+"</td><td>"+str(i[8])+"</td><td>"+str(i[9])+"</td><td><a href=updatecourse1.py?cid="+str(i[0])+">Update1<a></tr>")


print("<tr><td>footer</td><td>footer</td></tr>")
print("</table>")
print("</center>")
print("</form>")
print("</body>")
print("</html>")
