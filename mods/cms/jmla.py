import requests
def stuc(urlht,header):
    found = []
    path = ['/robots.txt.dist','/web.config.txt','/joomla.xml','/LICENSE.txt','/README.txt','/htaccess.txt',
            '/LICENSES.php','/configuration.php-dist','/CHANGELOG.php','/CHANGELOG.txt','/COPYRIGHT.php','/CREDITS.php',
            '/language/en-GB/en-GB.xml','/MANIFEST.xml','/manifest.xml','/error_log','/plugins/index.html','/administrator']

    for ru in path:
        ret = urlht + ru
        req = requests.get(ret, headers=header)
        if req.status_code == 200 or 301:
            ff = "[\033[1;33m!\033[0;0m] - " + ret + " - " + req.status_code
            found.append(ff)
        else:
            pass
    if len(found) != 0:
        print("Joomla Enum----")
        for i in found:
            print(i)
    else:
        pass
def check(urlht,header):
    fp1 = '<meta name="generator" content="Joomla!'

    req = requests.get(urlht, header=header).text

    if fp1 in req:
        print("[\033[1;33m!\033[0;0m] - Joomla Found")
        stuc(urlht, header)
    else:
        pass

def joomla(urlht,header):
    check(urlht,header)

