# Práctica IX - Mongo DB (Bases de Datos)

Las bases de datos son programas que nos permiten almacenar y recuperar datos mediante capas intermedias y a veces lenguajes intermedios como SQL (Standard Query Language). Sin embargo, hoy en día existen tecnologías modernas NO-SQL que hacen más fácil el manejo de datos incorporando nuevos conceptos y liberando al programador de sintaxis complejas. Un ejemplo es *MongoDB* el cual es un motor de base de datos NO-SQL basado en *Javascript* lo que lo hace fácil de administrar, por ejemplo, si quisieramos almacenar los datos de un usuario en una colección llamada usuarios, lo único que tendríamos que hacer es `db.usuarios.insert({ nombre: "batman", correo: "bruno.diaz@hotmail.com" });`, si la colección `db.usuarios` no existe, automáticamente la crea, lo mismo si no se define un *id* para el documento anterior, este se creará automáticamente con un valor aleatorio.

## Introducción a MongoDB

Mongo está basado en el concepto de documentos, un *documento* es un fragmento de datos que posee la información de un registro o entidad. El documento define los campos de la entidad y sus valores para ese documento, podemos observar una equivalencia entre un documento y un diccionario. En el ejemplo de abajo se muestra un documento que almacena los datos de una persona:

~~~js
{
    nombre: "Ana",
    apellidos: "Gonzalez Romero",
    edad: 21,
    direccion: {
        calle: "Av. Siempre Viva",
        num_ext: 123,
        num_int: 0,
        colonia: "Condesa",
        ciudad: "Del. Miguel Hidalgo",
        estado: "Ciudad de México",
        codigo_postal: "01600",
        ubicacion: {
            latitud: -98.73232,
            longitud: 123.1234,
        }
    }
}
~~~

Como puedes observar, todos los datos relacionados a una sola persona son almacenados en un documento con la notación de *javascript*, en realidad todos los documentos al final son transformados a un archivo *BSON* derivado de *JSON*.

Los documentos en mongo pueden contener distintos campos entre sí, por ejemplo, algunos documentos podrían tener el campo `direccion.ubicacion` o el campo `edad`, lo cual en modelos *SQL* no estaría permitido.

Los documentos son almacenados dentro de colecciones, las *colecciones* determinan un conjunto de documentos que tienen relación entre sí y pueden ser indexados. En el ejemplo anterior, podríamos almacenar todos los documentos referentes a personas en la colección `personas`. Las colecciones a su vez se guardan dentro de bases de datos que representan el conjunto de colecciones disponibles para nuestro sistema. Entonces, para poder utilizar mongo debemos hacerlo a través de una base de datos, luego a través de una colección y finalmente a través de documentos.

El ejemplo de abajo selecciona una base de datos (si no existe la crea), accede a la colección `personas` (si no existe la crea) y finalmente inserta un documento en ella:

~~~js
use MiDB;

db.personas.insert({
    nombre: "Ana",
    apellidos: "Gonzalez Romero",
    edad: 21,
    correo: "ana@gmail.com"
});
~~~

## Insertar multiples documentos en una colección

Ya vimos que el método `db.mi_coleccion.insert(...)` nos permite insertar un documento en la colección `mi_colección`, si embargo, si enviamos un arreglo podemos insertar más de uno.

~~~js
db.productos.insert([
    {
        nombre: "Droga-Cola",
        descripcion: "Refresco que droga",
        costo: 12.5
    },
    {
        nombre: "Galletas Marías",
        descripcion: "Galletas que engordan",
        costo: 6.5
    },
    {
        nombre: "Gansito",
        descripcion: "Recuerdame :')",
        costo: 7
    }
]);
~~~

## Buscar un documento

El `query` en la búsqueda de documentos contiene los campos que deberán cumplir ciertas condiciones, la más común es la condición de igualdad, por ejemplo, si tenemos el query:

~~~js
const query = {
    nombre: "Coca-Cola",
    bloqueado: false
};
~~~

El `query` anterior buscaría en la colección todos los documentos cuyo nombre es exactamente igual a `"Coca-Cola"` y cuyo campo `bloqueado` es exactamente `false`.

En mongo existen operadores de consulta, los cuales permiten hacer busquedas sobre los campos más sofisticadas, por ejemplo:

~~~js
const query = {
    existencias: { $gt: 100 }
};
~~~

El `query` anterior busca todos los documentos en la colección cuyo campo `existencias` es mayor estricto que `100`, si modificamos por `$gte` obtendremos los que son mayores o iguales a `100`. Otros operadores son `$lt` y `$lte` que representan menor estricto y menor o igual.

La lista completa de operadores puede ser consultada en https://docs.mongodb.com/manual/reference/operator/query/

Dos operadores principales son `$and` y `$or`, el operador `$and` funciona por defecto con todas las condiciones definidas en el `query`, pero si queremos que se cumpla una condición u otra, hacemos:

