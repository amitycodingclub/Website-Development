import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='aump')
a=conn.cursor()
print ("content-type:text/html\r\n\r\n")
res=cgi.FieldStorage()
email=str(res.getvalue('username'))
pwd=str(res.getvalue('pass'))

sql="select * from stdreg where email='"+str(email)+"'and pwd='"+str(pwd)+"'"
a.execute(sql)
x=a.fetchone()

try:
    if x!=None:
        print("Login Successful")
        print ("<a href=stddash.py> Login To Your Dashboard Now </a>")

    elif x==None:
        print("Invalid Crdentials")
    
except:
    print("Server Error")    
    


