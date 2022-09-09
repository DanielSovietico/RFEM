from enum import Enum


class ObjectTypes(Enum):
    '''
    Object Types
    '''

    E_OBJECT_TYPE_MATERIAL, E_OBJECT_TYPE_SECTION, E_OBJECT_TYPE_POINT = range(3)


class PointType(Enum):
    '''
    Point Type | Enumeration
    '''
    TYPE_STANDARD, TYPE_BETWEEN_TWO_POINTS, TYPE_BETWEEN_TWO_LOCATIONS, TYPE_ON_LINE = range(4)

class PointCoordinateSystemType(Enum):
    '''
    Point Coordinate System Type | Enum
    '''
    COORDINATE_SYSTEM_CARTESIAN = range(1)

class PointReferenceType(Enum):
    '''
    Point Reference Type| Enum
    '''
    REFERENCE_TYPE_L, REFERENCE_TYPE_Y, REFERENCE_TYPE_Z = range(3)

class LineType(Enum):
    '''
    Line Type | Enumeration
    '''
    TYPE_POLYLINE, TYPE_ARC, TYPE_CIRCLE = range(3)

class LineArcAlphaAdjustmentTarget(Enum):
    '''
    Line Arc Alpha Adjustment Target | Enumeration
    '''
    ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT, ALPHA_ADJUSTMENT_TARGET_END_OF_ARC = range(3)
