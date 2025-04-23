from .components import FunctionalDependency, Attribute, Relvar


def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    # TODO: Actividad 3
    """
    Dado un conjunto de atributos A, queremos A+
    Un conjunto de atributos que pueden ser determinado a partir de A usando las dependencias funcionales dadas
    """
    closure_set = set(attributes)       # hacemos una copia del conjunto dado
    changed = True                      # creamos una bandera para monitorear cambios a atributos
    
    while changed:                      # mientras se hayan hecho cambios buscamos nuevas dependencias funcionales aplicables 
        changed = False             
        for fd in functional_dependencies:
            # siendo fd = Y -> X
            left_side = fd.determinant  # Y
            right_side = fd.dependant   # X
            
            # buscamos si el determinante se encuentra en el conjunto
            # y en caso de que su dependiente no lo este lo agregamos
            if left_side.issubset(closure_set) and not right_side.issubset(closure_set):
                closure_set = closure_set.union(right_side)
                changed = True

    return closure_set


def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 4
    """
    Dado un conjunto de atributos A este será una superllave (superkey)
    si su closure incluye todos los atributos de R (heading)
    A+ ⊇ R
    """
    closure_set = closure(attributes, functional_dependencies)
    return closure_set.issuperset(heading)


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 5
    """
    Dado un conjunto de atributos A este será una llave (key) si:
        1. A es una superllave (superkey)
        2. A es irreducible
    """
    # toda llave es superllave, entonces checamos primero por eso
    if not is_superkey(attributes, heading, functional_dependencies):
        return False
    
    # checamos si algun subconjunto de A es una superllave, es decir si es reducible
    for a in attributes:
        attribute_subset = attributes - {a}     # creamos un subconjunto quitando un atributo
        if is_superkey(attribute_subset, heading, functional_dependencies):
            return False  # si existe un subconjunto de A que es superllave entonces no es irreducible
    
    return True


def is_relvar_in_bcnf(relvar: Relvar):
    # TODO: Actividad 6
    """
    Dado un relvar, este se encontrara en forma normal de Boyce-Codd si
    el determinante de la dependencia funcional es superllave (superkey)
    si X -> Y, entonces X es superllave
    """
    # checamos cada una de las dependencias funcionales en el relvar
    for fd in relvar.functional_dependencies:
        # para optimizacion checamos si la dependencia es trivial
        if not fd.is_trivial():
            # checamos si el determinante es superllave, en caso de no serlo regresamos falso ya que no cumple FNBC 
            if not is_superkey(fd.determinant, relvar.heading, relvar.functional_dependencies):
                return False
        
    return True

def is_relvar_in_4nf(relvar: Relvar):
    # TODO: Actividad 7
    """
    Dado un relvar, este se encontrara en cuarta forma normal si
        1. El relvar se encuentra en FNBC
        2. Todas las dependencias multivaluadas no triviales, el determinante es una superllave  
            si X ->-> Y, entonces X es una superllave
    """
    # checamos que el relvar este en FNBC
    if not is_relvar_in_bcnf(relvar):
        return False

    # checamos cada una de las dependencias multivaluadas
    for mvd in relvar.multivalued_dependencies:
        #checamos si es trivial o no
        if not mvd.is_trivial(relvar.heading):
            if not is_superkey(mvd.determinant, relvar.heading, relvar.functional_dependencies):
                return False

    return True
