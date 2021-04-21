import argparse
import errno
import json
import os


def parse_value_type(value_type: str) -> type:
    """
    Return the object type represented by the param string
    :param value_type: The string representing the object
    :type value_type: str
    :return: the object type
    :rtype: type
    """
    if value_type == "int":
        value_type = int
    elif value_type == "float":
        value_type = float
    elif value_type == "bool":
        value_type = bool
    elif value_type == "str":
        value_type = str

    return value_type


def get_file_arguments() -> dict:
    """
    Get the arguments stored in the "arguments.json" file and return them.
    :return: Dict with the arguments
    :rtype: dict
    """
    with open('arguments.json', 'r') as f:
        file_args = json.load(f)

    return file_args


class Generator:
    """
    Class for generating the configuration file that will be used for Flow framework. It can be used both by execution
    arguments or in an user-interactive way.
    """

    def __init__(self):

        #  Create the Argument Parser
        self.parser = argparse.ArgumentParser()

        # Initialize the class variables
        self.args_vals, self.args = {}, {}

        # Retrieve the arguments from the file "arguments.json"
        self.file_args = get_file_arguments()

        # Define the arguments of the generator
        self.define_arguments()

        # Store the values given by the execution arguments
        self.store_arguments_vals()

        # Create the json output file with the values
        self.create_json_config_file()

    def define_arguments(self) -> None:
        """
        Set the arguments extracted from the json file in the ArgumentParser and assign them into a class variable
        """

        # Iterate over the different arguments
        for long_name, value in self.file_args.items():

            if 'action' in value:
                # Some of the arguments would have a default action if not specified so it needs to be stored
                self.parser.add_argument(value['short_name'], long_name, help=value['help'], action=value['action'])
            else:
                # Otherwise, set the value type and the default value for the argument
                value_type = parse_value_type(value['type'])
                self.parser.add_argument(value['short_name'], long_name, help=value['help'], type=value_type,
                                         default=value['default'])

        # Store the arguments parsed by the ArgumentParser
        self.args = self.parser.parse_args()

    def store_arguments_vals(self) -> None:
        """
        Create a dict where all the data is going to be stored, in this case stored in a class variable called
        "args_vals", depending on its value it would be either processed or not.

        """

        # Iterate over the arguments from the ArgumentParser
        for arg in vars(self.args):
            # Retrieve the value
            value = getattr(self.args, arg)
            # Check if the value exists
            if value is not None:
                # Get the name of the argument
                arg_name = '--' + arg.replace('_', '-')
                # Check if the argument has the config name
                if 'name' in self.file_args[arg_name]:
                    # Retrieve the config name and group
                    config_name = self.file_args[arg_name]['name']
                    config_group = self.file_args[arg_name]['group']
                    # Create the dict for each group
                    if config_group not in self.args_vals:
                        self.args_vals[config_group] = {}
                    # In the "NETWORK" case, it is needed to split the value into two values: COLS and ROWS
                    if config_name == "NETWORK":
                        # Convert the string into a list
                        list_values = value.strip('][').split(',')
                        # Create the dict
                        self.args_vals[config_group] = {}
                        # Store the values
                        self.args_vals[config_group]['COLS'] = int(list_values[0])
                        self.args_vals[config_group]['ROWS'] = int(list_values[1])
                    # In the "WAYS" case, it is needed to split the value into four values: top, bot, left and right
                    elif config_name == "WAYS":
                        # Convert the string into a list
                        list_values = value.strip('][').split(',')
                        # Create the dict
                        self.args_vals[config_group][config_name] = {}
                        # Store the values
                        self.args_vals[config_group][config_name]['top'] = int(list_values[0])
                        self.args_vals[config_group][config_name]['bot'] = int(list_values[1])
                        self.args_vals[config_group][config_name]['left'] = int(list_values[2])
                        self.args_vals[config_group][config_name]['right'] = int(list_values[3])
                    # In the "PROB" case, parse the value to float
                    elif config_name == "PROB":
                        self.args_vals[config_group][config_name] = float(value)
                    # Otherwise, store the value itself
                    else:
                        self.args_vals[config_group][config_name] = value

    def create_json_config_file(self) -> None:
        """
        Create the directory indicated by arguments if not exists and store the dict with the values of the arguments
        into a json file.
        """

        # Create a variable for the output file <dir>/generated/<exp_name>_config.json
        output_file = getattr(self.args, 'output_directory') + 'generated/' + self.args_vals['GLOBAL']['EXP_NAME'] \
                      + "_config.json"

        # Check if the directory exists
        if not os.path.exists(os.path.dirname(output_file)):
            try:
                # Create the directory as it does not exists
                os.makedirs(os.path.dirname(output_file))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # Open output file and dump the dict
        with open(output_file, 'w') as config_file:
            json.dump(self.args_vals, config_file)


if __name__ == "__main__":
    generator = Generator()
