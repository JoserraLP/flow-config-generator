import argparse, json, os, errno

def parse_value_type(value_type: str):
    if value_type == "int":
        value_type = int  
    elif value_type == "float":
        value_type = float
    elif value_type == "bool":
        value_type = bool  
    elif value_type == "str":
        value_type = str       

    return value_type


class Generator:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args_vals = {}

        self.get_file_arguments()
        self.define_arguments()
        self.store_arguments_vals()
        self.create_json_config_file()

    def get_file_arguments(self):
        with open ("arguments.json") as f:
            self.file_args = json.load(f)

    def define_arguments(self):
        for long_name, value in self.file_args.items():
            
            if 'type' in value:
                value_type = parse_value_type(value['type'])

            if 'action' in value:
                self.parser.add_argument(value['short_name'], long_name, help=value['help'], action=value['action'])
            else:
                self.parser.add_argument(value['short_name'], long_name, help=value['help'], type=value_type, default=value['default'])

        self.args = self.parser.parse_args()
    def store_arguments_vals(self):
        for arg in vars(self.args):
            value = getattr(self.args, arg)
            if value is not None:
                arg_name = '--'+arg.replace('_', '-')
                if 'name' in self.file_args[arg_name]:
                    config_name = self.file_args[arg_name]['name']
                    config_group = self.file_args[arg_name]['group']
                    if config_group not in self.args_vals:
                        self.args_vals[config_group] = {}
                    if config_name == "NETWORK":
                        list_values = value.strip('][').split(',')
                        self.args_vals[config_group][config_name] = {}
                        self.args_vals[config_group][config_name]['COLS'] = list_values[0]
                        self.args_vals[config_group][config_name]['ROWS'] = list_values[1]
                    elif config_name == "WAYS":
                        list_values = value.strip('][').split(',')
                        self.args_vals[config_group][config_name] = {}
                        self.args_vals[config_group][config_name]['top'] = list_values[0]
                        self.args_vals[config_group][config_name]['bot'] = list_values[1]
                        self.args_vals[config_group][config_name]['left'] = list_values[2]
                        self.args_vals[config_group][config_name]['right'] = list_values[3]
                    else:
                        self.args_vals[config_group][config_name] = value


    def create_json_config_file(self):
        output_file =  getattr(self.args, 'output_directory')+'generated/'+self.args_vals['GLOBAL']['EXP_NAME']+"_config.json"

        if not os.path.exists(os.path.dirname(output_file)):
            try:
                os.makedirs(os.path.dirname(output_file))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        
        with open(output_file, 'w') as config_file: 
            json.dump(self.args_vals, config_file)            
            

if __name__ == "__main__":
    generator = Generator()

