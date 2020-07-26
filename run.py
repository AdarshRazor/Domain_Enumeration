#Run only once for setting up
import os

cwd = os.getcwd()
dnsdumpster = "%s/API-dnsdumpster.com"%cwd

os.system("python3 -m pip install -r requirements.txt")

os.chdir(dnsdumpster)

os.system("python3 -m pip install .")