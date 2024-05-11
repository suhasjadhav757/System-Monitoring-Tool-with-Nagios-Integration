import subprocess
import sys

def run_monitoring_script():
    try:
        output = subprocess.check_output(["python", "monitor.py"], stderr=subprocess.STDOUT)
        print(output.decode())
        return True
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
        return False

if __name__ == "__main__":
    if run_monitoring_script():
        sys.exit(0)  # OK status
    else:
        sys.exit(2)  # Critical status
