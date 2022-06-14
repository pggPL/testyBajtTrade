from core import *

def test_correctness1(debug):
    # Robotnik sprzedaje 3000 diamentów po 1000, ma mieć potem 3000100.0 diamentów.
    print("Running test_correctness1...")
    robotnicy = [
    	robotnik(1, poziom=1, kariera=rolnik(), 
    		                  kupowanie=gadzeciarz(), 
    		                  produkcja=chciwy(), 
    		                  zmiana=rewolucjonista(), 
    		                  uczenie=pracus(),
                              produktywnosc=produktywnosc(jedzenie=1200),
                              zasoby=zasoby(programy=0)),
    ]
    spekulanci = []
    cenyproduktow = ceny(jedzenie=1000)
    inp = generate_input(robotnicy=robotnicy, spekulanci=spekulanci, info=info(dlugosc=1, ceny=cenyproduktow))
    output = get_output(inp, debug)


    assert(output[0]["info"]["ceny_max"]["ubrania"] == 1.3)
    assert(output[0]["info"]["ceny_max"]["programy"] == 1.0)
    assert(output[0]["info"]["ceny_max"]["jedzenie"] == 1000.0)
    assert(output[0]["info"]["ceny_max"]["narzedzia"] == 1.5)

    assert(output[0]["info"]["ceny_min"]["ubrania"] == 1.3)
    assert(output[0]["info"]["ceny_min"]["programy"] == 1.0)
    assert(output[0]["info"]["ceny_min"]["jedzenie"] == 1000.0)
    assert(output[0]["info"]["ceny_min"]["narzedzia"] == 1.5)

    assert(output[0]["info"]["ceny_srednie"]["ubrania"] == 1.3)
    assert(output[0]["info"]["ceny_srednie"]["programy"] == 1.0)
    assert(output[0]["info"]["ceny_srednie"]["jedzenie"] == 1000.0)
    assert(output[0]["info"]["ceny_srednie"]["narzedzia"] == 1.5)



    assert(get_robotnik(1, output[0]["robotnicy"])["zasoby"]["diamenty"] == 3000100.0)

    

def test_correctness_exchange(debug):
    # test ma na celu sprawdzenie, czy dobrze działa giełda socjalistyczna
    # robotnik 1 jest biedy i on musi zostać obsłużony najpierw
    #
    print("Running test_correctness_exchange...")
    robotnicy = [
       robotnik(1, poziom=1, kariera=rzemieslnik(), kupowanie=gadzeciarz(), produkcja=chciwy(),
                          zmiana=rewolucjonista(),
                          uczenie=pracus(),
                              produktywnosc=produktywnosc(jedzenie=1200),
                              zasoby=zasoby(diamenty=300, programy=0, ubrania=0)),
      robotnik(2, poziom=1, kariera=rzemieslnik(),
                          kupowanie=gadzeciarz(),
                          produkcja=chciwy(),
                          zmiana=rewolucjonista(),
                          uczenie=pracus(),
                          produktywnosc=produktywnosc(jedzenie=1200),
                          zasoby=zasoby(diamenty=10000, programy=0, ubrania=0))]
    spekulanci = [
      spekulant(
        1,
        zasoby=zasoby(
          diamenty=0,
          narzedzia=0,
          ubrania=0,
          programy=100,
          jedzenie=0
        ),
      kariera=sredni())
    ]
    cenyproduktow = ceny(ubrania=1)
    inp = generate_input(robotnicy=robotnicy,
                         spekulanci=spekulanci,
                         info=info(dlugosc=1,
                         gielda=socjalistyczna()))
    output = get_output(inp, debug)

    assert(get_robotnik(1, output[0]["robotnicy"])["zasoby"]["programy"] == [100])
    assert(get_robotnik(2, output[0]["robotnicy"])["zasoby"]["programy"] == [])
