# Tarea 3: Normalización en Python
## Método is_trivial para la clase FunctionalDependency:

  #### *El método implementado:*
  * Usa `issubset()` que es un método de Python para conjuntos que verifica si un conjunto es subconjunto de otro
  * Compara si `self.dependant` (lado derecho) es subconjunto de `self.determinant` (lado izquierdo)
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
  * Recibe como parámetro el `heading` que es el conjunto completo de atributos de la relación
  * Primero verifica el Caso 1, si `self.dependant` (lado derecho) es subconjunto de `self.determinant` (lado izquierdo) usando `issubset()`
  * Si el Caso 1 no se cumple, verifica el Caso 2:
    * Calcula los atributos restantes usando la diferencia de conjuntos (heading - determinant)
    * Compara si el dependiente es exactamente igual a esos atributos restantes
  * Regresa True si es trivial, False si no lo es
     
  #### *Suposiciones:*
  1. Las dependencias están bien formadas (validadas durante la inicialización)
  2. Los nombres de los atributos son sensibles a mayúsculas/minúsculas
  3. El `heading` debe contener todos los atributos mencionados en la dependencia

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
  * Dado un conjunto de atributos `A`, el metodo calcula `A+` (**closure**)
  * `A+` es un conjunto de atributos que pueden ser determinados a partir de A usando las dependencias funcionales dadas
  * El método busca dentro de la dependencia funcional nuevos atributos dependientes que agregar
  * Cuando no existen nuevos atributos, el método para y devuelve un nuevo conjunto `A+`
  * Regresa un conjunto nuevo
     
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
  * Dado un conjunto de atributos `A` el método checa si es una `superkey` (**superllave**)
  * Busca si el closure del conjunto `A` incluye todos los atributos de `R` (**heading**), se usa `issuperset()` para comparar si `closure` es superconjunto del encabezado
  * Es decir si  `A+ ⊇ R`
  * Regresa True si es `superkey`, False si no lo es
     
  #### *Suposiciones:*
  1. Todos los atributos involucrados pertenecen al `heading`
  2. Las dependencias funcionales son completas

  #### *Ejemplos:*
  ```
  A = Attribute("A")
  B = Attribute("B")
  C = Attribute("C")
  D = Attribute("D")
  heading = {A, B, C, D}
  fd1 = FunctionalDependency("{A}->{B}")
  fd2 = FunctionalDependency("{B}->{C}")
  fd3 = FunctionalDependency("{C}->{D}")
  
  set_one = {A, B, C, D}
  set_two = {}
  #Caso 1: devuelve True porque set_one = heading, sin dependencias 
  print(is_superkey(set_one, heading, {}))
  
  #Caso 2: devuelve True porque closure({A}) es superconjunto de R
  print(is_superkey({A}, heading, {fd1, fd2, fd3}))
  
  #Caso 3: devuelve False porque closure({A}) no es superconjunto de R 
  print(is_superkey({A}, heading, {fd1}))
  ```
    
## is_key:
  #### *El método implementado:*
  * Dado un conjunto de atributos `A` se checa si es una `key` (**llave**) si:
    1. `A` es una `superkey` (**superllave**)
    2. `A` es irreducible
  * Primero se checa si `A` es `superkey` (**superllave**), ya que toda `key` es una `superkey` pero no al réves, utilizando el metodo `is_superkey`
  * En caso de ser `superkey` se busca si algun subconjunto de `A` es también es `superkey`, es decir si es reducible
  * Para esto creamos un subconjunto quitando un atributo y si existe un subconjunto de `A` que es `superkey` entonces no es irreducible
  * Regresa True si es `key`, False si no lo es
     
  #### *Suposiciones:*
  1. El conjunto de atributos es no vacío
  2. Las dependencias funcionales están bien definidas

  #### *Ejemplos:*
   ```
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
   ```
    
## is_relvar_in_bcnf:
  #### *El método implementado:*
  * Dado un relvar, se checa si este esta en forma normal de Boyce-Codd (*FNBC*) si el determinante de la dependencia funcional es `superkey`
    * Es decir si 𝑋 → 𝑌, entonces 𝑋 es `superkey`
  * Para cada una de las dependencias funcionales en el relvar se checa:
    * Si la dependecia es trivial, en caso de serlo cumple *FNBC*
    * Si el determinante es `superkey`, en caso de no serlo no cumple *FNBC*
  * Regresa True si cumple la *FNBC*, False si no la cumple

  #### *Suposiciones:*
  1. Las dependencias funcionales están correctamente definidas dentro de la relvar
  2. La relvar contiene un encabezado no vacío
  
  #### *Ejemplos:*
  ```
  fd1 = FunctionalDependency("{A} -> {B}")
  fd2 = FunctionalDependency("{A} -> {C}")
  
  # Caso 1: regresa False porque ninguna de las dependencias agrega el atributo D
  # por lo que ningun determinante es superkey del encabezado
  r1 = Relvar({"A", "B", "C", "D"}, {fd1, fd2})
  print(is_relvar_in_bcnf(r1))

  # Caso 2: regresa True porque todos los determinantes son superkey del encabezado
  r2 = Relvar({"A", "B", "C"}, {fd1, fd2})
  print(is_relvar_in_bcnf(r2))
  ```
    
## is_relvar_in_4nf:
  #### *El método implementado:*
  * Dado un relvar, se checa si cumple con la  cuarta forma normal (*4NF*)
  * Por lo que debe de cumplir con:
    1. La relvar se encuentra en *FNBC*
    2. Para todas las dependencias multivaluadas no triviales, el determinante es una `superkey` (*si 𝑋↠𝑌, entonces 𝑋 es una `superkey`*)
  * Entonces, primero checamos que el relvar este en *FNBC* con `is_relvar_in_bcnf` en caso de regresar True
  * Para cada una de las dependencias multivaluadas:
    * Checamos si es trivial o no con `is_trivial`
    * De no ser trivial se checa si el `mvd.determinant` es `superkey` con `is_superkey`
  * Regresa True si cumple con *4NF*, False si no la cumple
     
  #### *Suposiciones:*
  1. La relvar contiene dependencias funcionales y multivaluadas válidas
  2. Las dependencias multivaluadas siguen el formato 𝑋↠𝑌

  #### *Ejemplos:*
  ```
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
  ```
