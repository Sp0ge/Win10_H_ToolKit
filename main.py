## -*- coding: utf-8 -*-

from userbrute.userbrute import *
exit = False
command = ''
command_list = ['help - list commands','userbrute - local user bruteforce','quit or exit - close programm']
print('help - "list commands"')
while not(exit):
    if command == "exit" or command == "quit":
        exit = True
        
    elif command == 'userbrute':
        args = []
        os.system('net users')
        a = str(input("Input target username: "))
        args.append(a)
        a = 'N'
        a = str(input("Use custom wordlist? y/N: "))
        if a == 'y' or a == 'Y':
            a = str(input("Wordlist path: "))
        else:
            a = 'userbrute/default_passlist.txt'
        args.append(a)
        userbruteforce(args)
        
    elif command == 'help':
        for command in command_list:
            print(command)
        
        
        
    command = str(input('WinTK>> ' ))
    
