### Cómo iniciar un proyecto:

Clona el repositorio y ábrelo en la interfaz de línea de comandos:

```
git clone https://github.com/tripleten-com/Iris4Friends
```

```
cd iris_for_friends
```

Crea y activa un entorno virtual:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Actualiza pip:

Windows
```
python -m pip install --actualiza pip
```
Linux/macOS
```
python3 -m pip install --actualiza pip
```

Instala las dependencias del archivo requirements.txt:

```
pip install -r requirements.txt
```

Ejecuta migraciones:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Ejecuta el proyecto:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
