import json

def load_config_file(config_file_path):
    with open(config_file_path, 'r') as f:
        config = json.load(f)
    return config

config = load_config_file('config.json')
db_params = config['database']
