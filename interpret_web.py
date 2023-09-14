import subprocess
import sys

class WebUpdater:
    def __init__(self):
        self.packages = ['package1', 'package2']  # Replace with actual package names

    def check_updates(self):
        updates = {}
        for package in self.packages:
            latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(package)], capture_output=True, text=True))
            latest_version = latest_version[latest_version.find('(from versions:')+15:]
            latest_version = latest_version[:latest_version.find(')')]
            latest_version = latest_version.replace(' ','').split(',')[-1]

            current_version = str(subprocess.run([sys.executable, '-m', 'pip', 'show', '{}'.format(package)], capture_output=True, text=True))
            current_version = current_version[current_version.find('Version:')+8:]
            current_version = current_version[:current_version.find('\n')].replace(' ','')

            if latest_version != current_version:
                updates[package] = latest_version
        return updates

    def fetch_updates(self):
        updates = self.check_updates()
        if updates:
            for package, version in updates.items():
                subprocess.run([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(package, version)])