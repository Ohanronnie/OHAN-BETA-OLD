import os, platform
try:
    import requests
except:
    os.system('pip install requests')

bit = platform.architecture()[0]
if bit == '32bit':
    import Random
    
elif bit == '64bit':
    import Sarfraz32
