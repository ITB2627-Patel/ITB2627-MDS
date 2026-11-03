import requests
import random
import time
from datetime import datetime, timedelta

# ====================== CONFIG ======================
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScdarMYgeWtUP9IArREhuKO2YIkmK2b0cTzgNuBa19RAt7YZA/formResponse"

NUM_RESPONSES = 30          # how many to send this run
DELAY = 1.8                 # seconds between submissions (recommended ≥ 1.5)
# ====================================================

# Entry IDs extracted from your form
ENTRY = {
    "nom":          "entry.2012926423",   # Nom i cognoms
    "carrec":       "entry.127620210",    # Càrrec o rol
    "curs":         "entry.1513129506",   # Curs i grup / Departament
    "telefon":      "entry.1210945003",   # Telèfon (optional)
    "data_year":    "entry.1450428403_year",
    "data_month":   "entry.1450428403_month",
    "data_day":     "entry.1450428403_day",
    "hora_hour":    "entry.1163966062_hour",
    "hora_min":     "entry.1163966062_minute",
    "ubicacio":     "entry.1015749349",
    "codi":         "entry.1476884717",   # Número o codi equip (optional)
    "tipus":        "entry.1671569138",   # Tipus d'incidència
    "descripcio":   "entry.1497941961",
    "intentat":     "entry.1982456671",   # Heu intentat resoldre-ho?
    "impedeix":     "entry.943347352",    # Impedeix l'activitat?
    "urgencia":     "entry.1637432414",
    "observacions": "entry.1827479680",   # optional
    "confirmacio":  "entry.1378190087",   # checkbox
}

# Data pools (same style as your original .gs)
NOMS = ["Aryan", "Marta", "Joan", "Laia", "Pau", "Núria", "Àlex", "Sofia", "Marc", "Júlia",
        "Pol", "Emma", "Nil", "Clara", "Eric", "Aina", "Jan", "Ona", "Leo", "Mia"]
COGNOMS = ["Garcia", "Martí", "Soler", "Vila", "Ferrer", "Puig", "Roca", "Serra", "Pons", "Camps",
           "Riera", "Costa", "Font", "Bosch", "Mas", "Vidal", "Sánchez", "López", "Pérez", "Ruiz"]

CARRECS = ["Alumne/a", "Professor/a", "Tutor/a", "Cap d'estudis", "Director/a",
           "Personal d'administració i serveis (PAS)"]

GRUPS = ["1r A", "1r B", "2n A", "2n B", "3r A", "3r B", "4t A",
         "Departament de Matemàtiques", "Departament d'Informàtica", "Secretaria", "Biblioteca"]

LLOCS = ["Aula 101", "Aula 102", "Aula 204", "Aula 305", "Laboratori d'informàtica",
         "Biblioteca", "Sala de professors", "Despatx de direcció", "Aula d'idiomes"]

TIPUS = [
    "Ordinador / CPU (no s'encén, va lent, es bloqueja)",
    "Pantalla / monitor",
    "Teclat / ratolí",
    "Wi-Fi / Xarxa",
    "Accés a Internet",
    "Programari / Aplicació",
    "Compte d'usuari / Contrasenya",
    "Correu electrònic",
    "Impressora / Escàner",
    "Projector / Pissarra digital"
]

DESCRIPCIONS = [
    "L'equip no s'encén després de prémer el botó d'engegada.",
    "El Wi-Fi es desconnecta cada pocs minuts i cal tornar a connectar-se manualment.",
    "El monitor mostra la imatge amb parpelleigs i a vegades es posa en negre.",
    "El programa es tanca sol en obrir un fitxer concret.",
    "No puc iniciar sessió amb el meu compte d'usuari; diu que la contrasenya és incorrecta.",
    "L'ordinador va molt lent i es bloqueja quan obro més de dues aplicacions.",
    "La impressora no imprimeix i mostra un error de comunicació.",
    "No tinc accés a Internet des d'aquest ordinador, la resta de la xarxa funciona.",
    "El projector no detecta el senyal de l'ordinador.",
    "El teclat deixa de respondre de forma intermitent."
]

def random_name():
    return f"{random.choice(NOMS)} {random.choice(COGNOMS)} {random.choice(COGNOMS)}"

def random_phone():
    return "6" + str(random.randint(10000000, 99999999))

def random_code():
    return f"PC-{random.randint(1, 120)}"

def random_date():
    d = datetime.now() - timedelta(days=random.randint(0, 60))
    return d.year, d.month, d.day

def submit_one(i):
    year, month, day = random_date()
    hour = random.randint(8, 17)
    minute = random.randint(0, 59)

    data = {
        ENTRY["nom"]:          random_name(),
        ENTRY["carrec"]:       random.choice(CARRECS),
        ENTRY["curs"]:         random.choice(GRUPS),
        ENTRY["telefon"]:      random_phone(),
        ENTRY["data_year"]:    year,
        ENTRY["data_month"]:   month,
        ENTRY["data_day"]:     day,
        ENTRY["hora_hour"]:    hour,
        ENTRY["hora_min"]:     minute,
        ENTRY["ubicacio"]:     random.choice(LLOCS),
        ENTRY["codi"]:         random_code(),
        ENTRY["tipus"]:        random.choice(TIPUS),
        ENTRY["descripcio"]:   random.choice(DESCRIPCIONS),
        ENTRY["intentat"]:     random.choice(["Sí", "No"]),
        ENTRY["impedeix"]:     random.choice(["Sí, totalment", "Sí, parcialment", "No"]),
        ENTRY["urgencia"]:     random.choice(["Baix", "Mitjà", "Alt"]),
        ENTRY["observacions"]: random.choice(["", "Cal revisar-ho aviat.", "Ja he reiniciat l'equip sense èxit."]),
        ENTRY["confirmacio"]:  "Declaro que la informació facilitada és veritable i que he comunicat la incidència de bona fe.",
        "fvv": 1,
        "pageHistory": "0,1,2",   # important for multi-section forms
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://docs.google.com/forms/d/e/1FAIpQLScdarMYgeWtUP9IArREhuKO2YIkmK2b0cTzgNuBa19RAt7YZA/viewform",
    }

    try:
        r = requests.post(FORM_URL, data=data, headers=headers, timeout=15)
        ok = r.status_code == 200
        print(f"[{i+1:03d}] {'✓ OK' if ok else '✗ FAIL'}  (status {r.status_code})")
        return ok
    except Exception as e:
        print(f"[{i+1:03d}] ✗ Error: {e}")
        return False

def main():
    print(f"Sending {NUM_RESPONSES} fake responses to your form...\n")
    success = 0
    for i in range(NUM_RESPONSES):
        if submit_one(i):
            success += 1
        time.sleep(DELAY)
    print(f"\nFinished → {success}/{NUM_RESPONSES} submitted successfully.")

if __name__ == "__main__":
    main()
