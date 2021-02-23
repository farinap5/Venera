from mods import requester

def multi_index(url,header):
    found = []
    arq = open("mods/db/allindex.txt").read()
    arq = arq.splitlines()
    for i in arq:
        urlht = "http://" + url + "/" + i
        get = requester.req_code(urlht,header)
        if get == 200:
            found.append(urlht)
        else:
            pass

    if len(found) != 0:
        for it in found:
            print("\n[\033[1;33m!\033[0;0m] Index page found:",it)
    else:
        pass