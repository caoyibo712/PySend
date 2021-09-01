# Echo server program

def send(path):
    host =  gethostbyname(gethostname())

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
    return key36(host)