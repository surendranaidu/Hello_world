import cx_Oracle
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine

saengine = create_engine('<connection string>', echo=True)
saconn = saengine.connect()
QUERY = '''
    SELECT
        *
    FROM
        one1clear.servicetypes
'''
updatequery="update one1clear.servicetypes set enb_auto_ntg=:flag where svctype=:type"

class DB:
    def dbcon():
        CONN_INFO = {
            'host': 'oradevpim-db',
            'port': 1521,
            'user': 'da_own',
            'psw': 'dev',
            'service': 'dv03pimi_cfport_con'
        }
        CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)
        con = cx_Oracle.connect(CONN_STR)
        cursor = con.cursor()
        return cursor


cur = DB()
result = cur.callproc('<schema>.<stored procedure name>',{'param' : 'value', 'param' : 'value'})
print result
for i in result:
    print i
    ins = <plbbgbatch>.insert()
    saconn.execute(ins, id=2, name='test', age=12)
oracle_connection_string = (
    'oracle+cx_oracle://{username}:{password}@' +
    cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
)

engine = create_engine(
    oracle_connection_string.format(
        username='CALCULATING_CARL',
        password='12345',
        hostname='all.thedata.com',
        port='1521',
        service_name='every.piece.ofdata',
    )
)   
