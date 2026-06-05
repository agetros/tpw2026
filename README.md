# Blog Django

Aplicacion web de blog desarrollada con Django.

Incluye:

- Publicaciones con titulo, contenido y categorias.
- Comentarios por publicacion.
- Busqueda por titulo, contenido o categorias.
- Paginacion en el listado de publicaciones.
- Autenticacion de usuarios (login/logout).
- CRUD de publicaciones para usuarios autenticados.

## Stack

- Python 3
- Django 6
- SQLite (archivo local `db.sqlite3`)
- Bootstrap (archivos estaticos locales en `posts/static/blog`)

## Estructura Principal

- `blog/`: configuracion del proyecto (settings, urls, wsgi, asgi)
- `posts/`: app principal (modelos, vistas, formularios, templates)
- `db.sqlite3`: base de datos local
- `manage.py`: punto de entrada para comandos Django

## Modelos

- `Post`
  - `title`
  - `content`
  - `author` (relacion con usuario de Django)
  - `created_at`
  - `updated_at`
  - `categories`
- `Comment`
  - `post` (relacion con `Post`)
  - `author` (relacion con usuario de Django)
  - `content`
  - `created_at`

## Requisitos Previos

- Python 3 instalado
- Entorno virtual recomendado (venv o pyenv)

## Instalacion y Ejecucion

1. Clonar el repositorio y entrar a la carpeta del proyecto.

2. Crear y activar entorno virtual (ejemplo con `venv`):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Instalar dependencias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

1. Ejecutar migraciones:

```bash
python manage.py migrate
```

1. (Opcional) Crear superusuario para el panel admin:

```bash
python manage.py createsuperuser
```

1. Levantar servidor de desarrollo:

```bash
python manage.py runserver
```

1. Abrir en navegador:

```text
http://127.0.0.1:8000/
```

## Rutas Relevantes

- `/`: listado de publicaciones
- `/post/crear/`: crear publicacion (requiere login)
- `/post/<id>/`: detalle de publicacion y comentarios
- `/post/<id>/editar/`: editar publicacion (requiere login)
- `/post/<id>/eliminar/`: eliminar publicacion (requiere login)
- `/login/`: iniciar sesion
- `/logout/`: cerrar sesion
- `/admin/`: panel de administracion

## Funcionalidades Implementadas

- Busqueda en listado usando parametro `search` por query string.
- Paginacion de publicaciones (5 por pagina).
- Mensajes de confirmacion para crear, editar, eliminar y comentar.
- Redireccion a login al intentar comentar sin autenticacion.

## Comandos Utiles

```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test
```

## Dependencias

El proyecto usa las dependencias definidas en `requirements.txt`:

```text
asgiref==3.11.1
Django==6.0.5
sqlparse==0.5.5
```

## Estado de Tests

Actualmente existe el archivo base de tests (`posts/tests.py`) sin casos implementados.

## Notas

- `DEBUG=True` en configuracion actual (`blog/settings.py`), apropiado solo para desarrollo.
- `ALLOWED_HOSTS` esta vacio en la configuracion actual.
