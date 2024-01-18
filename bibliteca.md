# Casos de uso biblioteca
## Prestar Libro

- Actor: Bibliotecario
- Descripción: El bibliotecario presta un libro a un usuario.
Pasos:
El usuario solicita un libro.
El bibliotecario busca el libro en el sistema.
Si el libro está disponible, el bibliotecario registra el préstamo en el sistema.
El bibliotecario entrega el libro al usuario.
Devolver Libro
----------------
- Actor: Usuario
- Descripción: El usuario devuelve un libro que había tomado prestado.
- Pasos:
El usuario devuelve el libro en la biblioteca.
El bibliotecario recibe el libro y lo registra en el sistema.
Buscar Libro
------------
- Actor: Usuario
- Descripción: El usuario busca un libro en el sistema de la biblioteca.
- Pasos:
El usuario ingresa el título del libro en el sistema de búsqueda.
El sistema muestra los resultados de la búsqueda.
El usuario selecciona un libro de los resultados.
Renovar Préstamo
---------------
- Actor: Usuario
- Descripción: El usuario renueva el préstamo de un libro.
- Pasos:
El usuario solicita la renovación del préstamo en el sistema.
El sistema verifica la disponibilidad de la renovación.
Si es posible, el sistema renueva el préstamo y notifica al usuario.
Reservar Libro
----------------
- Actor: Usuario
Descripción: El usuario reserva un libro que actualmente no está disponible.
- Pasos:
El usuario busca el libro en el sistema.
Si el libro no está disponible, el usuario solicita una reserva.
El sistema registra la reserva y notifica al usuario cuando el libro está disponible.
