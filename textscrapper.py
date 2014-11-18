import base64

if __name__=="__main__":
    fil=open("allhost_proxy_clear.dat","r")
    fil_out=open("allhost_proxy_clear_out.dat","w")
    b=None
    masterlist=[]
    for a in fil:

        if a[0:6]=="Proxy ":
            b=next(fil)
        if b[0:6]=="Proxy ":
            a=b
            b=next(fil)
        if b[0:6]=="Proxy ":
            a=b
            b=next(fil)
        a=a[7:-1]
        try:
        	usrpass=base64.b64decode(b.split(" ")[-1])
        except TypeError :
        	continue
        if usrpass not in masterlist:
            masterlist.append(usrpass)
            usrpass=usrpass.split(":")
            try: 
                print "Proxy:%s  Username:%s Password:%s\n"%(str(a),usrpass[0],usrpass[1])
                fil_out.write("Proxy:%s  Username:%s Password:%s\n"%(str(a),usrpass[0],usrpass[1]))
            except IndexError:
                print b,usrpass
    fil.close()
    fil_out.close()
