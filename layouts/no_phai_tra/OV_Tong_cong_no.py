import dash
import dash_core_components as dcc
import dash_html_components as html
from DB import DB_NO_PT
from app import app_NO_PT
from dash.dependencies import Input, Output, State
from utils import GParams
from static.system_dashboard.css import css_define as css
import pandas as pd
from layouts.no_phai_tra.gen_overview import create_card

def gen_layout():
    
    title = 'GIÁ TRỊ TỔNG CÔNG NỢ'
    color = '#60B664'
    icon = 'money-bag.svg'

    layout = create_card(title,'ov_gt',color,icon)
           
    return layout


@app_NO_PT.callback(
    Output("ov_gt", "children"),
    [Input('ddl_dvcs', 'value'),
     Input('ddl_vt', 'value'),
     Input('ddl_dgx', 'value'),
     Input('ddl_dx', 'value'),
     Input('ddl_mauxe', 'value'),
     Input('warehouse_date','date'),
     Input('grh_GiaTri_KhoXe','selectedData'),
     Input('grh_SL_MAUXE','selectedData'),
     Input('grh_TiLeXe_Kho','clickData'),
     Input('detail_XE_MAUXE','active_cell'),
     Input('detail_KhoXe','active_cell'),],
    [State('detail_XE_MAUXE','data'),
     State('detail_KhoXe','data')]
)
def UPDATE_OV_GT(ddl_dvcs,ddl_vt,ddl_dgx,ddl_dx,ddl_mauxe,date_wh,GT_KHO,SL_MAUXE,SL_KHO,ac_MX,ac_KHO,data_MX,data_KHO):
    ctx = dash.callback_context
    datatable = {'detail_XE_MAUXE':data_MX,
                  'detail_KhoXe':data_KHO}
    label, value = GParams.Get_Value(ctx,datatable)
    ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_NO_PT.GET_NO_PT(('ov_gt',date_wh,ddl_dvcs,ddl_vt,ddl_dgx,ddl_dx,ddl_mauxe,label,value))
    return df['GiaTri'].values[0]