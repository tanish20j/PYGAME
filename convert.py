import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
executables=[cx_Freeze.Executable("game.py")]
cx_Freeze.setup(
    name="Tic Tac Toe",
    options={"build_exe": {"packages":["pygame","numpy"],
                           "include_files":["about.png","O.png","X.png","quit.png","start1.png"]}},
    executables = executables
    )
