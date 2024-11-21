# Endpoints
## Usuarios
### Registro
**Endpoint**: api/register/

**Method**: POST

**Payload**:
```json
{
    "username": "carlos",
    "password": "Carlos_123",
    "email": "carlos@django-todo.com"
}
```

**Response**:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl..."
}
```

### Login
**Endpoint**: api/login/

**Method**: POST

**Payload**:
```json
{
    "username": "carlos",
    "password": "Carlos_123"
}
```

**Response**:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl..."
}
```
### Refresh token (Nuevo token de acceso)
**Endpoint**: api/token_refresh/

**Method**: POST

**Payload**:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl..."
}
```

**Response**:
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBl..."
}
```

## Tareas
### Listar tareas
**Endpoint**: api/tasks/

**Ejemplo filtrando por estado**: /api/tasks?status=pending

**Ejemplo filtrando por fecha**: /api/tasks?date_from=2024-11-15&date_to=2024-11-17

**Ejemplo buscando subtareas**: /api/tasks?parent=1

**Method**: GET

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": [
            {
                "id": 1,
                "title": "Primera tarea",
                "description": null,
                "due_date": "2024-11-16",
                "status": "in_progress",
                "user": 1,
                "parent": null,
                "category": 1,
                "tags": [1, 2, 3]
            },
            {
                "id": 2,
                "title": "Segunda tarea",
                "description": "Esta es una descripción de la tarea",
                "due_date": "2024-11-17",
                "status": "pending",
                "user": 1,
                "parent": 1,
                "category": null,
                "tags": []
            }
        ]
    }
} 
```

### Obtener una tarea
**Endpoint**: api/tasks/<id>

**Method**: GET

**Response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 3,
            "title": "Tarea de prueba",
            "description": "descripción de prueba",
            "due_date": "2024-11-16",
            "status": "pending",
            "user": 3,
            "parent": null,
            "category": 1,
            "tags": [1, 2, 3]
        }
    }
}
```

### Crear una tarea
El únito campo obligatorio del payload es "title", el resto son opcionales.

Las opciones para status son: pending, in_progress y completed.

**endpoint**: api/tasks/

**method**: POST

**payload**:
```json
{
    "title": "Tarea de prueba",
    "description": "descripción de prueba",
    "due_date": "2024-11-16",
    "status": "pending",
    "parent": 1,
    "category": 1,
    "tags": [1, 2, 3]
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "title": "Tarea de prueba",
            "description": "descripción de prueba",
            "due_date": "2024-11-16",
            "status": "pending",
            "user": 1,
            "parent": 1,
            "category": 1,
            "tags": [1, 2, 3]
        }
    }
}
```

### Actualizar una tarea
Todos los parametros del payload son opcionales.

Las opciones para status son: pending, in_progress y completed.

**endpoint**: api/tasks/

**method**: PUT

**payload**:
```json
{
    "title": "Nuevo titulo",
    "description": "Nueva descripción",
    "due_date": "2024-11-17",
    "status": "in_progress",
    "parent": 1,
    "category": 1,
    "tags": [1, 2, 3]
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "title": "Nuevo titulo",
            "description": "Nueva descripción",
            "due_date": "2024-11-17",
            "status": "in_progress",
            "user": 1,
            "parent": 1,
            "category": 1,
            "tags": [1, 2, 3]
        }
    }
}
```

### Eliminar una tarea
**endpoint**: api/tasks/<id>

**method**: DELETE

**response**:
```json
{
    "code": 200,
    "status": "ok"
}
```

## Categorías
### Listar categorías
**Endpoint**: api/categories/

**Ejemplo filtrando por estado**: /api/categories?name=trabajo

**Ejemplo filtrando por fecha**: /api/categories?description=django

**Method**: GET

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": [
            {
                "id": 1,
                "name": "Trabajo",
                "description": "Tareas a nivel laboral",
                "user": 1
            },
            {
                "id": 2,
                "name": "Django",
                "description": "Tareas relacionadas con el framework django",
                "user": 1
            }
        ]
    }
} 
```

### Obtener una categorías
**Endpoint**: api/categories/<id>

**Method**: GET

**Response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral",
            "user": 1
        }
    }
}
```

### Crear una categoría
El únito campo obligatorio del payload es "name", description es opcional.

**endpoint**: api/categories/

**method**: POST

**payload**:
```json
{
    "name": "Trabajo",
    "description": "Tareas a nivel laboral"
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral"
        }
    }
}
```

### Actualizar una categoría
Todos los parametros del payload son opcionales.

**endpoint**: api/categories/

**method**: PUT

**payload**:
```json
{
    "name": "Trabajo",
    "description": "Tareas a nivel laboral"
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral"
        }
    }
}
```

### Eliminar una categoría
**endpoint**: api/categories/<id>

**method**: DELETE

**response**:
```json
{
    "code": 200,
    "status": "ok"
}
```

## Etiquetas
### Listar etiquetas
**Endpoint**: api/tags/

**Ejemplo filtrando por estado**: /api/tags?name=trabajo

**Ejemplo filtrando por fecha**: /api/tags?description=django

**Method**: GET

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": [
            {
                "id": 1,
                "name": "Trabajo",
                "description": "Tareas a nivel laboral",
                "user": 1
            },
            {
                "id": 2,
                "name": "Django",
                "description": "Tareas relacionadas con el framework django",
                "user": 1
            }
        ]
    }
} 
```

### Obtener una etiqueta
**Endpoint**: api/tags/<id>

**Method**: GET

**Response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral",
            "user": 1
        }
    }
}
```

### Crear una etiquetas
El únito campo obligatorio del payload es "name", description es opcional.

**endpoint**: api/tags/

**method**: POST

**payload**:
```json
{
    "name": "Trabajo",
    "description": "Tareas a nivel laboral"
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral"
        }
    }
}
```

### Actualizar una etiquetas
Todos los parametros del payload son opcionales.

**endpoint**: api/tags/

**method**: PUT

**payload**:
```json
{
    "name": "Trabajo",
    "description": "Tareas a nivel laboral"
}
```

**response**:
```json
{
    "code": 200,
    "status": "ok",
    "body": {
        "data": {
            "id": 1,
            "name": "Trabajo",
            "description": "Tareas a nivel laboral"
        }
    }
}
```

### Eliminar una etiqueta
**endpoint**: api/tags/<id>

**method**: DELETE

**response**:
```json
{
    "code": 200,
    "status": "ok"
}
```