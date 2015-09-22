from __future__ import print_function
import urllib2,urllib,sys
from urllib2 import URLError
import threading
from time import time
THREAD_COUNT=250
PROXY_TIMEOUT=50
JOIN_TIMEOUT=3
count_total=0
count_found=0
count_failed=0
class proxyTestThread(threading.Thread):
    def __init__(self,pxy_url,fil_out):
        threading.Thread.__init__(self)
        self.pxy_url=pxy_url
        self.fil_out=fil_out
    def run(self):
        proxy_tester(self.pxy_url,self.fil_out)

def proxy_url_generator(pxy_url):
    #Proxy:10.1.1.10:80 Username:002.9802 Password:kavita
    try:
        k=pxy_url.split(" ")
        proxy_url= k[0].split("Proxy:")[1]
        #print  k
        user_name=k[1].split("Username:")[1]
        #print urllib.quote(user_name)
        password=k[2].split("Password:")[1].split("\n")[0]
        #print urllib.quote(password)
        proxy_str='http://'+user_name+":"+password+"@"+proxy_url
        return proxy_str

    except IndexError:
        print ("Error with" +pxy_url)
        return None
def proxy_tester(pxy_url,fil_out):
    #print "Testing: "+pxy_url
    global count_found,count_failed
    proxy = urllib2.ProxyHandler({'http': pxy_url})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request('http://google.com')
    try:
        response = opener.open(req,timeout=PROXY_TIMEOUT)
        datum = response.read()
        #print response.code
        if response.code == 200:
            fil_out.write( "Found: "+pxy_url+"\n")
            print ("Found: "+pxy_url)
            count_found+=1
        else:
            count_failed+=1
        response.close()
    except urllib2.HTTPError as k:
        #print k
        count_failed+=1
        pass
    except :
        #print "Timed Out :"+pxy_url
        count_failed+=1
        pass
if __name__=="__main__":

    fil=open(str(sys.argv[1]),"r")
    fil_out=open(str(sys.argv[2]),"w")
    array = []
    for a in fil:
        final_url=proxy_url_generator(a)

        if final_url != None:
            # print (final_url)
            temp=proxyTestThread(final_url,fil_out)
            array.append(temp)
    print ("Appended Proxy Url")
    print ("Count "+str(len(array)))
    count_total=len(array)
    running_array=[]
    i=0
    print ("count_found / count_failed / count_total")
    while array!=[]:
        k=THREAD_COUNT
        while(k>0 and array!=[]):
            thread_runner=array[0]
            array.remove(thread_runner)
            thread_runner.start()
            running_array.append(thread_runner)
            k=k-1
        k=THREAD_COUNT
        while(k>0 and running_array!=[]):
            thread_runner=running_array[0]
            thread_runner.join(timeout=JOIN_TIMEOUT)
            if thread_runner.isAlive()==False:
                running_array.remove(thread_runner)
                k=k-1
                print(str(count_found)+"/"+str(count_failed)+"/"+str(count_total), end='\r')
