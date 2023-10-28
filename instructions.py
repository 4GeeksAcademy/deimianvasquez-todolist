# Equipo de desarrollo
"""
    1.- Juan Guerrero
    2.- Bruno Forti
    3.- Emilio Acosta
    4.- Felix Lara
    5.- Gabriel Franco
    6.- Gonzalo Mendez
    7.- Isabel Urribarri
    9.- Jesus Santisteban 
    10.-Jose Avendaño
    11.-Jose Frometa 
    12.-Naoli Zuñiga
    13.-Omar Ramirez
    14.-Ramiro Correa
    15.-Roberto Gonzalez
    16.-Vanessa Ramirez
"""


# 1.- Crear un modelo de la tabla User
## id, username
## realcionarla con la tabla todo de uno a mucho
## crearle el metodo serialize
### Omar Ramirez 


# 2.- crear el modelo de la tabla Todo
## id, label, done
## realacionarla con la tabla user de muchos a uno
## crearle el metodo serialize
### Ramiro Correa


#3.- /user --> POST 
## recibe en el body un json ---> { "username":"nameusername"}
### Emilio Acosta


#4.- /user --> GET
## traer todos los usuarios de la API --> ["deimian","daniel"]
### Gabrierl Franco


#5.- /user/<theid> --> GET 
## responde un usuario por el id 
### Naoli Zuñiga


#6.- /user/<theid> --> DELETE
## eliminar un usuario por id 
### Jesus Santiesteban


#7.- /user/task/<username> --> POST {"label":"bañar al gato", "done":false}
## Recibe la tarea y la guarda al usuario enviado por la ulr(params)
### Gonzalo Mendez


#8.- /user/task/<username> --> PUT {"label":"bañar al perro", "done":true}
## recibe el json y actualiza la tarea del usuario enviado por la url(params)
### Jose frometa 

#9.- /user/task/<theid> --> DELETE 
## Elimina la tarea por el id que se envio por url(params)
### Jose Avendaño


#10.- /user/task/<username> --> GET  
## Trae todas las tareas de el usuario enviado por la url(params)
### Omar Ramirez



# se debe forkear el repositorio hacer su tarea y enviar el pr(pull request)


