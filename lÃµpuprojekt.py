import random

def loo_ulesanne():
    arv1 = random.randint(1, 10)
    arv2 = random.randint(1, 10)
    tehe = random.choice(["+", "-", "*", "/"])

    if tehe == "+":
        oige_vastus = arv1 + arv2
    elif tehe == "-":
        oige_vastus = arv1 - arv2
    elif tehe == "*":
        oige_vastus = arv1 * arv2
    elif tehe == "/":
        while arv2 == 0:
            arv2 = random.randint(1, 10)
        oige_vastus = round(arv1 / arv2, 2)

    ulesanne = f"{arv1} {tehe} {arv2}"
    return ulesanne, oige_vastus

def harjutusrezhiim():
    print("\n--- Harjutusrežiim ---")
    while True:
        ulesanne, oige = loo_ulesanne()
        print("Ülesanne:", ulesanne)
        vastus = input("Sinu vastus (või 'q' lõpetamiseks): ")

        if vastus.lower() == "q":
            break

        try:
            if float(vastus) == oige:
                print("Õige vastus! Väga tubli!\n")
            else:
                print(f"Vale vastus. Õige vastus on {oige}.\n")
        except:
            print("Palun sisesta arvuline vastus!\n")

def testirezhiim():
    print("\n--- Testirežiim ---")
    oiged = 0
    valed = 0
    kogus = 10

    for i in range(kogus):
        ulesanne, oige = loo_ulesanne()
        print(f"Ülesanne {i+1}: {ulesanne}")
        vastus = input("Sinu vastus: ")

        try:
            if float(vastus) == oige:
                print("Õige!\n")
                oiged += 1
            else:
                print(f"Vale. Õige vastus: {oige}\n")
                valed += 1
        except:
            print(f"Vale sisestus. Õige vastus: {oige}\n")
            valed += 1

    print("--- Testi tulemus ---")
    print(f"Õigeid vastuseid: {oiged}")
    print(f"Valesid vastuseid: {valed}")
    print("---------------------\n")

def pea_menuu():
    while True:
        print("Tere tulemast matemaatika harjutuste generaatorisse!")
        print("1 - Harjutusrežiim")
        print("2 - Testirežiim (10 ülesannet)")
        print("3 - Välju")
        valik = input("Vali režiim (1/2/3): ")

        if valik == "1":
            harjutusrezhiim()
        elif valik == "2":
            testirezhiim()
        elif valik == "3":
            print("Kohtumiseni meie matemaatika kluubis!")
            break
        else:
            print("Tundmatu valik. Proovi uuesti.\n")

pea_menuu()
