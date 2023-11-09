# 🌐 Proyecto: API Unificada para SQL y NoSQL

Este proyecto es una API unificada diseñada para interactuar con bases de datos SQL y NoSQL, facilitando el manejo de operaciones de datos con un modelo de cliente común y una interfaz de programación coherente.

## Requisitos previos

Para ejecutar este proyecto, necesitarás:

- [Node.js](https://nodejs.org/): Entorno de ejecución para JavaScript.
- [XAMPP](https://www.apachefriends.org/index.html): Para MySQL en un entorno de desarrollo local.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas): Para alojar la base de datos NoSQL en la nube.

## Instalación de Dependencias

Este proyecto requiere las siguientes dependencias principales:

- `express`: Para la creación del servidor web y manejo de rutas.
- `sequelize`: ORM para interactuar con MySQL.
- `mongoose`: ODM para interactuar con MongoDB.
- `dotenv`: Para manejar variables de entorno.
- `cors`: Para habilitar CORS.
- `morgan`: Para el registro de solicitudes HTTP.
- `mysql2`: Cliente MySQL para Node.js.
- `nodemon`: Para reiniciar automáticamente el servidor durante el desarrollo.


## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- **Modelos**: Contiene dos modelos `Cliente`, uno para Sequelize (SQL) y otro para Mongoose (NoSQL).
- **Controladores**: Dos controladores separados, `sqlCliente` y `noSqlCliente`, que manejan la lógica de negocio para cada tipo de base de datos.
- **Rutas**: Un único enrutador que utiliza dos middlewares correspondientes a los controladores SQL y NoSQL. El enrutador dirige las solicitudes al controlador adecuado basándose en el último parámetro de la URL (`sql` o `nosql`).

## Configuración

Para configurar el entorno de desarrollo:

1. Instala y configura XAMPP para MySQL.
2. Configura tu cluster en MongoDB Atlas y obtén la cadena de conexión.
3. Crea un archivo `.env` en la raíz del proyecto con las credenciales de las bases de datos.

## Instalación

Para instalar las dependencias del proyecto, ejecuta:

```bash
npm install