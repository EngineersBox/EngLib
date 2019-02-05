class jsonlib:

    def getData(dirname, data_filter, data_set):
        with open(dirname) as json_file:
            data = json.load(json_file)
            for p in data[data_filter]:
                return p[data_set]
