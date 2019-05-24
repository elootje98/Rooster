# Handleiding voor Lectures & Lesroosters

## Case Lectures & Lesroosters
De opdracht voor Lectures & Lesroosters is om met behulp van verschillende
algoritmes op zoek te gaan naar het beste weekrooster voor de UvA. Een rooster
is geldig als alle vakken zijn ingepland volgens de regels van de UvA. Er worden
punten toegekend aan een rooster op basis van een aantal spelregels: de
objective function. Een volledige beschrijving van de geldigheidsregels,
spelregels, rooster en vakkenlijst vind je [hier](http://heuristieken.nl/wiki/index.php?title=Lectures_%26_Lesroosters).

We zijn niet toegkomen aan het deel van de case met individuele
vakinschrijvingen. We hebben geprobeerd meer nadruk te leggen op het implementeren
van verschillende algoritmes.

## Requirements
Deze package is geschreven in Python3.7.2. De benodigde modules staan in
'requirements.txt' en kunnen worden geinstalleerd met 'pip install -r
requirements.txt'.

## Handleiding
Run het script 'main.py' in een terminal om terug te refereren naar de correcte
manier om het programma te gebruiken. Er is tenminste één command line argument
nodig voor het programma, voordat het een taak uit kan voeren. Het eerste
command line argument wat meegegeven kan worden is een van de twee algoritmes
die een initieel lesrooster kunnen maken. De twee algoritmes die hiervoor
gebruikt worden zijn het Random algoritme en het Greedy algoritme. De command
line arguments die meegegeven moeten worden om een van deze algoritmes te
gebruiken zijn respectievelijk: 'random' of 'greedy'. Ook is er de mogelijkheid
een van de twee algoritmen meerdere malen uit te voeren op een leeg rooster om
vervolgens van de initiële lesroosters, het rooster met de hoogste score aan te
nemen. Deze functionaliteit wordt uitgevoerd door als eerste command line
argument 'multi' op te geven.

Als tweede argument kan een iteratief algoritme worden gekozen, die vervolgens
het lesrooster zal aanpassen. Er zijn drie algoritmes mogelijk om uit te kiezen:
Hillclimber, Simulated Annealing of Plant Propagation. De command line arguments
die meegegeven moeten worden om een van deze algoritmes te gebruiken zijn
respectievelijk: 'hillclimber', 'sa' of 'ppa'. Mocht de input van een van de
twee argumenten afwijken van de gevraagde waarden, zal dit aangegeven worden.

Het is mogelijk dat naar aanleiding van de gekozen algoritmen de gebruiker
enige input gevraagd wordt. Als de gebruiker slechts 1 argument heeft gegeven
wordt er alleen om een print optie gevraagd.

$ main.py random :
Er wordt slechts een initieel lesrooster gegenereerd met het Random algoritme.
De gebruiker wordt vervolgens gevraagd of dit lesrooster uitgeprint moet worden.
De gebruiker kan hierop 'yes' of 'no', antwoorden. De print functie van het
programma wordt uitgevoerd als de gebruiker 'yes' als antwoord geeft. De print
functie zal vervolgens het lesrooster uitprinten in de terminal en schrijven
naar het bestand timetable.txt in de map '/results'. Als de gebruiker 'no' kiest
wordt er niets geprint.

$ main.py greedy :
Er wordt slechts een initieel lesrooster gegenereerd met het Greedy algoritme.
Vervolgens wordt de gebruiker gevraagd voor print opties.

$ main.py multi :
Nu wordt er aan de gebruiker gevraagd wat voor algoritme hij wil gebruiken om de
lesroosters te vullen ('random', 'greedy') en met hoeveel iteraties op een leeg
lesrooster er vergeleken moet worden. Hieruit volgt het lesrooster wat uit dit
aantal iteraties de hoogste score heeft gekregen. Vervolgens wordt de gebruiker
gevraagd voor print opties.

Als er twee argumenten door de gebruiker worden meegegeven zal aan de hand van
het gegenereerde initele rooster de initiële score voor dat rooster gegeven.
Vervolgens zal de gebruiker om meer input gevraagd worden voor de
functionaliteit van de algoritmes.

$ main.py algorithm_1 hillclimber :
Nadat het initële rooster is gegenereerd heeft de gebruiker drie mogelijkheden
om het Hillclimber algoritme uit te voeren. 'regular' betekent dat Hillclimber
willekeurige vakken uit het rooster zoekt en deze omwisselt. Als het
resulterende rooster geen lagere score heeft dan het voorgaande, wordt het
behouden. 'greedy' betekent dat er in het rooster, het vak met de minste punten
wordt gezocht, om deze vervolgens te wisselen met een willekeurig vak. Een
lesrooster met een hogere score wordt weer behouden. 'combined' houdt in dat er
per iteratie zowel een stap 'regular' als 'greedy' wordt uitgevoerd.

Vervolgens is er de mogelijkheid om het Hillclimber algoritme optionele functies
mee te geven om uit te voeren. 'none' betekent dat er geen optionele functies
worden uitegevoerd. 'pop' is een populatie gebasseerd algoritme wat per iteratie
een kans heeft van 2% om uitegevoerd te worden, waarna er voor een groep van
500 samples willekeurig worden gekozen uit het lesrooster en in een lijst
worden gestopt. Van deze lijst wordt een element gewisselt met de eerstvolgende
vervolgens wordt van de lesroosters van al deze wisselingen de score berekent en
slechts de beste wisseling behouden. 'burst' is een random algoritme die
ongeacht de resulterende score een groep van 50 samples wordt gewisselt. De kans
waarmee dit gebeurt hangt af van het verschil van de score van het huidige
rooster met de maximaal te behalen score. Een hogere score van het huidige
rooster betekent een lagere kans waarmee 'burst' uitgevoerd kan worden.
'combined' betekent dat zowel 'pop' als 'burst' uitegevoerd worden.

Nadat het hillclimber algoritme klaar is met itereren, zal de gebruiker
gevraagd worden of het rooster uitgeprint moet worden. Daarnaast wordt ook
gevraagd of de gebruiker het rooster visueel wil weergeven. Als de gebruiker
hierop ook 'yes' antwoord, zal een plot worden gemaakt van de score over het
verloop van de iteraties van het algoritme.

$ main.py algorithm_1 sa :

$ main.py algorithm_1 ppa :
Nadat het initële rooster is gegenereerd wordt het Plant Propagation algoritme
op het rooster uitgevoerd. In de terminal zal de gebruiker weergegeven zien
worden over welke generatie het algoritme op dit moment aan het itereren is.
Vervolgens wordt de gebruiker gevraagd voor print opties.

## Structuur
- algorithms: bevat alle python scripts met de gebruikte algoritmes. Verdere
uitleg staat in de ReadMe van deze map.
- classes: bevat files van alle gebruikte objecten in deze package.
- data: bevat csv bestanden van alle ingevoerde data voor het project.
- helpers: bevat python script met functies die in meerdere andere scripts
voorkomen. Verdere uitleg in de ReadMe van deze map.
- presentatie: bevat onze presentatie van 24-05, deze wordt nog aangepast voor
de presentatie van woensdag.
- main.py: wordt gebruikt om alle algoritmes aan te roepen. Gebruik van dit
script wordt uitgelegd in de handleiding.

## Auteurs
- Wessel Rijk
- Elodie Rijnja
- József Zsíros

## Dankwoord
- Bram voor de geweldige begeleiding en zijn eindeloze geduld.
- Het hele team Heuristieken.
- De koffiemachine naast de hokjes bij B1.19.
