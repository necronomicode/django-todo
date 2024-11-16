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
                "user": 1
            },
            {
                "id": 2,
                "title": "Segunda tarea",
                "description": "Esta es una descripción de la tarea",
                "due_date": "2024-11-17",
                "status": "pending",
                "user": 1
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
            "user": 3
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
    "status": "pending"
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
            "user": 1
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
    "status": "in_progress"
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
            "user": 1
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