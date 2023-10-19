import subprocess

from web.plat import whoami


def save():
    execname = whoami()
    subprocess.run(
        [execname, "-m", "local"], 
        capture_output=False,
        shell=False,
    )