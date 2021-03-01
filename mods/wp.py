import requests
import re


def stur(urlht, header):
    paths = ['sitemap.xml','wp-admin/admin-ajax.php','wp-login.php','robots.txt','xmlrpc.php','wp-admin/install.php',
             'readme.html','license.txt','licencia.txt']
    for ru in paths:
        ret = urlht + "/" + ru
        req = requests.get(ret, headers=header)
        if req.status_code == 200 or 301:
            print("[\033[1;33m!\033[0;0m]", ret)
        else:
            pass
def findbu(urlht,header):
    backups = ['wp-config.php~', 'wp-config.php.txt', 'wp-config.php.save', '.wp-config.php.swp', 'wp-config.php.swp',
               'wp-config.php.swo', 'wp-config.php_bak', 'wp-config.bak', 'wp-config.php.bak', 'wp-config.save',
               'wp-config.old', 'wp-config.php.old', 'wp-config.php.orig', 'wp-config.orig', 'wp-config.php.original',
               'wp-config.original', 'wp-config.txt']

    for uni in backups:
        ret = urlht + "/" + uni
        req = requests.get(ret, headers=header)
        if req.status_code == 200:
            print("[\033[1;33m!\033[0;0m]",ret)
        else:
            pass
def uenum(urlht,header):
    us = ["1","2","3","4","5"]
    for u in us:
        try:
            ret = urlht + "/?author=" + u
            req = requests.get(ret, headers=header)
            user = req.url
            user = user.split("/")
            print("[\033[1;33m!\033[0;0m] User Found:",user[4])
        except:
            break
def getplugs(urlht,header):
    lplug = []
    req = requests.get(urlht, headers=header).text
    plug = re.findall(r'wp-content/plugins/(.*?)/',req)
    for p in plug:
        p = p.split("/")
        lplug.append(p[0])

    lplug2 = []
    for u in lplug:
        if u not in lplug2:
            lplug2.append(u)
        else:
            pass

    print("Plugins----------")
    for un in lplug2:
        print(un)

def gethemes(urlht,header):
    themes = []
    req = requests.get(urlht, headers=header).text
    the = re.findall(r'wp-content/plugins/(.*?)/',req)
    for t in the:
        t = t.split("/")
        themes.append(t[0])
    themes2 = []
    for u in themes:
        if u not in themes2:
            themes2.append(u)
        else:
            pass

    print("Themes-----------")
    for ttt in themes2:
        print(ttt)

def getver(urlht,header):
    print("Version----------")
    print("Trying to get version.")
    urlv1 = urlht + "/wp-links-opml.php"
    try:
        req = requests.get(urlv1, headers=header).text
        ver = re.findall(r'generator="WordPress/(.*?)"',req)
        for v in ver:
            print("WordPress",v)
    except:
        pass
    #/feed/
def wp(urlht,header):
    req = requests.get(urlht, headers=header).text
    if "/wp-content/" and "/wp-includes/" in req:
        print("\n[\033[1;34mInfo\033[0;0m] WordPress found:")
        findbu(urlht,header)
        uenum(urlht,header)
        getplugs(urlht,header)
        stur(urlht,header)
        gethemes(urlht,header)
        getver(urlht,header)
        print("---------------------------")
    else:
        pass