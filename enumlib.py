from enum import Enum, unique

class enumlib:

    def valList(enumList):
        if isinstance(enumList, Enum)
            return [eList.value for eList in enumList]
        else:
            raise TypeError("instance is not of type Enum")

    def nameList(enumList):
        if isinstance(enumList, Enum)
            return [eList.name for eList in enumList]
        else:
            raise TypeError("instance is not of type Enum")

    def trykey(cls, keyVal):
        return keyVal in cls.__members__

class engEnum:

    def newEnum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.iteritems())
        enums['reverse_mapping'] = reverse
        return type('Enum', (), enums)
