# %%
import requests
import json
import urllib3
import time
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# %%


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


# %%
url = "https://igs.backend2.logimed.com.ar/logimedws/turnoscalendario?obraSocial=21&plan=1&sucursal=1&especialidad=6&prestacion=420101&profesional=606"

payload = {}
headers = {
    'Token': 'Test123'
}

interval = 60  # in seconds
turno_mas_proximo = 20220901

# %%
while(1):
    response = requests.request(
        "GET", url, headers=headers, data=payload, verify=False)
    turnos = json.loads(response.text)

    turnos_fecha = []
    for turno in turnos["calendario"]:
        turnos_fecha.append(int(turno["fecha"]))

    if min(turnos_fecha) < turno_mas_proximo:
        print("{}{}\t Próximo turno: {}{}".format(bcolors.OKGREEN,
              datetime.now(), turnos_fecha[0], bcolors.ENDC))
        break
    else:
        print("{}{}\t Próximo turno: {}{}".format(bcolors.FAIL,
              datetime.now(), turnos_fecha[0], bcolors.ENDC))
    time.sleep(interval)

# %%
