from mods import requester
def backup(url,header):
    founds = []
    path = ['/backup.bak','/bk.bak','/backup/backup.bak','/backup/bk.db','/cobalt.db','/greysc.db','/mongo-db/bak-files/backup.bak',
            '/back/back.db','/back.db','/buck.bak','/admin/backup.db','/admin/backup.bak','/manager/backup.db','/mgr/back.bak',
            '/backup/','/.backup','/.backup/backup.db','/backup/backup.sqlite3','/backup.sqlite3','/backup.bak.sqlite3',
            '/employees/backup.bak','/users/backup.db','/db/main.mdb','/backup.mmdb','/wcx_ftp.ini','/ws_ftp.db','/flashFXP.bak',
            '/backup.bak.csv','/eudora.csv','/admin.dat','/server-logs.db','/servlet.bak','/admin/logs/backup.db','/employees.bak',
            '/sqlite-backup.db','/postgresql.bak','/.backup/','/passlistdb','/passlist.mmdb','/auth_user_files.db',
            '/administrators.pwd','/admin.mdb','/backup/backup.mmdb','/.backup/backup.mmdb','/_backup/backup.bak','/_backup.bak',
            '/_backup.mmdb','/_backup.dat']

    for i in path:
        urlht = "http://"+url+i
        get = requester.req_code(urlht,header)
        if get == 200:
            founds.append(i)
        else:
            pass
    if len(founds) >= 1:
        print("[\033[1;33m!\033[0;0m] - Backup found!")
        for t in founds:
            print("-> ",t)






