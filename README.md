# org-backend
backend from project using Python and Django
# Para poder trabajar sobre el código ya existente:

## Desde la consola del Git Bash:

mkdir \<directorio>  
cd \<directorio>  
git init  
git clone -b dev --single-branch <url>  
cd \<project>  
git branch -a (verificar que sea dev)  

## Desde el Visual Studio:
Abrir la carpeta <directorio> y el powershell en ese <directorio>  
Ejecutar:  
Set-ExecutionPolicy Unrestricted -Scope Process  
python -m venv env  
.\env\Scripts\activate  
pip install django  
pip install djangorestframework  
pip install pillow (solo para cuando se va a usar ImageField type en los módulos)  
Realizar las modificaciones al código   
git add \<cada archivo, evitar el uso del comodín *>  
git commit -m "Un mensaje de verdad útil"  
Recordar hacer git pull SIEMPRE antes del git push  

# Para cargar la base de datos:
## Desde DBeaver
Crear una nueva conexión de tipo SQLite.   
En el campo PATH abrir el explorador de carpetas e ir a la ubicación del código del proyecto y elegir el archivo que se llama “db.sqlite3”  
Dar clic abajo en el botón “Test connection” para verificar   
## Luego, desde el Visual Studio  
python manage.py makemigrations acogeloApp → para crear los archivos de las migraciones  
python manage.py migrate → para efectuar la migración  

