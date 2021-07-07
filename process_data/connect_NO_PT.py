import pymssql
import pandas as pd
from process_data.connect_NO_PT import Connect_SQLServer

class Data_NO_PT(Connect_SQLServer):

    def GET_NO_PT(self, params):
        print(params)
        params = self.convert_params(params)
        if params[1] != "NULL":
            params[1] = f"N{params[1]}"
        if params[2] != "NULL":
            params[2] = f"N{params[2]}"    
        if params[4] in ("'ten_kh'","'ten_hd'"):
            params[5] = f"N{params[5]}"
        # print(params)
        proc_name = 'EXEC dsa_N2H_Cong_No_Phai_tra {0}, {1}, {2}, {3}, {4}, {5}'.format(*params)
        cursor = self.Call_Proc(proc_name)
        if params[0] == "'dsa_N2H_graph_tinh_hinh_cong_no_ncc'":
            cols = ['Ma_kh', 'ten_kh','tong_cong_no','Da_Tra','Con_Lai','Du']
        elif params[0] == "'dsa_N2H_grh_top30_ncc_no_lon_nhat'":
            cols = ['ma_kh','ten_kh','Du']
        elif params[0] == "'dsa_N2H_table_tinh_hinh_cong_no_theo_hop_dong'":
            cols = ['ma_hd','ten_hd','ma_kh','ten_kh','ngay_hd','gt_hop_dong','con_lai','gt_chung_tu']
        elif params[0] == "'dsa_N2H_Table_Chi_Tiet_Chung_tu_theo_NCC'":
            cols = ['ma_hd','ten_hd','ma_ct','ma_kh','ten_kh','Giatri_chungtu','Da_tra','Conlai','songayquahan']
        elif params[0]== "'dsa_N2H_OverView_Tong_Cong_No'":
            cols = ['tong_cong_no']
        elif params[0] == "'dsa_N2H_OverView_Da_Tra'":
            cols = ['Da_tra']
        elif params[0] == "'dsa_N2H_OverView_Con_Lai'":
            cols = ['Con_lai']
        return self.Convert_DataFrame(cursor, cols)
    
    def GET_DDL_KHOXE(self, params):
        params = self.convert_params(params)
        proc_name = 'EXEC dsa_N2H_Cong_No_Phai_tra {0}, {1}, {2}, {3}, {4}, {5}'.format(*params)
        cursor = self.Call_Proc(proc_name)
        if params[0] in ("'dsa_N2H_ddl_ncc'"):
            cols = ['list_ddl_nha_cc']
        elif params[0] == "'dsa_N2H_ddl_hop_dong'":
            cols = ['list_ddl_ten_hd']
        elif params[0] == "'dsa_N2H_ddl_chung_tu'":
            cols = ['so_chung_tu']
        return self.Convert_DataFrame(cursor, cols)
    
        