~~~js
const query = {
    $or: [
        {
            costo: { $gte: 10 }
        },
        {
            existencias: { $lte: 100 }
        }
    ]
};
~~~

Finalmente un operador especial llamado `$regex` nos permitirá evaluar expresiones regulares dentro de patrones de texto, por ejemplo, detectar todos los usuarios que poseen correo de `gmail`.

~~~js
const query = {
    email: { $regex: "gmail", $options: "i" }
};
~~~

El `query` anterior recupera todos los documentos que contienen en su campo email (de texto) la palabra `gmail`, el `$options: "i"` especifica que sea insensitivo a minúsculas y mayúsculas.

~~~js
// Todos los que empiezan con PA
const query = {
    nombre: { $regex: "^pa", $options: "i" }
}

// Todos los que terminan con CO
const query = {
    nombre: { $regex: "CO$", $options: "i" }
}

// Todos los que contenienen con NA
const query = {
    nombre: { $regex: "NA", $options: "i" }
}
~~~

Mongo nos permite enviar un objeto de proyección, para esconder campos, o mostrar solo los campos de interés, el `_id` siempre se muestra, a menos que se oculte manualmente

~~~js
const query = {
    email: "pepe@gmail.com"
};
// Oculta el _id y muestra solo los campos nombre, email
const proj = {
    _id: 0,
    nombre: 1,
    email: 1
};
db.productos.findOne(query, proj);
~~~

Si queremos buscar toda una colección usamos `find` en lugar de `findOne` pero hay que tener cuidado ya que no hay callback.

~~~js
const query = {
    descripcion: { $regex: "refresco", $options: "i" }
};
db.productos.find(query).pretty();
~~~

## Actualizar un documento

Para actualizar definimos un `query` el cual va a definir que elementos deben actualizarse, luego podemos usar `updateOne` para actualizar solo uno, que es lo recomendable para evitar problemas. El operador `$set` nos permite ajustar todos los campos del documento a sus nuevos valores, si no existían los crea y sino lo reemplaza, para eliminar campos revisa el operador `$unset`.

> Agregar un campo que no existia

~~~js
const query = {
    email: "pepe@gmail.com"
};
db.collecion("usuarios").updateOne(query, {
    $set: {
        avatar: "http://placehold.it/300x300"
    }
});
~~~

## Eliminar un documento

~~~js
const query = {
    email: "pepe@gmail.com"
};
db.usuarios.removeOne(query);
~~~

## Conectar MongoDB en Python

Para poder tener acceso a la base de datos de mongo a través de python debemos instalar `pymongo` mediante `pip`

* Instalar *pymongo*: `pip install pymongo`

* Importar *pymongo*: `from pymongo import MongoClient`

* Crear una conexión: `client = MongoClient()` (Si es necesario especificar toda la ruta `client = MongoClient("mongodb://localhost:27017")`)

* Enlazar a la base de datos: `db = client.MiDB` (alternativamente `db = client["MiDB"]`)

## Insertar un documento con PyMongo

Podemos almacenar cualquier diccionario serializable en python, observa que en python los diccionarios llevan comillas en sus claves a diferencia de javascript.

~~~py
from pymongo import MongoClient

client = MongoClient()

db = client.mi_tienda

result = db.productos.insert_one({
    "nombre": "Droga-Cola",
    "descripcion": "Refresco que droga",
    "costo": 12.5
})
~~~

## Realizar un busqueda en PyMongo

Las búsquedas devuelven un cursor iterable, que mediante un `for` podemos recorrer sus documentos, alternativamente `find_one(...)` nos devolverá sólo un documento o `None`.

~~~py
from pymongo import MongoClient

client = MongoClient()

db = client.mi_tienda

cursor = db.productos.find()

for producto in cursor:
    print(producto)
~~~

Si queremos hacer una búsqueda avanzada hacemos `cursor = db.productos.find({ "costo": { "$gte": 10 } })` que hace una búsqueda de todos los productos, cuyo campo `costo` es mayor o igual a `10`.

## Problemas

* Definir los campos que debería contener un documento que almacena los datos de un experimiento, por ejemplo, `tiempo`, `temperatura`, `densidad`, etc.

* Crear una colección llamada `experimentos` con al menos 200 experimentos aleatorios.

* Recuperar todos los experimentos y guardarlos en un archivo de texto con la siguiente estructura, por ejemplo, si los campos de cada experimento son: `tiempo`, `temperatura`, `densidad`, se debería construir el archivo:

~~~txt
TIEMPO: 5 MIN
TEMPERATURA: 127 C
DENSIDAD: 5.2 U
-------------------------------
TIEMPO: 10 MIN
TEMPERATURA: 58 C
DENSIDAD: 6.2 U
-------------------------------
TIEMPO: 15 MIN
TEMPERATURA: 69 C
DENSIDAD: 3.1 U
-------------------------------
...
~~~

* Crear un programa que recupere los datos del archivo anterior y los guarde en la colección `experimentos_recuperados`.

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
