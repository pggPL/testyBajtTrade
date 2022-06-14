import json
import subprocess
import os



# Kariery

def programista():
	return "programista"

def rolnik():
	return "rolnik"

def rzemieslnik():
	return "rzemieslnik"

def inzynier():
	return "inzynier"

def gornik():
	return "gornik"

def kariery():
	return [
		programista,
		rolnik,
		rzemieslnik,
		inzynier,
		gornik
	]

# uczenie

def pracus():
	return {
		"typ": "pracus"
	}

def oszczedny(limit_diamentow=100):
	return {
		"typ": "oszczedny",
		"limit_diamentow": limit_diamentow
	}

def student(zapas=2, okres=5):
	return {
		"typ": "student",
		"zapas": zapas,
		"okres": okres
	}

def okresowy(okresowosc_nauki=3):
	return {
		"typ": "okresowy",
		"okresowosc_nauki": okresowosc_nauki
	}

def rozkladowy():
	return {
		"typ": "rozkladowy"
	}

def uczenie():
	return [
		pracus,
		oszczedny,
		student,
		okresowy,
		rozkladowy
	]

# zmiana

def konserwatysta():
	return "konserwatysta"

def rewolucjonista():
	return "rewolucjonista"

def zmiana():
	return [
		konserwatysta,
		rewolucjonista
	]

#produkcja

def krotkowzroczny():
	return {
		"typ": "krotkowzroczny"
	}

def chciwy():
	return {
		"typ": "chciwy"
	}

def sredniak(historia_sredniej_produkcji=3):
	return {
		"typ": "sredniak",
		"historia_sredniej_produkcji": historia_sredniej_produkcji
	}

def perspektywiczny(historia_perspektywy=3):
	return {
		"typ": "perspektywiczny",
		"historia_perspektywy": historia_perspektywy
	}

def losowy():
	return {
		"typ": "losowy"
	}

# kupowanie

def technofob():
	return {
		"typ": "technofob"
	}

def czyscioszek():
	return {
		"typ": "czyscioszek"
	}

def zmechanizowany(liczba_narzedzi=100):
	return {
		"typ": "zmechanizowany",
		"liczba_narzedzi": liczba_narzedzi
	}

def gadzeciarz(liczba_narzedzi=100):
	return {
		"typ": "gadzeciarz",
		"liczba_narzedzi": liczba_narzedzi
	}

def sprzedarz():
	return [
		technofob,
		czyscioszek,
		zmechanizowany,
		gadzeciarz
	]

# gielda


def kapitalistyczna():
	return "kapitalistyczna"

def socjalistyczna():
	return "socjalistyczna"

def zrownowazona():
	return "zrownowazona"

def gielda():
	return [
		kapitalistyczna,
		socjalistyczna,
		zrownowazona
	]

# kariera spekulanta

def wypukly():
	return "wypukly"

def regulujacy():
	return "regulujacy"

def sredni():
	return "sredni"


# inne
def zasoby(diamenty=100, ubrania=100, narzedzia=100, jedzenie=100, programy=100):
	zasoby = {}
	zasoby["diamenty"] = diamenty
	zasoby["ubrania"] = ubrania
	zasoby["narzedzia"] = narzedzia
	zasoby["jedzenie"] = jedzenie
	zasoby["programy"] = programy
	return zasoby



# inne
def produktywnosc(diamenty=100, ubrania=100, narzedzia=100, jedzenie=100, programy=100):
	produktywnosc = {}
	produktywnosc["diamenty"] = diamenty
	produktywnosc["ubrania"] = ubrania
	produktywnosc["narzedzia"] = narzedzia
	produktywnosc["jedzenie"] = jedzenie
	produktywnosc["programy"] = programy
	return produktywnosc


def robotnik(id, poziom=1, kariera=programista(), kupowanie=gadzeciarz(),
	         produkcja=chciwy(), zmiana=rewolucjonista(), uczenie=student(),
	         produktywnosc=produktywnosc(), zasoby=zasoby()
	         ):
    robotnik = {}
    robotnik["id"] = id
    robotnik["poziom"] = poziom
    robotnik["kariera"] = kariera
    robotnik["kupowanie"] = kupowanie	
    robotnik["produkcja"] = produkcja
    robotnik["uczenie"] = uczenie
    robotnik["zmiana"] = zmiana
    robotnik["produktywnosc"] = produktywnosc
    robotnik["zasoby"] = zasoby
    return robotnik

def spekulant(id, kariera=wypukly(), zasoby=zasoby()):
	spekulant = {}
	spekulant["id"] = id
	spekulant["kariera"] = kariera
	spekulant["zasoby"] = zasoby
	return spekulant


def ceny(programy=1, jedzenie=1.2, ubrania=1.3, narzedzia=1.5):
	return {
        "programy": programy,
        "jedzenie": jedzenie,
        "ubrania": ubrania,
        "narzedzia": narzedzia
	}

def info(dlugosc=5, gielda=socjalistyczna(), ceny=ceny()):
	info = {}
	info["gielda"] = gielda
	info["dlugosc"] = dlugosc
	info["kara_za_brak_ubran"] = 10
	info["ceny"] = ceny
	return info

def generate_input(robotnicy=[], spekulanci=[], info=info()):
	inp = {}
	inp["robotnicy"] = robotnicy
	inp["spekulanci"] = spekulanci
	inp["info"] = info

	return json.dumps(inp, indent=4)

def get_output(inp, debug):
	f = open("tmp_input", "w")
	f.write(inp)
	f.close()

	if debug:
		out = None
	else:
		out = subprocess.DEVNULL

	process = subprocess.run(['bash', './uruchom.sh', './testyBajtTrade/tmp_input', './testyBajtTrade/tmp_output'], cwd='..', stdout=out)


	f = open("tmp_output", "r")
	text = f.read()
	f.close()
	return json.loads(text)

def get_spekulant(id, spekulanci):
	for s in spekulanci:
		if s["id"] == id:
			return s
	return None

def get_robotnik(id, robotnicy):
	for r in robotnicy:
		if r["id"] == id:
			return r
	return None