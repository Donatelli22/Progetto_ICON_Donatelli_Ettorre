from owlready2 import *
from numpy import *
from pyswip import *



p = Prolog()
onto = get_ontology("file://menu.rdf").load()
p.consult("menu.pl")


print("Benvenuti, su questa piattaforma per la creazione di menu")    
print("seguite una delle seguenti diete?(NoLattosio, NoGlutine, Vegano o Nessuno)")
DietaApp=input().lower()
while(DietaApp!="vegano" and DietaApp!="nolattosio" and DietaApp!="noglutine" and DietaApp!="nessuno"):
    print("inserire una delle scelte possibili")
    DietaApp=input().lower()

Dieta="menu:"+DietaApp    

print("Tipo del primo piatto?(pasta, riso)")
Tipo=input().lower()
while(Tipo!="pasta" and Tipo!="riso"):
    print("inserire una delle scelte possibili")
    Tipo=input().lower()

print("Sapore del primo piatto?(leggero, medio, forte  o piccante)")
Sapore=input().lower()
while(Sapore!="leggero" and Sapore!="medio" and Sapore!="forte" and Sapore!="piccante"):
    print("inserire una delle scelte possibili")
    Sapore=input().lower()

print("Difficolta del primo piatto?(facile, medio o difficile)")
Difficolta=input().lower()
while(Difficolta!="facile" and Difficolta!="medio" and Difficolta!="difficile"):
    print("inserire una delle scelte possibili")
    Difficolta=input().lower()
    
print("Costo del primo piatto?(basso, medio o alto)")
Costo=input().lower()
while(Costo!="basso" and Costo!="medio" and Costo!="alto"):
    print("inserire una delle scelte possibili")
    Costo=input().lower()
    

if(Dieta!="menu:nessuno"):
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a {Dieta}, menu:primopiatto;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene; 
    menu:Sapore '{Sapore}';
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'. 
    }}"""
else:
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a menu:primopiatto;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene; 
    menu:Sapore '{Sapore}';
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'.  
    }}"""

Primo=list(default_world.sparql(Stringa))

print("Tipo del secondo piatto?(carne, pesce, verdura, legumi)")
Tipo=input().lower()

while(bool(list(p.query(f"menu({DietaApp},{Tipo})")))==False):
        print("inserire una delle scelte possibili seguendo le dieta scelta")
        Tipo=input().lower()    
    
print("Sapore del secondo piatto?(leggero, medio, forte o piccante)")
Sapore=input().lower()
while(Sapore!="leggero" and Sapore!="medio" and Sapore!="forte" and Sapore!="piccante"):
    print("inserire una delle scelte possibili")
    Sapore=input().lower()

print("Difficolta del secondo piatto?(facile, medio o difficile)")
Difficolta=input().lower()
while(Difficolta!="facile" and Difficolta!="medio" and Difficolta!="difficile"):
    print("inserire una delle scelte possibili")
    Difficolta=input().lower()
    
print("Costo del secondo piatto?(basso, medio o alto)")
Costo=input().lower()
while(Costo!="basso" and Costo!="medio" and Costo!="alto"):
    print("inserire una delle scelte possibili")
    Costo=input().lower()

if(Dieta!="menu:nessuno"):
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a {Dieta}, menu:secondopiatto;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene; 
    menu:Sapore '{Sapore}';
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'. 
    }}"""
else:
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a menu:secondopiatto;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene;
    menu:Sapore '{Sapore}'; 
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'.  
    }}"""

Secondo=list(default_world.sparql(Stringa))

print("Tipo di dessert?(cioccolata, frutta o crema)")
Tipo=input().lower()
while(Tipo!="frutta" and Tipo!="cioccolata" and Tipo!="crema"):
    print("inserire una delle scelte possibili")
    Tipo=input().lower()

print("Temperatura a cui va servito?(caldo, normale, freddo)")
Temperatura=input().lower()
while(Temperatura!="caldo" and Temperatura!="normale" and Temperatura!="freddo"):
    print("inserire una delle scelte possibili")
    Temperatura=input().lower()

print("Difficolta del dessert?(facile, medio o difficile)")
Difficolta=input().lower()
while(Difficolta!="facile" and Difficolta!="medio" and Difficolta!="difficile"):
    print("inserire una delle scelte possibili")
    Difficolta=input().lower()
    
print("Costo del dessert?(basso, medio o alto)")
Costo=input().lower()
while(Costo!="basso" and Costo!="medio" and Costo!="alto"):
    print("inserire una delle scelte possibili")
    Costo=input().lower()

if(Dieta!="menu:nessuno"):
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a {Dieta}, menu:dessert;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene; 
    menu:Temperatura '{Temperatura}';
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'. 
    }}"""
else:
    Stringa=f"""SELECT ?nome ?link 
    {{
    ?x a menu:dessert;
    menu:Nome ?nome;
    menu:Link ?link;
    menu:Contiene ?contiene; 
    menu:Temperatura '{Temperatura}';
    menu:Prezzo '{Costo}';
    menu:Difficolta '{Difficolta}' .
    ?contiene menu:Nome '{Tipo}'.  
    }}"""

Dessert=list(default_world.sparql(Stringa))

if(Primo):
    print("Primo: ",Primo[0])
else:
    print("ci dispiace non ci sono primi piatti nel nostro sistema con le proprietà chieste")
if(Secondo):
    print("Secondo: ",Secondo[0])
else:
    print("ci dispiace non ci sono secondi piatti nel nostro sistema con le proprietà chieste")
if(Dessert):
    print("Dessert: ",Dessert[0])
else:
    print("ci dispiace non ci sono dessert nel nostro sistema con le proprietà chieste")



