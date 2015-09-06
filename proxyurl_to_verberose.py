#clean.py
import sys
def proxy_url_generator(pxy_url):
    proxy_url=pxy_url.split("@")[-1][:-1]
    #print proxy_url
    k=pxy_url.split("@")[0].split(":")
    #print  k
    user_name=k[1][2:]
    #print urllib.quote(user_name)
    password=k[2]
    #print urllib.quote(password)
    proxy_str='http://'+user_name+":"+password+"@"+proxy_url
    print "Proxy:"+proxy_url +" Username:"+user_name+ " Password:"+password



if __name__=="__main__":

        fil=open(str(sys.argv[1]),"r")
        for a in fil:
            a=a[1:-2]
            final_url=proxy_url_generator(a)
