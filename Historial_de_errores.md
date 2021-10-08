# Historial de errores que se han presentado y c�mo se han solucionado

## Migraciones

Descripci�n: Durante la ejecuci�n de "python manage.py makemigrations acogeloApp" o "python manage.py migrate", aparece el error:  
  
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency acogeloApp.0001_initial on database 'default'.
  
Soluci�n: Esto es debido a que ya existen datos en la base de datos. Estando en un entorno de desarrollo, la soluci�n m�s r�pida es ir a la consola de Heroku para Postgres, dar clic en la pesta�a "Settings" y luego "Reset database". 
En caso que eso no lo solucione, tambi�n se pueden eliminar todos los archivos de la carpeta "migrations" A EXCEPCI�N del archivo __init__.py

