import configparser
import fileconfig

class parser_config:

    def checkAllValues(dirname, section): #Returns list of whether keys in section have values
        config = configparser.ConfigParser()
        config.read(dirname)
        ret_vals = []
        for key in config[section]:
            if bool(str(config[section][key]).strip()):
                ret_vals.append[True]
            else:
                ret_vals.append[False]
        return ret_vals

    def checkValue(dirname, section, key): #Returns whether key has a value
        config = configparser.ConfigParser()
        config.read(dirname)
        if config[section][key]:
            return True
        else:
            return False

    def checkValue(dirname, section, key, value): #Check value of a key if it exists
        config = configparser.ConfigParser()
        config.read(dirname)
        if config[section][key]:
            if config[section][key] == value:
                return True
            else:
                return False
        else:
            return False

    def getValue(dirname, section, key):
        config = configparser.ConfigParser()
        config.read(dirname)
        try:
            return config[section][key]
        except KeyError:
            pass

    def getAllValues(dirname, section):
        config = configparser.ConfigParser()
        config.read(dirname)
        ret_vals = []
        for key in config[section]:
            if bool(str(config[section][key]).strip()):
                ret_vals.append(config[section][key])
            else:
                ret_vals.append(None)
        return ret_vals

class cfg(fileconfig.Config):

    filename = "/path/to/file.ini"
    def __init__(self, key, **kwargs):
        self.key = key
        self.__dict__.update(kwargs)

class ini_config:

    def getValue(section, keyarg):
        ret_val = cfg(section).__dict__
        return ret_val.get(keyarg)

    def writeValue(section, keyarg, keyState):
        filepath = "/path/to/file.ini"
        config = configparser.ConfigParser()
        config.read(filepath)
        if key not in config:
            config.add_section(section)
            config.set(section, keyarg, keyState)
        else:
            config.set(section, keyarg, keyState)

        with open(filepath, 'w+') as configfile:
            config.write(configfile)
