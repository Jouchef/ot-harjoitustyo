# Vaatimusmäärittely

## Käyttäjät
Sovelluksessa on kaksi roolia. Peruskäyttäjä, ja moderaattori. 
Moderaattorilla on peruskäyttäjän lisäksi oikeuksina vain lisätä ja muokata käyttäjärooleja. Lisäksi moderaattori voi lisätä tavaroiden säilytyspaikkoja.

## Sovelluksen tarkoitus

Sovelluksella voidaan seurata missä mikäkin tavara milloinkin on. Aina kun tavara viedään muualle, niin se merkitään sovellukseen. Tällöin tavaroiden sijainnista saadaan parempi kokonaiskuva.


## Perusversion toiminnallisuus

- Käyttäjä voi luoda käyttäjätunnuksen ja kirjautua
- Käyttäjänimen pitää olla uniikki
- Käyttäjä voi kirjautua järjestelmään
- Käyttäjä voi kirjautua ulos
- Jos käyttäjänimeä ei löydy, ehdottaa sovellus rekisteröitymistä
- Kaikki tieto on tallennettu tietokantaan

- Käyttäjä näkee kirjautumisen jälkeen kaikki säilytyspaikat
- Samassa näkymässä on +-merkki, josta voi luoda uuden tavaran
- Säilytyspaikka valitessa avautuu näkymä, joka näyttää mitä tavaroita siellä on.
- Klikattaessa tavaraa, voi sen sijaintia muuttaa

- Moderaattori voi lisätä tai poistaa varastopaikkoja


## Näkymät

- Kirjautumisnäkymä
- rekisteröitymisnäkymä
- kirjautumisen jälkeen avautuu näkymä jossa on kaikki varastopaikat
- varastopaikka avattaessa on näkymä jossa näkyy kaikki siellä olevat tavarat
- Tavara avattaessa näkyy tavaran tiedot
- Tavaraa luodessa näkyy tavaran tiedot

## Jatkokehitys
- Tavaroita voi olla yhdessä slotissa monta, esim. varastosta voi ottaa helposti 50 lusikasta vaikka 20
- Moderaattorin pitää hyväksyä uudet käyttäjärekisteröitymiset
- Säilytyspaikalle voi määrittää teemavärin
- Tavaran voi siirtää "lainaan" itselle.
- Hakuominausuus tavaralle
- lainatessa ilmoitetaan milloin se palautuu
- Järjestelmä ilmoittaa käyttäjälle, jos hänellä on lainassa tavara, jota ei ole palautettu ajoissa.
