import os, platform, time, sys
os.system('git pull')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests futures==2 > /dev/null')
import F_enc
