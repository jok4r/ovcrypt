import pathlib
import os
import json


config_path = os.path.join('/etc/overengine/', 'ovcrypt.json')
config_path_alternate = os.path.join(os.path.expanduser("~"), '.config', 'overengine', 'ovcrypt.json')


def import_config(path=config_path):
    if not os.path.isfile(path):
        if path == config_path_alternate:
            generate_config()
        else:
            return import_config(config_path_alternate)
    with open(path, 'r') as f:
        load_config_data = json.loads(f.read())
    std_config = get_std_config()
    need_update = False
    for key in std_config:
        if key not in load_config_data:
            load_config_data[key] = std_config[key]
            need_update = True
    if need_update:
        update_config(path, load_config_data)
    return load_config_data


def update_config(path, c_data):
    with open(path, 'w') as f:
        f.write(json.dumps(c_data, indent=4, sort_keys=True))


def get_std_config():
    keys_dir = 'keys'
    config_data = {
        'keys_dir': keys_dir,
        'rsa_server_public_key_file': os.path.join(keys_dir, 'ov_public.pub'),
        'rsa_server_private_key_file': os.path.join(keys_dir, 'ov_private.pem'),
    }
    return config_data


def generate_config():
    global config_path
    global config_path_alternate
    config_data = get_std_config()
    try:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            f.write(json.dumps(config_data, indent=4, sort_keys=True))
    except PermissionError:
        config_path = config_path_alternate
        return generate_config()
    print(f'Created new config: {config_path}')


if __name__ == '__main__':
    input('Press Enter to rewrite config')
    generate_config()
    print(import_config())

