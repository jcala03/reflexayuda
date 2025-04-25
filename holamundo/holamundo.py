import reflex as rx

# Definir una clase State para manejar el estado
class AppState(rx.State):
    clicked_framework: str = ""
    
    def set_django(self):
        self.clicked_framework = "Django"
        
    def set_flask(self):
        self.clicked_framework = "Flask"
        
    def set_fastapi(self):
        self.clicked_framework = "FastAPI"

def index():
    texto_largo = """
Python es uno de los lenguajes de programación más populares del mundo, no solo por su simplicidad, sino por la gran cantidad de herramientas que ofrece para desarrollar aplicaciones web, móviles, de escritorio, y más. Dentro de estas herramientas se encuentran los **frameworks**.

Un *framework* es un conjunto de herramientas y componentes ya preparados que nos permiten construir aplicaciones de forma más rápida y ordenada. En Python existen muchos, pero los más utilizados en el ámbito del desarrollo web son:

- **Django**: un framework completo, robusto y con muchas funcionalidades integradas. Ideal para proyectos grandes.
- **Flask**: más ligero y minimalista. Perfecto para proyectos pequeños o para tener mayor control del desarrollo.
- **FastAPI**: moderno, rápido y pensado especialmente para construir APIs de forma eficiente.

Cada uno tiene sus fortalezas y casos de uso ideales. Conocerlos te permitirá elegir la mejor opción según el tipo de aplicación que quieras construir.
"""

    return rx.center(
        rx.vstack(
            rx.heading("Frameworks de Python", size="9", color="blue.700"),
            rx.markdown(texto_largo, width="80%", font_size="1.1em"),
            rx.hstack(
                rx.button("Django", on_click=AppState.set_django, color_scheme="blue"),
                rx.button("Flask", on_click=AppState.set_flask, color_scheme="blue"),
                rx.button("FastAPI", on_click=AppState.set_fastapi, color_scheme="blue"),
            ),
            # Mostrar el marco clickeado
            rx.text(f"Has hecho clic en: {AppState.clicked_framework}", font_size="1.2em", margin_top="1em"),
        ),
        padding="4em",
        min_height="100vh",
        bg="gray.50"
    )

app = rx.App()
app.add_page(index, title="Frameworks de Python")