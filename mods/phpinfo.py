from mods import requester

def phpinfo(url, header):
    founds = []
    path = ['phpinfo.php','PhpInfo.php','PHPinfo.php','PHPINFO.php','phpInfo.php','info.php','Info.php','INFO.php',
            'test.php?mode=phpinfo','index.php?view=phpinfo','index.php?mode=phpinfo','TEST.php?mode=phpinfo',
            '?mode=phpinfo','?view=phpinfo','install.php?mode=phpinfo','INSTALL.php?mode=phpinfo','phpversion.php',
            'admin.php?mode=phpinfo','phpVersion.php','test1.php','test.php','test2.php','phpinfo1.php','info1.php',
            'phpInfo1.php','PHPversion.php','x.php','xx.php','xxx.php']



    for i in path:
        urlht = "http://"+url+"/"+i
        get = requester.req_code(urlht,header)
        if get == 200:
            founds.append(i)
        else:
            pass
    if len(founds) >= 1:
        print("[\033[1;33m!\033[0;0m] - PHInfo!")
        for t in founds:
            print("-> ",t)








