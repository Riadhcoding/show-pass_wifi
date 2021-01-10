import subprocess
print('\033[1;31mWIFI NAME                     \033[1;36m|  \033[1;36mPASSWORD')
print('\033[1;32m*'*45)
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:

        print ("\033[1;36m{:<30}|  \033[1;31m{:<}".format(i, results[0]))
        print('\033[1;32m*' * 45)
    except IndexError:
        print ("\033[1;36m{:<30}|  \033[1;31m{:<}".format(i, ""))

