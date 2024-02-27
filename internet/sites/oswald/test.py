import os
import json

def link_loader():
    os.system("cd sites/oswald && scrapy crawl oswald -O websites.json")
    f = open('sites/oswald/websites.json')
    data = json.load(f)
    links_list = []
    for i in data:
        link = list(i.keys())[0]
        links_list.append(link)
    return links_list

# import subprocess
# process = subprocess.Popen(['workon','pgrank', '&&', 'scrapy','crawl','oswald'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# stdout, stderr =  process.communicate()
# # print(stdout)