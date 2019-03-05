#### ##################################################
import subprocess
import glob


for project in glob.glob('site-source/*'):
    subprocess.call('scrapy crawl example', shell=True, cwd=project)
