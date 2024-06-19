# Die main.py bootet beim Start des Pico automatisch
# Nach der LED starten wir das WLAN
'''
In Ihrem Code sorgt der Block if __name__ == "__main__": dafür, dass die Funktion main()
nur dann aufgerufen wird, wenn das Skript main.py direkt ausgeführt wird, nicht aber, wenn es
von einem anderen Skript importiert wird.
'''

from GrowLed import GrowLed
from WLan import Wlan


def main():
    light_1 = GrowLed()
    print("Starting loop...")
    internetVerbindung = WLan()
    while True:
        light_1.blinkLed()
        
if __name__ == "__main__":
    main()