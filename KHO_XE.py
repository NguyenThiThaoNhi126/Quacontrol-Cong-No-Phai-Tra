# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import datetime
from app import app_NO_PT
from index_string import index_str
from DB import DF_XeDG  
from dash.dependencies import Input, Output, State
from layouts.no_phai_tra import SL_XE_KHO, GIATRI_KHOXE, SL_MAUXE_KHO, DETAIL_MAU_SL_KHO, DETAIL_KHOXE, OV_GT_XE, OV_SL_XE, DDL_XE,\
                              SL_XE_DG, SL_XE_DG_TG, DETAIL_MAU_XE_DG, DETAIL_XE_DG, DDL_XE_DG, OV_SL_XE_DG, OV_GT_XE_DG_CHUA_VAT
                        


app_NO_PT.index_string = index_str


def render_layout():

    # df = DF_XeDG.get_data()
    now = datetime.datetime.today().strftime('%Y-%m-%d')

    layout = html.Div([
        html.Div([
            html.Div([
                OV_GT_XE.gen_layout(),
                OV_SL_XE.gen_layout(),
                OV_GT_XE_DG_CHUA_VAT.gen_layout(),
                OV_SL_XE_DG.gen_layout()
            ],style={'height':'15vh'},className='ele_row m-b-10'),

            html.Div([
                dcc.DatePickerSingle(
                id='warehouse_date',
                placeholder='Ngày',
                day_size = 42,
                clearable=True,
                number_of_months_shown=3,
                display_format = 'DD/MM/YYYY',
                date = now),
            ],className='col',style ={'marginBottom':'10px'}),
            
            DDL_XE.gen_layout(),

            html.Div([
                SL_XE_KHO.gen_layout(),
                GIATRI_KHOXE.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15'),

            html.Div([
                SL_MAUXE_KHO.gen_layout(),
                DETAIL_MAU_SL_KHO.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15'),

            html.Div([
                DETAIL_KHOXE.gen_layout()
            ],style={'height':'40vh'},className='m-b-15'),

            #  html.Div([
            #     dcc.DatePickerRange(
            #             id='date_DG',
            #             day_size = 42,
            #             display_format = 'DD/MM/YYYY',
            #             clearable=True,
            #             start_date_placeholder_text='Ngày bắt đầu',
            #             end_date_placeholder_text='Ngày kết thúc',
            #             number_of_months_shown=3,
            #             minimum_nights=0,
            #             start_date_id='start_date',
            #             end_date_id='end_date',
            #             start_date = min(df['ngay_giao']).strftime('%Y-%m-%d'),
            #             end_date = max(df['ngay_giao']).strftime('%Y-%m-%d'),)
            # ],className='col',style ={'marginBottom':'10px'}),

            # DDL_XE_DG.gen_layout(),

            # html.Div([
            #     SL_XE_DG.gen_layout(),
            #     DETAIL_XE_DG.gen_layout()
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

            # html.Div([
            #     SL_XE_DG_TG.gen_layout(),
            #     DETAIL_MAU_XE_DG.gen_layout(),
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

        ], className="container-fluid")
    ], className="section__content--p30", style={'backgroundColor': '#e5e5e5'})

    return layout

app_NO_PT.layout = render_layout

if __name__ == '__main__':
    app_NO_PT.run_server(port=2222, debug=True,host='127.0.0.1')