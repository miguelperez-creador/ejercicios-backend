# models.py

roles_permisos = {
    "admin": ["ver_dashboard", "editar_usuarios", "acceder_configuracion"],
    "editor": ["ver_dashboard", "editar_contenido"],
    "usuario": ["ver_dashboard"]
}

class Usuario:
    def __init__(self, username, rol):
        self.username = username
        self.rol = rol

    def tiene_permiso(self, permiso):
        return permiso in roles_permisos.get(self.rol, [])
