# Echo server program
key=key36(host)
host =gethostbyname(gethostname()) 

def _send(paths):
    pathl=paths.split(',')
    for path in pathl:
        sendcore(path)
    print('{k}[0-{n}]'.format(key,
      

def sendcore(path):
    gobal key,host

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, 9999))
        s.listen(1)
        conn, addr = s.accept()

        with conn as c:
            #Connected by ''addr''
            f=c.makefile（'w')
            F=open(path,'r')

    for line in F.readlines():
        f.write(line) 

    f.flush()
    F.close()
    f.close()
