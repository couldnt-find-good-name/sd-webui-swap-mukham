import launch
import os

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

try:
    launch.run_pip(f"install -r {req_file}", f"sd-webui-swap-mukham requirement: installing dependencies from {req_file}")
except Exception as e:
    print(e)
    print(f'Warning: Failed to install dependencies from {req_file}.')
