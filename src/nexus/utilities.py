import json
from importlib.resources import files
import os

# Rutas de archivos dentro del paquete nexus
data_file = files("nexus").joinpath("data/data.json")
system_file = files("nexus").joinpath("data/system.txt")
command_file = files("nexus").joinpath("data/commands_data.txt")
projects_folder = "C:/Users/holme/Escritorio/Projects"       # Esto para windows
# projects_folder = "/mnt/c/Users/holme/Escritorio/Projects" # Esto para WSL/Ubuntu

projects = [
    nombre for nombre in os.listdir(projects_folder)
    if os.path.isdir(os.path.join(projects_folder, nombre))
]

projects = "\n".join(projects)

def detect_shell():
    if os.name == "nt":  # Windows
        if "PSModulePath" in os.environ:
            return "PowerShell"
        comspec = os.environ.get("COMSPEC", "").lower()
        if comspec.endswith("cmd.exe"):
            return "CMD"
        return "Shell desconocida (Windows)"
    else:  # Linux / macOS
        return os.environ.get("SHELL", "Shell desconocida")

def load_system():
    file = system_file.read_text(encoding="utf-8")
    file = file.format(PROJECTS=projects, SHELL=detect_shell())
    return file


def load_command_data():
    file = command_file.read_text(encoding="utf-8")
    file = file.format(PROJECTS=projects, SHELL=detect_shell())
    return file


def load_data():
    return json.loads(data_file.read_text(encoding="utf-8"))


def save_current_agent(current_agent):
    data = load_data()
    data["current_agent"] = current_agent
    data_file.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")

if __name__ == "__main__":
    print(load_command_data())
    print(load_system())