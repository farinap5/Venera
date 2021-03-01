from mods import requester
import re

def apache_about(urlht,header):
    h = requester.req_header(urlht, header)
    apch = h["Server"]
    getv = re.findall(r"[0-9].[0-9].[0-9]",apch)
    if len(getv) != 0:
        print("[\033[1;34mInfo\033[0;0m] - Apache Version:",getv[0])
    else:
        pass
    getsys = re.findall(r"[(].*[)]",apch)
    if len(getsys) != 0:
        print("[\033[1;34mInfo\033[0;0m] - Operating System:",getsys[0])
    else:
        pass

def apache_user_enum(url,header):
    ufounds = []
    l2 = ["~root","~toor","~bin","~daemon","~adm","~lp","~sync","~shutdown","~halt","~mail","~pop","~postmaster","~news","~uucp","~operator","~games", \
          "~gopher","~ftp","~nobody","~nscd","~mailnull","~ident","~rpc","~rpcuser","~xfs","~gdm","~apache","~http","~web","~www","~adm","~admin", \
          "~administrator","~guest","~firewall","~fwuser","~fwadmin","~fw","~test","~user","~sql","~data","~database"]
    for i in l2:
        urlht = url + "/" + i
        uf = requester.req_code(urlht, header)
        if uf == 200:
            ufounds.append(urlht)
        if uf == 302:
            ufounds.append(urlht)
        else:
            pass
    if len(ufounds) != 0:
        print("[\033[1;33m!\033[0;0m] - Apache users found:")
        for it in ufounds:
            print(it)
        else:
            pass

def apache_def_enum(url,header):
    founds = []
    l1 = [".htaccess",".htpasswd",".meta",".web","access_log","cgi","cgi-bin","cgi-pub","cgi-script","dummy","error", \
          "error_log","htdocs","httpd","httpd.pid","icons","logs","manual","phf","printenv","server-info","server-status", \
          "status","test-cgi","tmp"]
    for i in l1:
        urlht = url + "/" + i
        uf = requester.req_code(urlht,header)
        if uf == 200:
            founds.append(urlht)
        if uf == 302:
            founds.append(urlht)
        else:
            pass
    if len(founds) != 0:
        print("[\033[1;33m!\033[0;0m] - Apache Dir found:")
        for it in founds:
            print(it)
        else:
            pass
def apache_(urlht,header):
    h = requester.req_header(urlht,header)
    if "Apache" or "apache" in h["Server"]:
        print("\n[\033[1;34mInfo\033[0;0m] - Server: Apache")
        apache_about(urlht,header)

        url = urlht
        apache_def_enum(url,header)
        apache_user_enum(url,header)
    else:
        pass
