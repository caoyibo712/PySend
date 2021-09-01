# Echo client program

  # The remote host   
path=input('PATH')
key=input('KEY')
with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST36(key), 9999))

    f=makefile('rb')
    F=open(path ,'wb')
while True:
  line=f.readline()
    if line.strip()=='quit':
      break
    else:
      F.write(line)
F.flush()
F.close()
f.close()
















