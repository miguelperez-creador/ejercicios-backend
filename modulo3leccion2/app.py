# app.py

from flask import Flask, session, redirect, url_for
from models import Usuario
from auth import requiere_permiso

app = Flask(__name__)
app.secret_key = "secreto_super_seguro"

# Simular inicio de sesión (solo para pruebas)
@app.route("/login/<rol>")
def login(rol):
    usuario = Usuario("usuario_demo", rol)
    session["usuario"] = {"username": usuario.username, "rol": usuario.rol}
    return f"Sesión iniciada como {rol}"

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return "Sesión cerrada"

@app.route("/")
def inicio():
    return "Inicio público"

@app.route("/dashboard")
@requiere_permiso("ver_dashboard")
def dashboard():
    return "Bienvenido al Dashboard"

@app.route("/admin")
@requiere_permiso("editar_usuarios")
def admin():
    return "Zona de administración"

if __name__ == "__main__":
    app.run(debug=True)
