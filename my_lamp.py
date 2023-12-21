from yeelight import Bulb
from yeelight import discover_bulbs
import time
import keyboard


def get_current_color(ip):
    bulb = Bulb(ip)
    properties = bulb.get_properties()

    rgb_value = int(properties["rgb"], 16)

    # Extract RGB values from the integer
    r = (rgb_value >> 16) & 255
    g = (rgb_value >> 8) & 255
    b = rgb_value & 255

    return r, g, b


bulbs = discover_bulbs()


# Assuming there's only one Yeelight bulb, you can select the first one
yeelight_ip = bulbs[0]['ip']


def set_color(ip, color):
    bulb = Bulb(ip)
    bulb.turn_on()
    bulb.set_rgb(*color)


def option_off(ip):
    bulb = Bulb(ip)
    bulb.turn_off()


def display_menu():
    print("Welcome to the Menu:")
    print("1. Reading Mode")
    print("2. Party Mode")
    print("3. Patriot Mode 3")
    print("4. I CAN'T SEE IN THIS FUCKING ROOM mode")
    print("5. Turn Off")
    print("6. Exit")


def option_reading():
    print("Rading Mode Activated")
    set_color(yeelight_ip, (81, 41, 104)) 


def option_party():
    print("Party Mode Activated.")
    r, g, b = get_current_color(yeelight_ip)
    print(f"Current RGB color: ({r}, {g}, {b})")


def option_patriot():
    print("Nothing happens yet")
    

def option_see():
    print("Bright Light Activated.")


def main():

    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            option_reading()
        elif choice == '2':
            option_party()
        elif choice == '3':
            option_patriot()
        elif choice == '4':
            option_see()
        elif choice == '5':
            option_off()
        elif choice.lower() == 'exit' or choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
