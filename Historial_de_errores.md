# Historial de errores que se han presentado y cómo se han solucionado

## Migraciones

Descripción: Durante la ejecución de "python manage.py makemigrations acogeloApp" o "python manage.py migrate", aparece el error:  
  
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency acogeloApp.0001_initial on database 'default'.
  
Solución: Esto es debido a que ya existen datos en la base de datos. Estando en un entorno de desarrollo, la solución más rápida es ir a la consola de Heroku para Postgres, dar clic en la pestaña "Settings" y luego "Reset database". 
En caso que eso no lo solucione, también se pueden eliminar todos los archivos de la carpeta "migrations" A EXCEPCIÓN del archivo __init__.py

