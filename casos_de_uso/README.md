# APP TRANSPORTE.
###  CASO DE USO *DEFINIR TRANSPORTE*.

| Nombre caso de uso | Definir transporte |
|--------------------|--------------------------|
| Actor | Administrador. |
| Resumen | El administrador define un medio de transporte para el Usuario. |
| Precondiciones | Se registra el medio de transporte y se comprueba la disponibilidad del mismo.|
| Postcondiciones | El transporte llega al destino elegido por el usuario.|


### ACTOR *USUARIO*.

| Usuario | Aplicación de transporte |
|--------------------|--------------------------|
| Breve descripción | Los usuarios pueden registrarse en la app de transporte para su utilización. |
| Flujo de eventos | El usuario se registra y puede planear una ruta por geolocalización |
| Flujo básico | El usuario puede registrarse en la app tras darse de alta, tras el *log in* y verificar sus credenciales puede acceder a planear su ruta, a partir de ahi el sistema externo puede sugerir destinos interesantes al pulsar en el botón '' *destinos interesantes* '' o mostrar puntos de interes en la ruta al pulsar el botón con el mismo nombre. También el usuario estará asistido en todo momento por geolocalización of.|
| Flujos alternativos | El usuario puede fallar al realizar el *login* |

