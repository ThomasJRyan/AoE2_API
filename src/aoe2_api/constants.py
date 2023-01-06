from aenum import MultiValueEnum

class Regions(MultiValueEnum):
    GLOBAL = 7, '7'
    AFRICA = 6, '6'
    OCEANIA = 5, '5'
    SOUTH_AMERICA = 4, '4'
    NORTH_AMERICA = 3, '3'
    ASIA = 2, '2'
    MIDDLE_EAST = 1, '1'
    EUROPE = 0, '0'

class MatchTypes(MultiValueEnum):
    TEW = 14, '14', 'tew'
    EW = 13, '13', 'ew', 'Empire Wars'
    TRM = 4, '4', 'trm'
    RM = 3, '3', 'rm', 'Random Map'
    TDM = 2, '2', 'tdm'
    DM = 1, '1', 'dm', 'Death Match'

class MatchSize(MultiValueEnum):
    ONE_VS_ONE = '1v1'
    TWO_VS_TWO = '2v2'
    THREE_VS_THREE = '3v3'
    FOUR_VS_FOUR = '4v4'

class MapSize(MultiValueEnum):
    LARGE = 'Large'
    MEDIUM = 'Medium'
    NORMAL = 'Normal'
    SMALL = 'Small'
    TINY = 'Tiny'