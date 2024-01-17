from ..src.stasjon import Stasjon, Lokomotiv, Vogn, Pakke

def test_legg_til_lokomotiv():
    stasjon = Stasjon("Oslo")
    assert stasjon.navn == "Oslo"
    assert len(stasjon.lokomotiv) == 2

    lok1 = Lokomotiv(12345, 500, 4000, "Bergen")
    lok2 = Lokomotiv(12346, 500, 4000, "Moss")

    assert lok1.serienr == 12345
    assert lok1.vekt == 500
    assert lok1.maksvekt == 4000
    assert lok1.destinasjon == "Bergen"

    assert lok1.serienr == 12346
    assert lok1.vekt == 500
    assert lok1.maksvekt == 4000
    assert lok1.destinasjon == "Moss"

    stasjon.registrer_lokomotiv(lok1)
    stasjon.registrer_lokomotiv(lok2)
    assert len(stasjon.lokomotiv) == 2

def test_legg_til_vogn():
    lok1 = Lokomotiv(12345, 500, 4000, "Bergen")
    lok2 = Lokomotiv(12346, 500, 4000, "Moss")
    assert len(lok1.vogner) == 0
    assert len(lok2.vogner) == 0

    for i in range(5):
        lok1.registrer_vogn(Vogn(1234+i, 100, 200))
        lok2.registrer_vogn(Vogn(1245+2*i, 100, 200))
        lok2.registrer_vogn(Vogn(1245+10*i, 100, 200))
    
    assert len(lok1.vogner) == 5
    assert len(lok2.vogner) == 10
    assert lok1.beregn_vekt() == (500+5*100)
    assert lok2.beregn_vekt() == (500+10*100)
    assert lok1.sjekk_vekt()
    assert lok2.sjekk_vekt()

def test_legg_til_pakke():
    stasjon = Stasjon("Oslo")
    lok1 = Lokomotiv(12345, 500, 4000, "Bergen")
    lok2 = Lokomotiv(12346, 500, 4000, "Moss")
    stasjon.registrer_lokomotiv(lok1)
    stasjon.registrer_lokomotiv(lok2)

    for i in range(5):
        lok1.registrer_vogn(Vogn(1234+i, 100, 200))
        lok2.registrer_vogn(Vogn(1245+2*i, 100, 200))
        lok2.registrer_vogn(Vogn(1245+10*i, 100, 200))

    for _ in range(100):
        stasjon.registrer_pakke(Pakke("Oslo", 10, "ting"))
        stasjon.registrer_pakke(Pakke("Bergen", 20, "ting"))
    
    assert lok1.beregn_vekt() == (500+5*100+100*10)
    assert lok2.beregn_vekt() == (500+10*100+100*20)
