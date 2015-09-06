import urllib2,urllib,sys

def proxy_url_generator(pxy_url):
    proxy_url=pxy_url.split("@")[-1][:-1]
    print proxy_url
    k=pxy_url.split("@")[0].split(":")
    print  k
    user_name=k[1][2:]
    print urllib.quote(user_name)
    password=k[2]
    #print urllib.quote(password)


    proxy_str='http://'+user_name+":"+password+"@"+proxy_url
    return proxy_str
    
def proxy_tester(pxy_url):
    final_url=proxy_url_generator(pxy_url)
    proxy = urllib2.ProxyHandler({'http': final_url})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request('http://google.com')
    try:
        response = opener.open(req)
        datum = response.read()
        print response.code
        if response.code == 200:
            fil_out.write( "Found: "+proxy_url+" : "+final_url)
            print "Found: "+proxy_url+" : "+final_url
        response.close()
    except urllib2.HTTPError as k:
        #print k
        pass
if __name__=="__main__":

#    fil=open(str(sys.argv[1]),"r")
#    fil_out=open(str(sys.argv[2]),"a")

#    for a in fil:
#        a=a[1:-2]
#        proxy_tester(a)
    proxy_tester("http://068.1525:passcode@10.1.1.19:80/")