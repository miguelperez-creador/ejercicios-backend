# auth.py

from flask import redirect, url_for, session
from functools import wraps
from models import roles_permisos

def requiere_permiso(permiso):
    def decorador(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            usuario = session.get("usuario")
            if usuario and permiso in roles_permisos.get(usuario["rol"], []):
                return f(*args, **kwargs)
            return "Acceso denegado", 403
        return decorada
    return decorador
