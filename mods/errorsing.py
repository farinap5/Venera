from mods import requester

def errorsig(url,header):
    lssing = ["<title>Page not found &middot; GitHub Pages</title>","<address>Apache/","<center>nginx"]

    sigs = {
        "<title>Page not found &middot; GitHub Pages</title>":"GitHub pages",
        "<address>Apache/":"Apache error page.",
        "<center>nginx":"Nginx error page."
    }
    urlht = "http://"+ url +"/404-error.html"
    geterr = requester.req_content(urlht,header)
    getcode = requester.req_code(urlht,header)
    for i in lssing:
        if i in geterr:
            print("[\033[1;34mInfo\033[0;0m] - Error From:",sigs[i],getcode)
