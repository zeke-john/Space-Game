import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup( name= "Space Game", options = {"build_exe": {"packages": ["turtle"] ,"include_files":["res/images/wp3284832.gif, res/images/3nd_enemy.gif, res/images/player.gif, res/images/enemy.gif, res/images/boom.gif, res/images/2nd_enemy.gif, res/sounds/cartoon016.wav, res/sounds/cartoon007.wav, res/sounds/battle003.wav"]}}, executables = executables)

