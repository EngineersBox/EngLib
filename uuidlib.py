import uuid

class uuidlib:

    def __init__(self):
        self.cfg_path = ""

    def mult_uuid1(nodes=[], clock_seqs=[], count=0):
        if len(nodes) == len(clock_seqs) and len(nodes) == count:
            ret_val = []
            for i in range(count):
                ret_val.append(uuid.uuid1(nodes[i], clock_seqs[i]))
            return ret_val
        elif len(nodes) < 1 and len(clock_seqs) < 1 and count > 0:
            ret_val = []
            for i in range(count):
                ret_val.append(uuid.uuid1())
            return ret_val
        else:
            pass

    def mult_uuid3(namespaces=[], names=[], count=0): #Returned as a list
        if len(namespaces) == len(names) and len(names) == count:
            ret_val = []
            for i in range(count):
                ret_val.append(uuid.uuid3(namespaces[i], names[i]))
            return ret_val
        else:
            pass

    def mult_uuid4(count=0): #Returned as a list
        if count > 0:
            ret_val = []
            for i in range(count):
                ret_val.append(uuid.uuid4())
            return ret_val
        else:
            pass

    def mult_uuid5(namespaces=[], names=[], count=0): #Returned as a list
        if len(namespaces) == len(names) and len(names) == count:
            ret_val = []
            for i in range(count):
                ret_val.append(uuid.uuid5(namespaces[i], names[i]))
            return ret_val
        else:
            pass

    def str_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(str(i))
            return ret_val
        else:
            pass

    def bytes_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.bytes)
            return ret_val
        else:
            pass

    def hex_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.hex)
            return ret_val
        else:
            pass

    def int_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.int)
            return ret_val
        else:
            pass

    def urn_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.urn)
            return ret_val
        else:
            pass

    def variant_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.variant)
            return ret_val
        else:
            pass

    def version_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.version)
            return ret_val
        else:
            pass

    def is_safe_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.is_safe)
            return ret_val
        else:
            pass

    def node_list(uuidList=[]):
        if len(uuidList) > 0:
            ret_val = []
            for i in uuidList:
                ret_val.append(i.getnode())
            return ret_val
        else:
            pass
