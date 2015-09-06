import base64,sys

if __name__=="__main__":

    fil=open(str(sys.argv[1]),"r")
    fil_out=open(str(sys.argv[2]),"a")
    fil_out_key=open(str(sys.argv[3]),"a")
    b=None
    masterlist=[]
    i=0

    for a in fil:
    	#print a
        if a[0:9]=="Proxy-AIP":
            b=next(fil)
        #print b
        while b[0:9] != "Proxy-Aut":
            a=b
            b=next(fil)
        a=a[10:-1]
        #print a
        try:
        	usrpass=base64.b64decode(b.split(" ")[-1])
        except TypeError :
        	continue
        if usrpass not in masterlist:
            masterlist.append(usrpass)
            usrpass=usrpass.split(":")
            #print usrpass
            if usrpass[0]!='' and usrpass[0]!='None' :
                try: 
                	#print a
                	#print usrpass
                    #print "Username:%s Password:%s Proxy:%s  \n"%(usrpass[0],usrpass[1],str(a))
                    fil_out.write("Proxy:%s Username:%s Password:%s\n"%(str(a),usrpass[0],usrpass[1]))
                    fil_out_key.write('"http://%s:%s@%s/"\n'%(usrpass[0],usrpass[1],str(a)))
                except IndexError:
                    #print a,b,usrpass
                    print a,b,usrpass
    fil.close()
    fil_out.close()
    fil_out_key.close()
