from RFEM.initModel import Model, clearAtributes

class Instersection():
    def __init__(self,
                 no: int = 1,
                 surface_1: int = 1,
                 surface_2: int = 2,
                 comment: str = '',
                 params: dict = None):

        # Client model | Intersection
        clientObject = Model.clientModel.factory.create('ns0:intersection')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Intersection No.
        clientObject.no = no

        # Assigned surfaces
        clientObject.surface_a = surface_1
        clientObject.surface_b = surface_2

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Intersection to client model
        Model.clientModel.service.set_intersection(clientObject)
