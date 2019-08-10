import cx_Oracle
con = cx_Oracle.connect('jothi/jothi1@localhost/xe')
print (con.version)
con.close()
