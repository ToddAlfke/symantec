#### ##################################################
import subprocess
import glob


for project in glob.glob('site-source/*'):
    subprocess.call('scrapy crawl charlotte', shell=True, cwd=project)
