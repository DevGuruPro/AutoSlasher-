import glob
import ntpath
import os
import platform


_cur_dir = os.path.dirname(os.path.realpath(__file__))

ui_folders = [
    _cur_dir,
    os.path.join(_cur_dir, 'dialog')
]


RC_NAME = 'res'


if __name__ == '__main__':

    for ui_folder in ui_folders:
        for ui_file in glob.glob(os.path.join(ui_folder, '*.ui')):
            name = ntpath.basename(ui_file).split('.')[0]
            py_file = os.path.join(ui_folder, f'ui_{name}.py')
            os.system(f"pyside6-uic {ui_file} > {py_file}")

    os.system(f"pyside6-rcc -o {_cur_dir}/{RC_NAME}_rc.py {_cur_dir}/{RC_NAME}.qrc")

    # Fix path issue of the RC file.
    for ui_folder in ui_folders:
        for rc in glob.glob(os.path.join(ui_folder, 'ui_*.py')):
            if platform.system() == 'Linux':
                os.system(f"sed -i -- \"s/import {RC_NAME}_rc/import ui.{RC_NAME}_rc/g\" {rc}")
            else:
                with open(rc, "r") as sources:
                    lines = sources.readlines()
                with open(rc, "w") as sources:
                    for line in lines:
                        line = line.replace(f"import {RC_NAME}_rc", f"import ui.{RC_NAME}_rc")
                        sources.write(line.replace(f"from displayboard import DisplayBoard", f"from widget.displayBoard import DisplayBoard"))
