from controller.get_params import Get_Params
from DB import DF_XeDG
import config as cf

class Params_XEDG(Get_Params):
    def Get_Value(self, ctx, data=None):
        label, value = super().Get_Value(ctx, data)

        if self._id_ in cf.MultiLine_Chart.keys() and value is not None:
            return label, DF_XeDG.MaKho[self._id_][value]
            
        return label, value