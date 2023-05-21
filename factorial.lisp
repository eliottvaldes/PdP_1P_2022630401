#|
    Autores:
    1) Delgado Acosta Luis Bernardo
    2) Díaz Jiménez Jorge Arif
    3) Valdés Luis Eliot Fabian

    Grupo: 3BV2

    Fecha de realización: 20/05/2023

    Planteamiento del problema:
    A. Calcular el factorial de un número 'N'
    B. Calcular el valor de la posición 'N' en la serie fibonacci (la serie tendra esta forma: 1, 2, 3, 5, 8, ...)
|#
(
    defun factorial(numero) ;Funcion que permite obtener el factorial de un número
        (if (= numero 0) 1 ;Si el numero llega a 0, este devolvera '1'
            (* numero (factorial (- numero 1))) ;Retorna el numero multiplicado por su valor menos 1
        )
)   
(
    defun fibonacci(pos) ;Función que permite obtener el valor de una posición 'N' en la serie Fibonacci
        (if (> pos 2) (+ (fibonacci (- pos 2)) (fibonacci (- pos 1))) ;Devuelve la suma de los dos valores anteriores al valor actual
            pos ;Devuelve el valor actual si 'pos' es menor a 2
        )
)
(
    defun menu() ;Funcion del menu principal
        (princ "Ingrese el numero para calcular factorial: ")
        (setq valor (read)) ;Obtenemos el valor de factorial que desea calcular el usuario
        (print (factorial valor)) ;Imprime el factorial
        (terpri);Salto de linea
        (princ "Ingrese la posicion de fibonacci: ")
        (setq valor2 (read));Obtenemos el valor de la posición en la serie Fibonacci que el usuario desea obtener
        (print (fibonacci valor2)) ;Imprime la posición de Fibonacci
)

(menu) ;Ejecución del programa completo