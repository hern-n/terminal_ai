import json
from importlib.resources import files

# Rutas de archivos dentro del paquete nexus
data_file = files("nexus").joinpath("data/data.json")
system_file = files("nexus").joinpath("data/system.txt")
command_file = files("nexus").joinpath("data/commands_data.txt")


def load_system():
    return system_file.read_text(encoding="utf-8")


def load_command_data():
    return command_file.read_text(encoding="utf-8")


def load_data():
    return json.loads(data_file.read_text(encoding="utf-8"))


def save_current_agent(current_agent):
    data = load_data()
    data["current_agent"] = current_agent
    data_file.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
