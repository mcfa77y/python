#!/usr/bin/python
import adodapi

def main():
	# connection string for an SQL server
    _computername="127.0.0.1" #or name of computer with SQL Server
    _databasename="bcdevdb1" #or something else
    _table_name= 'Lease'

    if True:
        # this will open a MS-SQL table with Windows authentication
        constr = r"Initial Catalog=%s; Data Source=%s; Provider=SQLOLEDB.1; Integrated Security=SSPI" \
                 %(_databasename, _computername)
	conn = adodapi.connect(host='SQL01', user='user', password='password', database='mydatabase')
	cur = conn.cursor()
		
	#run an SQL statement on the cursor
	sql = 'select * from %s' % _table_name
	c.execute(sql)
	
	#check the results
	print 'result rowcount shows as= %d. (Note: -1 means "not known")' \
	      % (c.rowcount,)
	print
	print 'result data description is:'
	print '            NAME Type         DispSize IntrnlSz Prec Scale Null?'
	for d in c.description:
	    print ('%16s %-12s %8d %8s %4d %5d %s') % \
	          (d[0], adc.adTypeNames[d[1]], d[2],   d[3],  d[4],d[5], bool(d[6]))
	print
	print 'str() of first five records are...'
	
	#get the results
	db = c.fetchmany(5)
	
	#print them
	for rec in db:
	    print rec
	
	print
	print 'repr() of next row is...'
	print repr(c.next())
	print
	
	c.close()
	con.close()
main()