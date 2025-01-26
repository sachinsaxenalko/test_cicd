import platform
import subprocess
import random
import string
import time
import socket

from datetime import datetime

def write_to_file(filename, data):
  """
  Writes data to a specified file.

  Args:
    filename: The name of the file to write to.
    data: The data to write to the file. Can be a string or a list of strings.
  """
  try:
    with open(filename, 'a') as file:
      if isinstance(data, list):
        file.writelines(data)
      else:
        file.write(data)
    print(f"Data written successfully to {filename}")
  except IOError as e:
    print(f"An I/O error occurred: {e}")

def generate_random_name(length=10):
    """
    Generates a random string of the specified length.

    Args:
        length: The desired length of the random string.

    Returns:
        str: The generated random string.
    """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def get_machine_id():
    """
    Gets the machine ID of the current system.

    Returns:
        str: The machine ID, or None if it cannot be determined.
    """

    try:
        # Check for Linux distributions
        if platform.system() == 'Linux':
            with open('/etc/machine-id', 'r') as f:
                return f.read().strip()

        # Check for Windows
        elif platform.system() == 'Windows':
            cmd = 'wmic csproduct get uuid'
            output = subprocess.check_output(cmd, shell=True, text=True)
            lines = output.splitlines()
            if len(lines) > 1:
                return lines[1].strip()

        # Check for macOS
        elif platform.system() == 'Darwin':
            cmd = "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'"
            output = subprocess.check_output(cmd, shell=True, text=True)
            return output.strip()

    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

if __name__ == "__main__":
    cnt_count = 0
    while cnt_count < 20:
        time.sleep(2)
        machine_id = socket.gethostname()
        now = datetime.now()
        
            
        if machine_id:
            print(f"Machine ID: {machine_id}")
            print(f"Current TIme :", now.strftime("%Y-%m-%d %H:%M:%S"))
            random_number = random.randint(1, 100)

            print("Random number:", random_number) 
            random_name = generate_random_name()
            print(random_name)
            data = machine_id + "," + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "," +   str(random_number) +   "," + str(random_name) + "\n"
            filename = '/home/sachin/add_file.txt'
            write_to_file(filename,data)
        else:
            print("Could not determine machine ID.")
        cnt_count = cnt_count + 1