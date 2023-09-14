import subprocess

class E2B:
    def __init__(self):
        pass

    def execute_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if error:
            raise Exception('Error executing command: ' + str(error))
        return output.decode('utf-8')