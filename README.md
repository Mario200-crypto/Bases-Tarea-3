# Tarea 3: Normalización en Python
## Método is_trivial para la clase FunctionalDependency:

  #### *El método implementado:*
  * Usa issubset() que es un método de Python para conjuntos que verifica si un conjunto es subconjunto de otro
  * Compara si self.dependant (lado derecho) es subconjunto de self.determinant (lado izquierdo)
  * Regresa True si es trivial, False si no lo es

  #### *Suposiciones:*
  1. Las dependencias están bien formadas (validadas durante la inicialización)
  2. Los nombres de los atributos son sensibles a mayúsculas/minúsculas
  3. Se permiten conjuntos vacíos tanto para determinante como dependiente

  #### *Ejemplos:*
  * Caso 1: {A,B}->{B}     - Trivial porque B está en {A,B}, regresa True
  * Caso 2: {A,B,C}->{A,B} - Trivial porque A y B están en {A,B,C}, regresa True
  * Caso 3: {A,B}->{C}     - No trivial porque C no está en {A,B}, regresa False
  * Caso 4: {A}->{}        - Trivial con dependiente vacío, regresa True

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
  3. Se permiten conjuntos vacíos tanto para determinante como dependiente
  4. El heading debe contener todos los atributos mencionados en la dependencia

  #### *Ejemplos:*
  * Caso 1: {A,B}->->{B} - Trivial porque B está en {A,B}, regresa True
  * Caso 2: {A,B}->->{C,D} - Trivial porque {C,D} contiene todos los atributos restantes, regresa True
  * Caso 3: {A,B}->->{C} - No trivial porque {C} no contiene todos los atributos restantes, regresa False
  * Caso 4: {A,B,C,D}->->{ } - Trivial con dependiente vacío, regresa True

## closure – calcula y regresa el cierre:
  #### *El método implementado:*
  * 
     
  #### *Suposiciones:*
  1. 

  #### *Ejemplos:*
  * Caso 1: 
  * Caso 2: 
  * Caso 3: 
  * Caso 4: 
    
## is_superkey:
  #### *El método implementado:*
  * 
     
  #### *Suposiciones:*
  1. 

  #### *Ejemplos:*
  * Caso 1: 
  * Caso 2: 
  * Caso 3: 
  * Caso 4:
    
## is_key:
  #### *El método implementado:*
  * 
     
  #### *Suposiciones:*
  1. 

  #### *Ejemplos:*
  * Caso 1: 
  * Caso 2: 
  * Caso 3: 
  * Caso 4:
    
## is_relvar_in_bcnf:
  #### *El método implementado:*
  * 
     
  #### *Suposiciones:*
  1. 

  #### *Ejemplos:*
  * Caso 1: 
  * Caso 2: 
  * Caso 3: 
  * Caso 4:
    
## is_relvar_in_4nf:
  #### *El método implementado:*
  * 
     
  #### *Suposiciones:*
  1. 

  #### *Ejemplos:*
  * Caso 1: 
  * Caso 2: 
  * Caso 3: 
  * Caso 4:
