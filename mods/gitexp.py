# source code disclosure through exposed .git folder
from mods import requester

def git_exposed(url, header):
    founds = []
    path = [".git",".git/",".gitignore",".git/logs/",".git/HEAD",".git/logs/HEAD",".git/index",".git/config"]

    for i in path:
        urlht = url + "/" + i

        try:
            req = requester.req_code(urlht, header)
            print(req)

            if req != 404:
                ff = "> "+ urlht + " " + req
                founds.append(ff)
        except:
            pass

    if len(founds) >= 1:
        print("\n[\033[1;33m!\033[0;0m] - .git folder")
        for it in founds:
            print(it)