class yamllib:

    def __init__(self):
        self.cfg_path = ""

    #Check if file exists
    def check_file_inst(filepath):
        if not os.path.exists(filepath):
            with open(filepath, 'w'):
                print("File does not exist -- Generating " + filepath)
        else:
            print("File exists -- Skipping generation")

    #Loading from file
    def yaml_loader(filepath):
        with open(filepath, "r") as file_descriptor:
            data = yaml.safe_load(file_descriptor)
        return data

    #Writing to file
    def yaml_dump(filepath, data):
        with open(filepath, 'a') as file_descriptor:
            yaml.safe_dump(data, stream=file_descriptor, default_flow_style=False)

    #Check for instance before write
    def yaml_dump_check(filepath, key, data):
        with open(filepath, 'a') as file_descriptor:
            store_data = yaml_config.yaml_loader(filepath)
            if os.stat(filepath).st_size == 0 or key not in store_data:
                yaml.safe_dump(data, stream=file_descriptor, default_flow_style=False)
