import re

if __name__=="__main__":
	fil=open("proxy_clear_2.txt","r")
	fil_out=open("sanitizedpassword.txt","w")
	for a in fil:

		m = re.search('Proxy:(.+?)Username:(.+?)Password:(.+?)$', a)
		k=str(m.group(3))
		password=k[0]+"*"*(len(k)-3)+k[-2:]
		fil_out.write("Proxy:%s  Username:%s Password:%s\n"%(m.group(1),m.group(2),password)) 
	fil.close()
	fil_out.close()