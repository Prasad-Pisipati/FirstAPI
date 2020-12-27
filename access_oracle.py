import cx_Oracle

dsn_tns = cx_Oracle.makedsn('64.101.193.207', '1541', service_name='CFNSTG.cisco.com')
conn = cx_Oracle.connect(user=r'apps', password='metal1nk', dsn=dsn_tns)

c = conn.cursor()

c.execute("select * from fnd_user where user_name = 'VPISIPAT'")
for row in c:
    print (row[0], '-',row[1], '-', row[2] )

conn.close()