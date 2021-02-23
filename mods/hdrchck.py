#Check Headers
import socket
import requests

def header(urlht,header):
    h = requests.get(urlht,headers=header)

    urlsplit = urlht.split("/")
    try:
        ip = socket.gethostbyname(urlsplit[2])
    except:
        pass
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)

        print("\nProtocols:")
        print("IP: ",ip)
        code = client.connect_ex((ip, 80))
        if code == 0:
            print("[\033[1;34mInfo\033[0;0m] 80 HTTP Opened.")
        else:
            pass
        code = client.connect_ex((ip, 443))
        if code == 0:
            print("[\033[1;34mInfo\033[0;0m] 443 HTTPS Opened.")
        else:
            pass

    except:
        pass

    def ucm(headers):
        common = ("host", "server", "age", "cookie", "pragma", "accept", "allow",
                  "authorization", "connection", "cache-control", "date", "etag",
                  "expires", "expect", "from", "via", "location", "host", "keep-live",
                  "if-match", "p3p", "proxy-authenticate", "proxy-authorization", "range",
                  "referer", "set-cookie", "te", "trailer", "vary", "warning", "www-authenticate",
                  "x-powered-by", "powered-by", "x-pad", "mime-version", "proxy-connection", "status",
                  "public", "dav", "nncoection", "dasl", "x-aspbet-version", "whisker", "user-agent", "upgrade",
                  "transfer-encoding", "retry-after", "max-forwards", "last-modified", "if-range", "if-none-match",
                  "if-modified-since", "if-unmodified-since", "content-type", "content-range", "content-md5",
                  "content-location",
                  "content-language", "link", "content-encoding", "content-length", "accept-charset",
                  "accept-encoding", "accept-language", "accept-ranges", "x-mod-pagespeed", "x-frame-options",
                  "x-xss-protection", "content-security-policy", "strict-transport-security")

        print("\nParsing headers:")
        for uni in common:
            try:
                print(uni, ":", headers[uni])
            except:
                pass

    def dvuln(headers):
        print("\nMissing Headers:")
        if 'x-xss-protection' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'X-XSS-Protection' - XSS Vulnerable.")

        if 'content-type' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'Content-type' header.")

        if 'content-security-policy' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'Content-Security-Policy' - Can be accessed over HTTP.")

        if 'x-frame-options' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'X-Frame-Options' - Might there a Clickjacking Vulnerability.")

        if 'strict-transport-security' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'Strict-Transport-Security' - Connection Might be Sniffed.")

        if 'x-content-type-options' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'X-Content-Type-Options' - MIME sniffing.")

        if 'public-key-pins' not in headers:
            print("[\033[1;34mInfo\033[0;0m] Missing 'Public-Key-Pins'.")

    def ck(req):
        try:
            ck = req.cookies
            if len(ck) == 0:
                pass
            else:
                print("\nCookies:")
                for coo in ck:
                    print("Name:", coo.name)
                    print("Value:", coo.value)
                    print("Port:", coo.port)
                    print("Path:", coo.path)
                    print("Secure:", coo.secure)
                    print("Expires:", coo.expires)
                    print("Domain:", coo.domain)
                    print("Version:", coo.version)
                    print("Discard:", coo.discard)
                    print("RFC:", coo.rfc2109)
        except:
            pass
    req = requests.get(urlht, headers=header)
    headers = req.headers
    ucm(headers)
    dvuln(headers)
    ck(req)