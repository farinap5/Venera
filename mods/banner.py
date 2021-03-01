from mods import requester
import re
def banner(ver):
    header = {"User-Agent": "Venera/1.0"}
    urlht = "https://raw.githubusercontent.com/farinap5/Venera/master/vnr.py"
    lver = requester.req_content(urlht,header)
    a = re.findall(r'"(.*)"#',lver)

    if ver != a[0]:
        ch = "[\033[1;33m!\033[0;0m] - Update avaliable."
    else:
        ch = " "

    print("""
__    _ ____________________________________
\ \  | |   ___   _  _    ___   _  _   __ _  |
 \ \ | |  / _ \ | \| |  / _ \ | |//  / _' | |
  \ \| | |  __/ |  \ | |  __/ | |/  | (_| | |
   \___|  \___| |_| _|  \___| |_|    \__,_| |
   -----------------------------------------{}
   {}
     """.format(ver,ch))