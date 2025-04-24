# Tarea 3: Normalización en Python
## Método is_trivial para la clase FunctionalDependency:

  #### *El método implementado:*
  * Usa issubset() que es un método de Python para conjuntos que verifica si un conjunto es subconjunto de otro
  * Compara si self.dependant (lado derecho) es subconjunto de self.determinant (lado izquierdo)
  * Regresa True si es trivial, False si no lo es

  #### *Suposiciones:*
  1. Las dependencias están bien formadas (validadas durante la inicialización)
  2. Los nombres de los atributos son sensibles a mayúsculas/minúsculas

  #### *Ejemplos:*
  ```
    # Caso 1: {A,B}->{B}
    # Trivial porque B está en {A,B}, regresa True
    fd = FunctionalDependency("{A, B} -> {B}")
    print("Caso 1:", fd.is_trivial())

    # Caso 2: {A,B,C}->{A,B} 
    # Trivial porque A y B están en {A,B,C}, regresa True
    fd = FunctionalDependency("{A, B, C} -> {A, B}")
    print("Caso 2:", fd.is_trivial())

    # Caso 3: {A,B}->{C}
    # No trivial porque C no está en {A,B}, regresa False
    fd = FunctionalDependency("{A, B} -> {C}")
    print("Caso 3:", fd.is_trivial())
  ```


## Método is_trivial para la clase MultivaluedDependency:

  #### *El método implementado:*
  * Recibe como parámetro el heading que es el conjunto completo de atributos de la relación
  * Primero verifica el Caso 1, si self.dependant (lado derecho) es subconjunto de self.determinant (lado izquierdo) usando issubset()
  * Si el Caso 1 no se cumple, verifica el Caso 2:
    * Calcula los atributos restantes usando la diferencia de conjuntos (heading - determinant)
    * Compara si el dependiente es exactamente igual a esos atributos restantes
  * Regresa True si es trivial, False si no lo es
     
  #### *Suposiciones:*
  1. Las dependencias están bien formadas (validadas durante la inicialización)
  2. Los nombres de los atributos son sensibles a mayúsculas/minúsculas
  3. El heading debe contener todos los atributos mencionados en la dependencia

  #### *Ejemplos:*
  ```
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
    
  ```

## closure – calcula y regresa el cierre:
  #### *El método implementado:*
  * Dado un conjunto de atributos `A`, el metodo calcula `A+` (**cierre**)
  * `A+` es un conjunto de atributos que pueden ser determinados a partir de A usando las dependencias funcionales dadas
  * El método busca dentro de la dependencia funcional nuevos atributos dependientes que agregar
  * Cuando no existen nuevos atributos, el método para y devuelve un nuevo conjunto `A+`
     
  #### *Suposiciones:*
  1. Los atributos están definidos como instancias de `Attribute`
  2. Las dependencias funcionales están correctamente instanciadas
  3. No se permite la modificación durante la ejecución

  #### *Ejemplos:*
  ```
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
  ```
    
## is_superkey:
  #### *El método implementado:*
  * Dado un conjunto de atributos `A` se checa si es una `superkey` (**superllave**)
  * El método busca si el closure del conjunto `A` incluye todos los atributos de `R` (**heading**), se usa issubset() para comparar si closure es subconjunto del encabezado
  * Es decir si  `A+ ⊇ R`
     
  #### *Suposiciones:*
  1. Todos los atributos involucrados pertenecen al encabezado
  2. Las dependencias funcionales son completas

  #### *Ejemplos:*
 ```
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
  ```
    
## is_key:
  #### *El método implementado:*
  * Dado un conjunto de atributos A este será una llave (key) si:
        1. A es una superllave (superkey)
        2. A es irreducible
  * toda llave es superllave, entonces checamos primero por eso
  * checamos si algun subconjunto de A es una superllave, es decir si es reducible
  * creamos un subconjunto quitando un atributo
  * si existe un subconjunto de A que es superllave entonces no es irreducible
     
  #### *Suposiciones:*
  1. El conjunto de atributos es no vacío
  2. Las dependencias funcionales están bien definidas

  #### *Ejemplos:*
   ```
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
  ```
    
## is_relvar_in_bcnf:
  #### *El método implementado:*
  * Dado un relvar, este se encontrara en forma normal de Boyce-Codd si
    el determinante de la dependencia funcional es superllave (superkey)
    si X -> Y, entonces X es superllave
  * checamos cada una de las dependencias funcionales en el relvar
  * para optimizacion checamos si la dependencia es trivial
  * checamos si el determinante es superllave, en caso de no serlo regresamos falso ya que no cumple FNBC 

     
  #### *Suposiciones:*
  1. Las dependencias funcionales están correctamente definidas dentro de la relvar
  2. La relvar contiene un encabezado no vacío
  
  #### *Ejemplos:*
  ```

  ```
    
## is_relvar_in_4nf:
  #### *El método implementado:*
  * Dado un relvar, este se encontrara en cuarta forma normal si
        1. El relvar se encuentra en FNBC
        2. Todas las dependencias multivaluadas no triviales, el determinante es una superllave  
            si X ->-> Y, entonces X es una superllave
  * checamos que el relvar este en FNBC
  * checamos cada una de las dependencias multivaluadas
  * checamos si es trivial o no
     
  #### *Suposiciones:*
  1. La relvar contiene dependencias funcionales y multivaluadas válidas.
  2. Las dependencias multivaluadas siguen el formato 𝑋↠𝑌 X↠Y

  #### *Ejemplos:*
  ```

  ```
