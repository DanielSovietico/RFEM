import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn
from RFEM.DynamicLoads.accelerogram import Accelerogram

if Model.clientModel is None:
    Model()

def test_accelerogram():

    SetAddonStatus(Model.clientModel, AddOn.spectral_active, True)
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # create user defined accelerogram
    Accelerogram(1, 'User-Defined Accelerogram', user_defined_accelerogram = [[0, 0.1, 0.2, 9.81], [20, 0.3, 0.5, 12.5]])
    Accelerogram.FromLibrary(no = 2, library_id= 939)
    Model.clientModel.service.finish_modification()

    acg_1 = Model.clientModel.service.get_accelerogram(1)
    acg_2 = Model.clientModel.service.get_accelerogram(2)

    assert acg_1.no == 1
    assert round(acg_1.user_defined_accelerogram[0][0]['row']['acceleration_x'], 2) == 0.1
    assert round(acg_1.user_defined_accelerogram[0][1]['row']['time'], 2) == 20

    assert acg_2.name == 'Aftershock of Kocaeli earthquake, Turkey - Messstation: Afyon-Bayindirlik ve Iskan Mudurlugu'
    assert round(acg_2.user_defined_accelerogram[0][0]['row']['acceleration_x'], 8) == -3.242e-05
