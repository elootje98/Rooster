# algoritmes

## Constructieve algoritmes:
- Random (randomalg.py): Maakt een leeg rooster object aan en vult alle vakken
in willekeurige volgorde in op een willekeurig plek.

- Greedy (greedy.py): Sorteert alle vakken op basis van hun 'moeilijkheid' om
in te rooster. Deze moeilijkheid is een door ons bedachte heuristiek en hangt
af van het aantal in te plannen colleges en het aantal tegelijk volgbare vakken.

## Iteratieve algoritmes
- Hillclimber (hillclimber.py)

- Simulated Annealing (simulated_annealing.py): Simulated annealing werkt
vergelijkbaar met hillclimber, maar accepteert verslechteringen met een bepaalde
kans. De kans is een exponentiele functie die afhangt van de grootte van de
verslechtering, de temperatuur en een parameter. De temperatuur is een indicator
voor hoe ver het algoritme is in zijn totale runs. De temperatuur volgt een
koelschema. De geimplementeerde koelschemas zijn lineair, exponentieel en
sigmoidaal.

Alle parameters bevinden zich bovenaan het bestand en kunnen
eenvoudig worden aangepast.

- Plant Propagation Algorithm (ppa.py): Plant propagation initialiseert een
groep startroosters met Random. Deze roosters worden beoordeeld op hun score
door een adapted fitness te berekenen. Hiermee wordt uitgerekend hoeveel kindroosters
er moet worden gemaakt en hoeveel mutaties (swaps van lectures) moeten worden gemaakt.
Hoe beter het rooster, hoe meer kinderen en minder mutaties. De kindroosters en
ouderroosters worden in een lijst gegooid, gesorteerd op hun score en de beste
roosters worden gebruikt om een startgroep te maken voor een volgende generatie.
Deze formule wordt een aantal keer herhaald.

Alle parameters bevinden zich bovenaan het bestand en kunnen
eenvoudig worden aangepast.
