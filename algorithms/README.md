# Algoritmes

## Constructieve algoritmes:
- Random (randomalg.py): Maakt een leeg rooster object aan en vult alle vakken
in willekeurige volgorde in op een willekeurig plek.

- Greedy (greedy.py): Sorteert alle vakken op basis van hun 'moeilijkheid' om
in te rooster. Deze moeilijkheid is een door ons bedachte heuristiek en hangt
af van het aantal in te plannen colleges en het aantal tegelijk volgbare vakken.

## Iteratieve algoritmes
- Hillclimber (hillclimber.py): Het hillclimber algoritme werkt op twee
verschillende manieren. Hillclimber kan worden uitgevoerd door twee
willekeurige vakken uit het rooster met elkaar te verwisselen, gebruik makend
van de functies die in timetable_helpers.py staan. Vervolgens wordt de score
van een resulterend rooster berekend, waarna de vakken alleen worden terug
gewisselt als de resulterende score lager is dan de score van het voorgaande
rooster. Greedy hillclimber werkt op dezelfde manier maar gebruikt het vak
met het minst aantal punten als een van de vakken die gewisselt worden.

Hillclimber heeft twee optionele functies die naast de standaard hillclimber
ook uitgevoerd kunnen worden. de hill_population pakt een groep van willekeurige
lectures uit het rooster en stopt deze in een lijst, vervolgens wordt van een
element uit de lijst de plek in het rooster gewisselt met de opvolgende. Van al
deze wisselingen wordt het rooster gezocht met de hoogst resulterende score,
die vervolgens als enige wordt behouden. De kans waarop deze functie uitegevoerd
wordt is 2%. De random_burst pakt een groep en wisselt ze op dezelfde manier als
hill_population, echter worden alle wisselingen behouden ongeacht de
resulterende score. De kans waarop deze functie geactiveerd wordt hangt af van
het verschil tussen het huidige rooster en de maximum te behalen score. Waarbij
de kans lager is als het huidige rooster een hogere score heeft.
Beide optionele functies kunnen tegelijk meegenomen worden bij het itereren.


- Simulated Annealing (simulated_annealing.py): Simulated annealing werkt
vergelijkbaar met hillclimber, maar accepteert verslechteringen met een bepaalde
kans. De kans is een exponentiele functie die afhangt van de grootte van de
verslechtering, de temperatuur en een parameter. De temperatuur is een indicator
voor hoe ver het algoritme is in zijn totale runs. De temperatuur volgt een
koelschema. De geimplementeerde koelschemas zijn lineair, exponentieel en
sigmoidaal. Alle parameters bevinden zich bovenaan het bestand en kunnen
eenvoudig worden aangepast.

- Plant Propagation Algorithm (ppa.py): Plant propagation initialiseert een
groep startroosters met Random. Deze roosters worden beoordeeld op hun score
door een adapted fitness te berekenen. Hiermee wordt uitgerekend hoeveel kindroosters
er moet worden gemaakt en hoeveel mutaties (swaps van lectures) moeten worden gemaakt.
Hoe beter het rooster, hoe meer kinderen en minder mutaties. De kindroosters en
ouderroosters worden in een lijst gegooid, gesorteerd op hun score en de beste
roosters worden gebruikt om een startgroep te maken voor een volgende generatie.
Deze formule wordt een aantal keer herhaald. Alle parameters bevinden zich bovenaan het bestand en kunnen
eenvoudig worden aangepast.
