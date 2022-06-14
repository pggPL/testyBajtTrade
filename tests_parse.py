from core import *

def test_parse(debug):
    print("Running test_parse...")
    robotnicy = [
    	robotnik(1, poziom=1, kariera=programista(), 
    		                  kupowanie=gadzeciarz(), 
    		                  produkcja=chciwy(), 
    		                  zmiana=rewolucjonista(), 
    		                  uczenie=pracus()),
    	robotnik(2, poziom=1, kariera=rolnik(), 
    		                  kupowanie=technofob(), 
    		                  produkcja=krotkowzroczny(), 
    		                  zmiana=konserwatysta(), 
    		                  uczenie=oszczedny()),
    	robotnik(3, poziom=1, kariera=gornik(), 
    		                  kupowanie=czyscioszek(), 
    		                  produkcja=sredniak(), 
    		                  zmiana=rewolucjonista(), 
    		                  uczenie=student()),
    	robotnik(4, poziom=1, kariera=inzynier(), 
    		                  kupowanie=zmechanizowany(), 
    		                  produkcja=perspektywiczny(), 
    		                  zmiana=rewolucjonista(), 
    		                  uczenie=okresowy()),
    	robotnik(5, poziom=1, kariera=rzemieslnik(), 
    		                  kupowanie=gadzeciarz(), 
    		                  produkcja=losowy(), 
    		                  zmiana=rewolucjonista(), 
    		                  uczenie=rozkladowy()),
    ]
    spekulanci = [
    	spekulant(1, kariera=wypukly()),
    	spekulant(2, kariera=regulujacy()),
    	spekulant(3, kariera=sredni()),
    ]
    inp = generate_input(robotnicy=robotnicy, spekulanci=spekulanci, info=info(dlugosc=3))
    output = get_output(inp, debug)
    day1 = output[0]

    robotnicy = day1["robotnicy"]
    spekulanci = day1["spekulanci"]

    assert(get_robotnik(1, robotnicy)["kariera"] == "programista")
    assert(get_robotnik(2, robotnicy)["kariera"] == "rolnik")
    assert(get_robotnik(3, robotnicy)["kariera"] == "gornik")
    assert(get_robotnik(4, robotnicy)["kariera"] == "inzynier")
    assert(get_robotnik(5, robotnicy)["kariera"] == "rzemieslnik")

    assert(get_robotnik(1, robotnicy)["zmiana"] == "rewolucjonista")
    assert(get_robotnik(2, robotnicy)["zmiana"] == "konserwatysta")

    assert(get_robotnik(1, robotnicy)["kupowanie"]["typ"] == "gadzeciarz")
    assert(get_robotnik(1, robotnicy)["kupowanie"]["liczba_narzedzi"] == 100)
    assert(get_robotnik(2, robotnicy)["kupowanie"]["typ"] == "technofob")
    assert(get_robotnik(3, robotnicy)["kupowanie"]["typ"] == "czyscioszek")
    assert(get_robotnik(4, robotnicy)["kupowanie"]["typ"] == "zmechanizowany")
    assert(get_robotnik(4, robotnicy)["kupowanie"]["liczba_narzedzi"] == 100)


    assert(get_robotnik(1, robotnicy)["produkcja"]["typ"] == "chciwy")
    assert(get_robotnik(2, robotnicy)["produkcja"]["typ"] == "krotkowzroczny")
    assert(get_robotnik(3, robotnicy)["produkcja"]["typ"] == "sredniak")
    assert(get_robotnik(3, robotnicy)["produkcja"]["historia_sredniej_produkcji"] == 3)
    assert(get_robotnik(4, robotnicy)["produkcja"]["typ"] == "perspektywiczny")
    assert(get_robotnik(4, robotnicy)["produkcja"]["historia_perspektywy"] == 3)
    assert(get_robotnik(5, robotnicy)["produkcja"]["typ"] == "losowy")

    assert(get_robotnik(1, robotnicy)["uczenie"]["typ"] == "pracus")
    assert(get_robotnik(2, robotnicy)["uczenie"]["typ"] == "oszczedny")
    assert(get_robotnik(2, robotnicy)["uczenie"]["limit_diamentow"] == 100)
    assert(get_robotnik(3, robotnicy)["uczenie"]["typ"] == "student")
    assert(get_robotnik(3, robotnicy)["uczenie"]["okres"] == 5)
    assert(get_robotnik(3, robotnicy)["uczenie"]["zapas"] == 2)
    assert(get_robotnik(4, robotnicy)["uczenie"]["typ"] == "okresowy")
    assert(get_robotnik(4, robotnicy)["uczenie"]["okresowosc_nauki"] == 3)
    assert(get_robotnik(5, robotnicy)["uczenie"]["typ"] == "rozkladowy")


    assert(get_robotnik(5, robotnicy)["produktywnosc"]["diamenty"] == 100)
    assert(get_robotnik(5, robotnicy)["produktywnosc"]["narzedzia"] == 100)
    assert(get_robotnik(5, robotnicy)["produktywnosc"]["ubrania"] == 100)
    assert(get_robotnik(5, robotnicy)["produktywnosc"]["jedzenie"] == 100)
    assert(get_robotnik(5, robotnicy)["produktywnosc"]["programy"] == 100)


    assert(get_spekulant(1, spekulanci)["kariera"]["typ"] == "wypukly")
    assert(get_spekulant(2, spekulanci)["kariera"]["typ"]  == "regulujacy_rynek")
    assert(get_spekulant(3, spekulanci)["kariera"]["typ"]  == "sredni")
    assert(get_spekulant(3, spekulanci)["kariera"]["historia_spekulanta_sredniego"]  == 10)

















