# Die main.py bootet beim Start des Pico automatisch

from GrowLed import GrowLed


def main():
    light_1 = GrowLed()
    print("Starting loop...")
    while True:
        light_1.blinkLed()
        
if __name__ == "__main__":
    main()