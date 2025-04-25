from normalization.components import *
from normalization.algorithms import *

if __name__ == "__main__":
    print("\nDependencias Funcionales")
    # Caso 1: {A,B}->{A,B}
    # Trivial porque B está en {A,B}, regresa True
    fd = FunctionalDependency("{A, B} -> {A,B}")
    print("Caso 1:", fd.is_trivial())

    # Caso 2: {A,B,C}->{A,B} 
    # Trivial porque A y B están en {A,B,C}, regresa True
    fd = FunctionalDependency("{A, B, C} -> {A, B}")
    print("Caso 2:", fd.is_trivial())

    # Caso 3: {A,B}->{C}
    # No trivial porque C no está en {A,B}, regresa False
    fd = FunctionalDependency("{A, B} -> {C}")
    print("Caso 3:", fd.is_trivial())
    
    ##############
    print("\nDependencias Multivaluadas")
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")
    D = Attribute("D")
    heading = {A, B, C, D}
    
    # Caso 1: {A,B}->->{B}
    # Trivial porque B está en {A,B}, regresa True
    mvd = MultivaluedDependency("{A, B} ->-> {B}")
    print("Caso 1:", mvd.is_trivial(heading))  
    
    # Caso 2: {A,B}->->{C,D}
    # Trivial porque {C,D} contiene todos los atributos restantes, regresa True
    mvd = MultivaluedDependency("{A, B} ->-> {C, D}")
    print("Caso 1:", mvd.is_trivial(heading))  
    
    # Caso 3: {A,B}->->{C} 
    # No trivial porque {C} no contiene todos los atributos restantes, regresa False
    mvd = MultivaluedDependency("{A, B} ->-> {C}")
    print("Caso 1:", mvd.is_trivial(heading))  
    
    ##############
    print("\nClosure")
    
    fd1 = FunctionalDependency("{A}->{B}")
    fd2 = FunctionalDependency("{B}->{C}")
    fd3 = FunctionalDependency("{C}->{D}")
    
    # Caso 1: devuelve {A, B, C, D} ya que todos los atributos estan relacionados
    closure_set = closure({A}, {fd1, fd2, fd3})
    print(closure_set)
    
    # Caso 2: devuelve {A, B} ya que no todos los atributos estan relacionados
    closure_set = closure({A}, {fd1, fd3})
    print(closure_set)
    
    # Caso 3: devuelve {A} ya que nada esta relacionado
    closure_set = closure({A}, {})
    print(closure_set)
    
    ###########
    print("\nSuperkey")
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")
    D = Attribute("D")
    heading = {A, B, C, D}
    fd1 = FunctionalDependency("{A}->{B}")
    fd2 = FunctionalDependency("{B}->{C}")
    fd3 = FunctionalDependency("{C}->{D}")
    
    #Caso 1: devuelve True porque conjunto = heading, sin dependencias 
    print(is_superkey({A, B, C, D}, heading, {}))
    
    #Caso 2: devuelve True porque closure(conjunto) es superconjunto de R
    print(is_superkey({A}, heading, {fd1, fd2, fd3}))
    
    #Caso 3: devuelve False porque closure(conjunto) no es superconjunto de R 
    print(is_superkey({A}, heading, {fd1}))
    
    ##########
    print("\nKey")
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")
    D = Attribute("D")
    heading = {A, B, C}
    fd1 = FunctionalDependency("{A}->{B}")
    fd2 = FunctionalDependency("{B}->{C}")
    fd3 = FunctionalDependency("{C}->{D}")
    
    #Caso 1: devuelve True porque conjunto = heading, sin dependencias 
    print(is_key({A, B, C}, heading, {}))
    
    #Caso 2: devuelve True porque closure(conjunto) = heading
    print(is_key({A}, heading, {fd1, fd2}))
    
    #Caso 3: devuelve False porque el conjunto no es superllave
    print(is_key({A}, heading, {fd1}))
    
    #Caso 4: devuelve False porque el conjunto puede reducirse y seguir siendo superllave
    print(is_key({A, D}, heading, {fd1, fd2, fd3}))

    ########
    print("\nFNBC")
    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{A} -> {C}")
    
    # Caso 1: regresa False porque ninguna de las dependencias agrega el atributo D
    # por lo que ningun determinante es superkey del encabezado
    r1 = Relvar({"A", "B", "C", "D"}, {fd1, fd2})
    print(is_relvar_in_bcnf(r1))

    # Caso 2: regresa True porque todos los determinantes son superkey del encabezado
    r2 = Relvar({"A", "B", "C"}, {fd1, fd2})
    print(is_relvar_in_bcnf(r2))
    
    ######
    print("\n4NF")
    mvd1 = MultivaluedDependency("{A} ->-> {B}")
    mvd2 = MultivaluedDependency("{B} ->-> {A}")
    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{A} -> {C}")
    
    # Caso 1: devuelve False ya que el relvar no cumple FNBC
    r1 = Relvar({"A", "B", "C", "D"}, {fd1, fd2}, {mvd1})
    print(is_relvar_in_4nf(r1))

    # Caso 2: devuelve False porque el relvar esta en FNBC pero B no es superkey
    r2 = Relvar({"A", "B", "C"}, {fd1, fd2}, {mvd2})
    print(is_relvar_in_4nf(r2))
    
    # Caso 3: devuelve True porque el relvar esta en FNBC y A es superkey
    r3 = Relvar({"A", "B", "C"}, {fd1, fd2}, {mvd1})
    print(is_relvar_in_4nf(r3))
    
