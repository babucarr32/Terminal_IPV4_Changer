import subprocess

def main():
    run = True
    while run:
        command = input('</> ')
        ON = ['on', 'ON', 'oN']
        OFF = ['off', 'OFF', 'ofF', 'Off']
        if command in OFF:
            subprocess.run(f'netsh interface ipv4 set address name="Ethernet" static 192.168.1.30 mask=255.255.255.0', capture_output=True,shell=True, text=True)
            print('Connection off!')
        elif command in ON:
            subprocess.run(f'netsh interface ipv4 set address name="Ethernet" source=dhcp', capture_output=True,shell=True, text=True)
            print('Connection on!')
        elif command == 'quit':
            quit()
        else:
            print('Invalid input!')
        
main()
