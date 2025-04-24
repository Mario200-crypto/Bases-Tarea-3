from normalization.components import *
from normalization.algorithms import *

if __name__ == "__main__":
    print("Dependencias Funcionales")
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
    print("Dependencias Multivaluadas")
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
    print("Closure")
    
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
    
    