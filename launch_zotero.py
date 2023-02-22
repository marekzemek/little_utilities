'''
Zotero needs an absolute path for its library.
This script makes it easier to launch zotero when the drive letter changes. It:
	1) Finds the path to the Zotero library
	2) Finds the path to the zotero EXE and user preferences folder
	3) Creates a user.js file with the current path to the Zotero library
	4) Launches Zotero

compile this script by running the following command in terminal:
> pyinstaller --onefile launch_zotero.py --icon=ZoteroStandalonePortable\App\AppInfo\appicon.ico

Or, if using a venv, make and launch a batch file containing:
@echo off
cmd /k ".venv\Scripts\python.exe launch_zotero.py"
'''

import os
import subprocess
import time
import json

SETTINGS_FILENAME = 'launch_zotero_settings.json'

DEFAULTS = {'zotero_folder': 'ZoteroStandalonePortable', 
            'zotero_exe': 'ZoteroStandalonePortable.exe',
            'library_name': 'Zotero_dir',
            'profile_name': 'profile'
            }

def find_dir(name, path):
    # https://stackoverflow.com/questions/1724693/find-a-file-in-python
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)


def set_settings(sett):
    with open(SETTINGS_FILENAME, 'w') as file:
        json.dump(sett, file, indent=4)


def get_settings():
    if os.path.isfile(SETTINGS_FILENAME):
        with open(SETTINGS_FILENAME) as settings_file:
            sett = json.load(settings_file)
        print('Settings loaded from JSON file:', os.linesep, sett)
    else:
        print('Settings file not found, using defaults...')
        sett = DEFAULTS
        set_settings(sett)
    return sett


def main():
    sett = get_settings()
    try:
        lib_dir = find_dir(sett['library_name'], os.getcwd()).replace("\\", "\\\\")
        print('Zotero library directory:', lib_dir)
        zotero_dir = find_dir(sett['zotero_folder'], os.getcwd()) # find paths to zotero folder
        # get filepath to user.js within the profile folder inside the data folder of zotero
        user_filepath = os.path.join(find_dir(sett['profile_name'], zotero_dir), 'user.js')
        print('Writing library directory to', user_filepath)
        with open(user_filepath, 'w') as user_file: # change path to library in user preferences
            user_file.write(f'user_pref("extensions.zotero.dataDir", "{lib_dir}" );')
        print('Launching Zotero...')
        subprocess.Popen('"' + os.path.join(zotero_dir, sett['zotero_exe']) + '"')
        print('All done!')
        time.sleep(3)
    except Exception as e:
        print('Something went wrong:', e)
        print('There might be something wrong with the settings.')
        print('Try editing the file', SETTINGS_FILENAME)
        print('It should look something like this:', os.linesep, json.dumps(DEFAULTS, indent=4))
        input('Press ENTER to quit')

if __name__ == '__main__':
    main()

