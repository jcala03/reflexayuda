import reflex as rx

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("¿Qué es Reflex?", size="8"),
        rx.text(
            "Reflex es un framework web moderno que permite construir aplicaciones web "
            "usando únicamente Python. Está diseñado para ser simple, rápido y potente.",
            size="5"
        ),
        rx.heading("Características principales", size="7", padding_top="2em"),
        rx.text(
            "- Usa solo Python: no necesitas HTML, CSS ni JavaScript.\n"
            "- Reactivo: la interfaz se actualiza automáticamente con los cambios de estado.\n"
            "- Integración con React: genera componentes React optimizados.\n"
            "- Fácil de aprender: ideal para quienes ya dominan Python.",
            size="5"
        ),
        rx.heading("¿Cómo se instala?", size="7", padding_top="2em"),
        rx.text(
            "1. Instala Reflex con: pip install reflex\n"
            "2. Inicializa un nuevo proyecto con: reflex init\n"
            "3. Ejecuta tu app con: reflex run",
            size="5"
        ),
        rx.heading("Ejemplo básico", size="7", padding_top="2em"),
        rx.text(
            "Un contador simple en Reflex:\n\n"
            "class State(rx.State):\n"
            "    count: int = 0\n\n"
            "    def increment(self):\n"
            "        self.count += 1\n\n"
            "def index():\n"
            "    return rx.vstack(\n"
            "        rx.text(f\"Contador: {State.count}\"),\n"
            "        rx.button(\"Incrementar\", on_click=State.increment),\n"
            "    )",
            size="5",
            font_family="monospace",
        ),
        padding="2em"
    )

app = rx.App()
app.add_page(index, title="Reflex Teoría", description="Teoría básica sobre Reflex")
