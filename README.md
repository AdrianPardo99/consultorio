## Development

### Git/Commit conventions

We use https://www.conventionalcommits.org/en/v1.0.0/

### Development Environment Setup

### Docker

Install `docker` and run project `docker-compose up -d`

If you make any changes that requires a new Docker build:
`docker-compose up --build -d --remove-orphans`

To run one-off processes on container, for example:
`docker-compose run api python consultorio/manage.py makemigrations`

To debug using pdb or ipdb
`docker attach {containerId}`

### Environment Variables

Create a file named `.env` inside root directory and fill environments in the way:

```
DEBUG=True
STAGE=local
```

### Setup first time app

__For run application localy:__

1. You need to create .env file with missing information for work with app
2. You only need to download docker-compose and installed
3. You need to run the next command `docker-compose up --build -d`
4. You need to run migrations for create schema and more in database `docker-compose run api python consultorio/manage.py migrate`

Have fun

__For run application in cloud:__
 
1. Add envars to project (Sometimes you need to setup and add github connection and you can set your envars)
2. Create a file for install requirements and run migrations like locally in point 4
3. Connect or config your app for CI/CD

Have fun

## Swager doc

The application has two endpoints and is a Restfull API, it means you can `GET(list, retrieve)`, `POST(create)`, `PATH(partial_update)`, `DELETE(delete)` objects in database

`BASE_URL=<url>/v1/`

### Endpoints

__Paciente__

- `pacientes/` - It allows filter by `nombre` you only need to follow the next structure `pacientes/?nombre=<name_here>`, allow methods `POST, GET`
- `pacientes/<paciente_pk>/` - It check `paciente` where `paciente_pk` is the id of the database, allow_methods `PATCH, GET, DELETE`
- `citas/` - It allows filter by `fecha` you only need to follow the next structure `citas/?fecha=<YYYY-MM-DD>`, allow methods `POST, GET`
- `citas/<cita_pk>/` - It check `cita` where `cita_pk` is the id of the database, allow_methods `PATCH, GET, DELETE`

#### How to create paciente

```python
    import requests
    # Example following using python you can write this in whatever programming language
    payload = {
        "nombre":"Juan",
        "ap":"Maya", # Apellido paterno
        "am":"Maya", # Apellido materno
        "edad":25,
        "peso":78.5,
        "estatura":180,
        "cc":10,
        "telefono":"5518179786",
        "email":"email@test.com",
        "pa": ["vomito", "colitis"], # Problemas actuales enviar en forma de lista de acuerdo a las opciones en minusculas que aparecen en el archivo modelos/__init__.py
        "af": ["obesidad", "diabetes"], # Antecedentes familiares enviar en forma de lista de acuerdo a las opciones en minusculas que aparecen en el archivo modelos/__init__.py
        "ea": False # Embarazo actual es solo enviar true or false
    }
    url = "http://direccion.com/v1/pacientes/"
    response=requests.post(url,payload)

    if response.status_code==201:
        # The paciente was succesfully created
    else:
        # You have some errors check message
```

#### How to update paciente

```python
    import requests
    # Example following using python you can write this in whatever programming language
    payload = {
        "pa": ["vomito", "colitis"],
        "af": ["obesidad", "diabetes"],
    }
    id_of_paciente = 1
    url = f"http://direccion.com/v1/pacientes/{id_of_paciente}/"
    response=requests.patch(url,payload)

    if response.status_code==200:
        # The paciente was succesfully updated
    else:
        # You have some errors check message sometimes paciente doesn't exists 404=status_code
```

#### How to list paciente

```python
    import requests
    # Example following using python you can write this in whatever programming language
    name_filter = "Octavio"
    url = f"http://direccion.com/v1/pacientes/"
    # Using name filter
    url_params = f"http://direccion.com/v1/pacientes/?nombre={name_filter}"
    response=requests.get(url)

    if response.status_code==200:
        # The pacientes list
    else:
        # You have some errors check message sometimes paciente doesn't exists 404=status_code
```

#### How to retrive paciente

```python
    import requests
    # Example following using python you can write this in whatever programming language
    id_of_paciente = 1
    url = f"http://direccion.com/v1/pacientes/{id_of_paciente}/"
    response=requests.get(url)

    if response.status_code==200:
        # The paciente was found
    else:
        # You have some errors check message sometimes paciente doesn't exists 404=status_code
```

#### How to delete paciente

```python
    import requests
    # Example following using python you can write this in whatever programming language
    id_of_paciente = 1
    url = f"http://direccion.com/v1/pacientes/{id_of_paciente}/"
    response=requests.delete(url)

    if response.status_code==204:
        # The paciente was deleted succesfully
    else:
        # You have some errors check message sometimes paciente doesn't exists 404=status_code
```

#### How to create cita

```python
    import requests
    # Example following using python you can write this in whatever programming language
    payload = {
        "paciente": 1, # Id del paciente
        "fecha": "YYYY-MM-DDTHH:mm:ss" # Formato iso
    }
    url = "http://direccion.com/v1/citas/"
    response=requests.post(url,payload)

    if response.status_code==201:
        # The cita was succesfully created
    else:
        # You have some errors check message
```

#### How to update cita

```python
    import requests
    # Example following using python you can write this in whatever programming language
    payload = {
        "fecha": "YYYY-MM-DDTHH:mm:ss" # Formato iso
    }
    id_of_cita = 1
    url = f"http://direccion.com/v1/citas/{id_of_cita}/"
    response=requests.patch(url,payload)

    if response.status_code==200:
        # The cita was succesfully updated
    else:
        # You have some errors check message sometimes cita doesn't exists 404=status_code
```

#### How to list cita

```python
    import requests
    # Example following using python you can write this in whatever programming language
    date_filter = "YYYY-MM-DD"
    url = f"http://direccion.com/v1/citas/"
    # Using date filter
    url_params = f"http://direccion.com/v1/citas/?fecha={date_filter}"
    response=requests.get(url)

    if response.status_code==200:
        # The citas list
    else:
        # You have some errors check message sometimes cita doesn't exists 404=status_code
```

#### How to retrive cita

```python
    import requests
    # Example following using python you can write this in whatever programming language
    id_of_cita = 1
    url = f"http://direccion.com/v1/citas/{id_of_cita}/"
    response=requests.get(url)

    if response.status_code==200:
        # The cita was found
    else:
        # You have some errors check message sometimes cita doesn't exists 404=status_code
```

#### How to delete cita

```python
    import requests
    # Example following using python you can write this in whatever programming language
    id_of_cita = 1
    url = f"http://direccion.com/v1/citas/{id_of_cita}/"
    response=requests.delete(url)

    if response.status_code==204:
        # The cita was deleted succesfully
    else:
        # You have some errors check message sometimes cita doesn't exists 404=status_code
```