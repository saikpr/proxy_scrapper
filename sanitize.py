import re,sys

if __name__=="__main__":
    fil=open(str(sys.argv[1]),"r")
    fil_out=open(str(sys.argv[2]),"w")
    for a in fil:

        m = re.search('Proxy:(.+?)Username:(.+?)Password:(.+?)$', a)
        try:
            k=str(m.group(3))
            password=k[0]+"*"*(len(k)-3)+k[-2:]
            fil_out.write("Proxy:%s Username:%s Password:%s\n"%(m.group(1),m.group(2),password)) 
        except AttributeError:
            print "AttributeError@"+str(m)
    fil.close()
    fil_out.close()