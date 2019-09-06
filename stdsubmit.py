import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='aump')
a=conn.cursor()
print ("content-type:text/html\r\n\r\n")
res=cgi.FieldStorage()
nm=str(res.getvalue('nm'))
fnm=str(res.getvalue('fnm'))
add=str(res.getvalue('add'))
gen=str(res.getvalue('gen'))
state=str(res.getvalue('state'))
city=str(res.getvalue('city'))
dob=str(res.getvalue('dob'))
pincode=str(res.getvalue('pincode'))
course=str(res.getvalue('course'))
email=str(res.getvalue('email'))
pwd=str(res.getvalue('pwd'))
rpwd=str(res.getvalue('rpwd'))

if pwd==rpwd:
    sql="insert into stdreg values('"+nm+"','"+fnm+"','"+add+"','"+gen+"','"+state+"','"+city+"','"+dob+"',"+pincode+",'"+course+"','"+email+"','"+pwd+"')"
    insert=a.execute(sql)
    
    if insert!=0:
        print("<h2 align=center>Successful Thank You<h2>")
    else:
        print("failed")

    conn.commit()
else:
    print("Password Not Matched....")
print("<br>")



