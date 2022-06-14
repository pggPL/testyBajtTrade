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
    inp = generate_input(robotnicy=robotnicy, spekulanci=spekulanci, info=info(dlugosc=1))
    output = get_output(inp, debug)

    robotnicy = output["robotnicy"]

    assert(get_robotnik(1, robotnicy)["kariera"] == "programista")
    assert(get_robotnik(2, robotnicy)["kariera"] == "rolnik")
    assert(get_robotnik(3, robotnicy)["kariera"] == "gornik")
    assert(get_robotnik(4, robotnicy)["kariera"] == "inzynier")
    assert(get_robotnik(5, robotnicy)["kariera"] == "rzemieslnik")

    assert(get_robotnik(1, robotnicy)["zmiana"] == "rewolucjonista")
    assert(get_robotnik(2, robotnicy)["zmiana"] == "konserwatysta")
