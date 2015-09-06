import urllib2,urllib,sys
from urllib2 import URLError
import threading
from time import time
THREAD_COUNT=750


class proxyTestThread(threading.Thread):
    def __init__(self,port_no):
        threading.Thread.__init__(self)
        self.port_no=port_no
    def run(self):
        proxy_tester(self.port_no)

    
def proxy_tester(port_no):
    #print "Testing: "+pxy_url
    
    try:
        response = urllib2.urlopen('http://portquiz.net:'+str(port_no)+'/')
        datum = response.read()
        print response.code
        if response.code == 200:
            print "Found: "+str(port_no)+"\n"
            #print "Found: "+pxy_url
        response.close()
    except urllib2.HTTPError as k:
        print k
        pass
    except URLError:
        #print "Timed Out :"+str(port_no)
        pass
if __name__=="__main__":

    array = []
    for i in xrange (1,65535):
        array.append(proxyTestThread(i))
    print "ADDED"
    running_array=[]
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
            thread_runner.join()
            running_array.remove(thread_runner)
            k=k-1



    