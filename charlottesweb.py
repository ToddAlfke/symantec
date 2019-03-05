#from packetstormsecurity import charlottesweb

#from subprocess import call
#call(["cd packetstormsecurity/", "python charlottesweb.py"])
#import os
#os.system('scrapy crawl charlotte')
#import os
#from subprocess import Popen
#Popen("scrapy crawl charlotte", shell=True, cwd="packetstormsecurity/")

#import os
#import subprocess, os

#projects = '/home/ubuntu/site-source/packetstormsecurity/'
#projects = [name for name in os.listdir(".") if os.path.isdir(name)]
#print(projects)

#subprocess.Popen('scrapy crawl charlotte', env=dict(os.environ, PATH=projects))

#Popen("scrapy crawl charlotte", shell=True, env=projects)


#### ##################################################
import subprocess
import glob


for project in glob.glob('site-source/*'):
    subprocess.call('scrapy crawl example', shell=True, cwd=project)


##################### this code yo!!!!!!!!!!!!!!!!!
