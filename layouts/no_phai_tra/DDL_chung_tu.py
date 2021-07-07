import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app_NO_PT
from utils import GParams
from DB import DB_KhoXe
# from dash.exceptions import PreventUpdate

def gen_ddl(id_ddl, placeholder,className):
    data = DB_KhoXe.GET_DDL_KHOXE((id_ddl,))
    if id_ddl in ("ddl_dvcs","ddl_dgx","ddl_dx","ddl_mauxe"):
        options = [{'value': data.values[i][0], 'label': data.values[i][1], 'title': data.values[i][1]} for i in range(data.shape[0])]
    else:
        options = [{'value': data.values[i][0], 'label': data.values[i][0], 'title': data.values[i][0]} for i in range(data.shape[0])]
    return  html.Div([
                dcc.Dropdown(
                    id=id_ddl,
                    options = options,
                    placeholder=placeholder,
                )
            ], className=className)

def gen_layout():
    layout= html.Div([
                    gen_ddl('ddl_dvcs', "Chọn cửa hàng",'col-4'),
                    gen_ddl('ddl_vt', "Chọn vật tư",'col-4'),
                    gen_ddl("ddl_dgx", "Chọn dòng xe",'col-4 m-b-5'),
                    gen_ddl("ddl_dx", "Chọn đời xe",'col-6'),
                    gen_ddl("ddl_mauxe", "Chọn màu xe",'col-6'),
                ], className="ele_row m-b-15",style={'width':'100%','flexWrap':'wrap'})
    return layout