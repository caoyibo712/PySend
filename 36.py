def _host36(key):
    key=t10(key)
    key=hex(key)
    keyArr=key[3:].split('')
    count=0
    for char in keyArr[]:
        if a % 2 == 0 :
            outputArr.apppend(''.join(['0x',last,char]))
        else :
            last=char
    outputArr[]=[int(x,16) for x in outputArr[]]
    return '.'.join(outputArr[])
    
def _key36(host):
    #g-36
    hos[]=host.replace(' ','').split('.',)
    host.join(
["0x"]+[hex( int(x) )[3:] for x in hos ] ) 
    host=int(host,16)
    return t36(host)

num_36l=[chr(x) for x in  range(48,57) ][chr(y) for y in range(97,122)]
num_36d=dict(zip(num_36l,range(0,36)))

def _t36(value):
    val_l=[]
    while value>35:
        a,value= value//36,value%36
        val_l.append(a)
    val_l.reverse()
    
    return [num_36l[x] for x in val_l]

def _t10(value):
    val_10=0
    for d,c in value,range(len(value)):
        val_10+=num_36d[d]*(36**c)
    return val_10