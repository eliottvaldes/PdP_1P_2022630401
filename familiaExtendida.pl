/*
 * Autores:
 * 1) Delgado Acosta Luis Bernardo
 * 2) Díaz Jiménez Jorge Arif
 * 3) Valdés Luis Eliot Fabían
 *
 * Grupo: 3BV2
 *
 * Fecha de elaboraci�n: 20/05/2022
 *
 * Planteamiento del problema:
 * A partir del ejemplo revisado en el archivo family.pl, ampl�a la base
 * de conocimientos de tal manera que se puedan agregar reglas para los
 * casos de bisabuelo, tatarabuelo y sobrino. (En nuestro caso las
 * reglas asignadas son greatgrandparent, greatgreatgrandparent y
 * nephew respectivamente).
*/

% Facts: parent(Child, Parent)
parent(john, mary).
parent(john, mike).
parent(mary, alice).
parent(mary, george).
parent(mike, lisa).
parent(mike, james).
parent(susan, alice).
parent(susan, george).
parent(lisa, carol).
parent(lisa, paul).
parent(james, karen).
parent(james, daniel).
parent(juan, julio).
parent(julio, anam).
parent(maria, anam).
parent(anam, tabo).
parent(tabo, adan).

% Rule: grandparent(Grandchild, Grandparent)
grandparent(Grandchild, Grandparent) :-
    parent(Grandchild, Parent),
    parent(Parent, Grandparent).

% Rule: sibling(Person1, Person2)
sibling(Person1, Person2) :-
    parent(Person1, Parent),
    parent(Person2, Parent),
    Person1 \= Person2.

% Rule: cousin(Person1, Person2)
cousin(Person1, Person2) :-
    parent(Person1, Parent1),
    parent(Person2, Parent2),
    sibling(Parent1, Parent2).

% Rule: greatgrandparent(Greatgrandchild, Greatgrandparent)
greatgrandparent(Greatgrandchild, Greatgrandparent) :-
    parent(Greatgrandchild, Parent),
    parent(Parent, Grandparent),
    parent(Grandparent, Greatgrandparent).

% Rule: greatgreatgrandparent(Greatgreatgrandchild, Greatgreatgrandparent)
greatgreatgrandparent(Greatgreatgrandchild, Greatgreatgrandparent) :-
    greatgrandparent(Greatgreatgrandchild, Parent1),
    parent(Parent1, Greatgreatgrandparent).

% Rule nephew(Nephew, Uncle)
nephew(Nephew, Uncle) :-
    parent(Nephew, Parent1),
    sibling(Uncle, Parent1).
