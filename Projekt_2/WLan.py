import network
import time

class WLan:
    def __init__(self):
    #rp2.country("DE") # Jedes Land hat andere Vorschiften für das W-Lan (z.B. Signalstärke, verfügbare Kanäle) und stellt diese entsprechend ein. Ist aber optional.
    self.wlan = network.WLAN(network.STA_IF)
    self.wlan.active(True)
    self.wlan.connect("RoboStudio2GHz", "robo-1958!")
    
    # Der Aufbau einer Verbindung dauert eine Weile und es werden unterumständen mehrer Versuche benötigt bis eine Verbindung hergestellt wurde.
    while not self.wlan.isconnected() and self.wlan.status() >= 0:
        print("Verbinde, bitte warten...")
        time.sleep(1) # Pause zwische 2 Verbindungsversuche
        
    print(self.wlan.ifconfig())
    print("Bin online...")
    return self.wlan