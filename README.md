# SSBW
Repositorio para la asignatura de Sistemas Software Basados en Web (SSBW) del MII de la UGR. 

Durante el curso iremos desarrollando una aplicación web, inspirada en [Turgranada](https://www.turgranada.es/cosas-que-hacer/turismo-activo-y-de-naturaleza/excursiones-y-senderismo/), en la que se puedan consultar senderos y rutas por Granada, añadir fotos, mapas y comentarios por parte de los visitantes.

La división por tareas es la siguiente:
 * Tarea 0: configuración del entorno de desarrollo.
 * [Tarea 1](https://github.com/PedroMFC/SSBW/commit/b317465fe6599d5c6b10598812c3efef450d9b17): conexión con la base de datos (mongoDB).
 * [Tarea 2](https://github.com/PedroMFC/SSBW/commit/2f7378167ee994b48e2378237bff5a898cf4faf2): Django.
 * [Tarea 3](https://github.com/PedroMFC/SSBW/commit/9495758ff05062cc23dd1cfc8ead213d3b86bb2e): Framework CCS. Template sencillo. Se ha añadido la opción de tarjetas para las excursiones aunque se ha mejorado en la tera 4.
 * [Tarea 4](https://github.com/PedroMFC/SSBW/commit/a38c644702c284799e30c7408da56664e52571e0): vista de detalle para cada excursión, así como la posibilidad de añadir, borrar, y editar registros.Haremos uso de formularios.
 * [Tarea 5](https://github.com/PedroMFC/SSBW/commit/93bcd49790bbc428a039c953093a4b8c97b0bdf6): autenficación, autorización de los usuarios sobre la BD, y un registro de eventos en la aplicación.
 * [Tarea 6](https://github.com/PedroMFC/SSBW/commit/25e42e724420aefb3f4f033b4fc11be76b766b4b): creación de una api RESTFULL usando `django-rest-framework-mongoengine`. También algo de restricción de acceso a la base de datos usando JWT Authentication.