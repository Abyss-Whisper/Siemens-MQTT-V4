#Este será o ponto de entrada do seu aplicativo. Ele inicializará a interface do usuário e o controlador.

import paho.mqtt.client as paho
import os
import ssl
from time import sleep
from random import uniform, randint
import json
import logging
from time import sleep
import datetime
#from lib import config_parser
import json
import os
import logging, sys
import requests
import uuid

# main.py

from controller import Controller

def collect_input(prompt, required_type=str):
    while True:
        user_input = input(prompt)
        try:
            return required_type(user_input)
        except ValueError:
            print(f"Please enter a valid {required_type.__name__} value.")

def main():
    controller = Controller()

    while True:
        print("\nMindSphere Model Creator CLI")
        print("1. Add Aspect Type")
        print("2. Add Asset Type")
        print("3. Add Asset")
        print("4. Generate and Publish Model to MindSphere")
        print("5. Exit")
        choice = collect_input("Choose an option: ", int)

        if choice == 1:
            # Collect inputs for Aspect Type
            # Call controller methods to handle the inputs
            pass
        elif choice == 2:
            # Collect inputs for Asset Type
            # Call controller methods to handle the inputs
            pass
        elif choice == 3:
            # Collect inputs for Asset
            # Call controller methods to handle the inputs
            pass
        elif choice == 4:
            # Call controller method to generate and publish the model
            pass
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

