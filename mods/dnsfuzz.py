from mods import requester

def dnsfuzz(url, header):
    listt = []
    arq = open("mods/db/dnsfuzz.txt").read()
    arq = arq.splitlines()
    for i in arq:
        try:
            urlht = "http://"+i+"."+url
            rc = requester.req_code(urlht,header)
            if rc == 200:
                listt.append(i)
            if rc == 300:
                listt.append(i)
            if rc == 301:
                listt.append(i)
            if rc == 302:
                listt.append(i)
            else:
                pass
        except:
            pass

    if len(listt) >= 0:
        pass
    else:
        print("DNS FUZZ:")
        for item in listt:
            print(item)


