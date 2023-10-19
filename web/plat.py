import platform


def whoami():
    current_platform = platform.system()

    if current_platform == "Windows":
        # Code to run on a local Windows machine
        print("Running on a local Windows machine.")
    elif current_platform == "Linux":
        # Code to run on a Linux server
        print("Running on a Linux server.")
        return "bin/geckodriver-linux"
    else:
        # Code to run on an unknown platform (you can add more cases as needed)
        print(f"Running on an unknown platform: {current_platform}")
        return "bin/geckodriver-macos"

def is_docker() -> bool:
    current_platform = platform.system()
    if current_platform == "Linux":
        print("Running in a container!")
        return True
    else:
        print(f"Running locally: {current_platform}")
        return False