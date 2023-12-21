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
from lib import config_parser
import json
import os
import logging, sys
import requests
import uuid

from ui import start_ui

def main():
    start_ui()

if __name__ == "__main__":
    main()
