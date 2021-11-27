import os
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Helicopter body
heli_body = '******************  \n\t\t  A\n' + '\t' + '─' * 20 + '\n' + '─' * 8 + '\t\t{}  \\\n' + '\t\\\t\t     \\\n' + \
            '\t \\\t\t      ' + '\\\n' + '\t  ( ' + '─' * 18 + ' )\n' + '\t\t*\t*'
heli_body_r = '\t\t  ******************  \n\t\t  A\n' + '\t' + '─' * 20 + '\n' + '─' * 8 + '\t\t{}  \\\n' + \
              '\t\\\t\t     \\\n' + '\t \\\t\t      ' + '\\\n' + '\t  ( ' + '─' * 18 + ' )\n' + '\t\t*\t*'

# list of frames
heli = [heli_body, heli_body_r]

print('This program is here to stay forever. Press Ctrl & C to terminate. \n\n\n\n\n\n\n')
i = 0
while True:
    index = i % 2

    print("".join(heli[index]))
    print('\n\n Helicopter helicopter\n'
          ' Para kofer, para kofer')

    # delay
    time.sleep(.01)
    i += 1

    # clear screen
    cls()
