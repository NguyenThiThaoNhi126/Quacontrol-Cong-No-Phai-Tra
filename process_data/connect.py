import pymssql
import pandas as pd
from datetime import datetime as dt

class Connect_SQLServer:

    def __init__(self, host, database, uid, pw):
        self.uid = uid
        self.pw = pw
        self.host = host
        self.database = database

    def Call_Procedure(self, proc):
        '''Kết nối đến CSDL và thực thi Procedure'''

        conn = pymssql.connect(self.host, self.uid, self.pw, self.database)
        print('AAAAAAAAAAAAAAAAAAAAA', proc)
        
        cursor = conn.cursor()
        cursor.execute(proc)

        return cursor

    def Convert_DataFrame(self, cursor, cols):
        '''Chuyển đổi dữ liệu lấy được về dạng DataFrame'''
        
        results = cursor.fetchall()
        df = pd.DataFrame.from_records(results, columns=cols)
        return df

    def convert_params(self, params):
        r = []
        for val in params:
            r.append('NULL') if val is None else r.append("'"+val+"'")
        return r