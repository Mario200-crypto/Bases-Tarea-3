# Bases-Tarea-3

 Método is_trivial para la clase FunctionalDependency:

  El método implementado:
   - Usa issubset() que es un método de Python para conjuntos que verifica si un conjunto es subconjunto de otro
   - Compara si self.dependant (lado derecho) es subconjunto de self.determinant (lado izquierdo)
    Retorna True si es trivial, False si no lo es

  Suposiciones:
     - Las dependencias están bien formadas (validadas durante la inicialización)
     -  Los nombres de los atributos son sensibles a mayúsculas/minúsculas
     -  Se permiten conjuntos vacíos tanto para determinante como dependiente

  Ejemplos :

  - Caso 1: {A,B}->{B} - Trivial porque B está en {A,B}
  - Caso 2: {A,B,C}->{A,B} - Trivial porque A y B están en {A,B,C}
  - Caso 3: {A,B}->{C} - No trivial porque C no está en {A,B}
  - Caso 4: {A}->{} - Trivial con dependiente vacío

 Método is_trivial para la clase MultivaluedDependency:

   El método implementado:
    - Recibe como parámetro el heading que es el conjunto completo de atributos de la relación
      Primero verifica el Caso 1 usando issubset()
    - Si el Caso 1 no se cumple, verifica el Caso 2:
      Calcula los atributos restantes usando la diferencia de conjuntos (heading - determinant)
     Compara si el dependiente es exactamente igual a esos atributos restantes
     
   Suposiciones:
     - Las dependencias están bien formadas (validadas durante la inicialización)
     -  Los nombres de los atributos son sensibles a mayúsculas/minúsculas
     -  Se permiten conjuntos vacíos tanto para determinante como dependiente
     -  El heading debe contener todos los atributos mencionados en la dependencia

  Ejemplos :

  - Caso 1: {A,B}->->{B} - Trivial porque B está en {A,B}
  - Caso 2: {A,B}->->{C,D} - Trivial porque {C,D} contiene todos los atributos restantes
  - Caso 3: {A,B}->->{C} - No trivial porque {C} no contiene todos los atributos restantes
  - Caso 4: {A,B,C,D}->->{} - Trivial con dependiente vacío


closure – calcula y regresa el cierre:

is_superkey:

is_key:

is_relvar_in_bcnf:

is_relvar_in_4nf:
