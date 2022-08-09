# %%
import requests
import json
import urllib3
import time
import telepot
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# %% Class to print in colors


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# %% Definitions
url = "https://igs.backend2.logimed.com.ar/logimedws/turnoscalendario?obraSocial=21&plan=1&sucursal=1&especialidad=6&prestacion=420101&profesional=606"

payload = {}
headers = {
    'Token': 'Test123'
}

check_period = 60  # in seconds
max_date = 20220931  # the script will check for dates closer than this

bot = telepot.Bot('5448057728:AAEEeDVEGpaYvJRSfl9p4RrTKLHbqy9svbs')
chat_id = 670220713

# %%
while(1):
    response = requests.request(
        "GET", url, headers=headers, data=payload, verify=False)
    appointments = json.loads(response.text)

    appointments_dates = []
    for appointment in appointments["calendario"]:
        appointments_dates.append(int(appointment["fecha"]))

    if min(appointments_dates) < max_date:
        print("{}{}\t Next available appointment: {}{}".format(bcolors.OKGREEN,
              datetime.now(), appointments_dates[0], bcolors.ENDC))
        bot.sendMessage(chat_id, "{}\t Next available appointment: {}".format(
            datetime.now(), appointments_dates[0]))
        break
    else:
        print("{}{}\t Next available appointment: {}{}".format(bcolors.FAIL,
              datetime.now(), appointments_dates[0], bcolors.ENDC))
    time.sleep(check_period)
# %%
