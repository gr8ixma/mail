import os,sys,requests,json

banner = """ 
\033[1;35;40m
____________________██████
_________▓▓▓▓____█████████
__ Ixma▓▓▓▓▓=▓____▓=▓▓▓▓▓
__ ▓▓▓_▓▓▓▓░●____●░░▓▓▓▓
_▓▓▓▓_▓▓▓▓▓░░__░░░░▓▓▓▓
_ ▓▓▓▓_▓▓▓▓░░♥__♥░░░▓▓▓
__ ▓▓▓___▓▓░░_____░░░▓▓
▓▓▓▓▓____▓░░_____░░▓
_ ▓▓____ ▒▓▒▓▒___ ████
_______ ▒▓▒▓▒▓▒_ ██████
_______▒▓▒▓▒▓▒ ████████
_____ ▒▓▒▓▒▓▒_██████ ███
_ ___▒▓▒▓▒▓▒__██████ _███
_▓▓X▓▓▓▓▓▓▓__██████_ ███
▓▓_██████▓▓__██████_ ███
▓_███████▓▓__██████_ ███
_████████▓▓__██████ _███
_████████▓▓__▓▓▓▓▓▓_▒▒
_████████▓▓__▓▓▓▓▓▓
_████████▓▓__▓▓▓▓▓▓
__████████▓___▓▓▓▓▓▓
_______▒▒▒▒▒____▓▓▓▓▓▓
_______▒▒▒▒▒ _____▓▓▓▓▓
_______▒▒▒▒▒_____ ▓▓▓▓▓
_______▒▒▒▒▒ _____▓▓▓▓▓
________▒▒▒▒______▓▓▓▓▓
________█████____█████
_'▀█║────────────▄▄───────────​─▄──▄_
──█║───────▄─▄─█▄▄█║──────▄▄──​█║─█║
──█║───▄▄──█║█║█║─▄║▄──▄║█║─█║​█║▄█║
──█║──█║─█║█║█║─▀▀──█║─█║█║─█║​─▀─▀
──█║▄║█║─█║─▀───────█║▄█║─▀▀
──▀▀▀──▀▀────────────▀─█║
───────▄▄─▄▄▀▀▄▀▀▄──▀▄▄▀
──────███████───▄▀
──────▀█████▀▀▄▀
────────▀█▀
                                                      
\033[0;37;40m
\033[1;32;40m
Tool Information :
- Tool Name : Ixma Email Validator
- Creator : Rabbit
- Telegram : @ixmazeco
- Version : 1.0 [FREE]

Halo : U
\033[0;37;40m
"""
api = "https://soulapizy.000webhostapp.com/emailvalidator/"

#Main
print(banner)

#Open Number List
filename = input("Input Email List (Exemple: list.txt) : ")
try:
    file = open(filename,"r")
except:
    sys.exit("[!] Error. No File Exist")
combo = file.readlines()
file.close()

for line in combo:
    line = line.strip()
    data = {"email": line}
    try:
        response = requests.post(api, data=data).text
    except:
        print("[!] Stopped.")
        combo.append(line)
        break
    if "Success" in response:
        print('\r[\033[92m ' + response + ' \033[0m] ')
        open('hits.txt','a').write(str(line)+'\n')
        open('full-hits.txt','a').write(str('[ ' + response + ' ]')+'\n')
    elif "Bad" in response:
        print('\r[\033[91mBad\033[0m] ' + line)
    else:
        print('\r[\033[91mBan\033[0m] ' + line)

print("Done....")
