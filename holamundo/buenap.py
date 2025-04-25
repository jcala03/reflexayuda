import reflex as rx

class FlaskInfo(rx.Component):
    def __init__(self):
        super().__init__()
        self.info = {
            'titulo': 'Información Básica sobre Flask',
            'descripcion': 'Flask es un microframework web para Python, minimalista y flexible.',
            'caracteristicas': [
                'Ligero y fácil de aprender',
                'Sistema de routing simple',
                'Motor de plantillas Jinja2',
                'Extensible con complementos'
            ],
            'enlace': 'https://flask.palletsprojects.com/'
        }

    def render(self):
        return rx.box(
            # Icono de Flask
            rx.image(
                src="/api/placeholder/100/100",  # Reemplazado con imagen de placeholder
                alt="Logo de Flask",
                width="100px",
                height="100px",
                display="block",
                margin="0 auto"
            ),
            
            rx.heading(self.info['titulo'], size="xl"),
            rx.text(self.info['descripcion']),
            
            rx.box(
                rx.heading("Características principales:", size="lg"),
                rx.list(
                    *[rx.list_item(item) for item in self.info['caracteristicas']],
                    spacing=".5em"
                ),
                bg="#f8f9fa",  # Cambiado background_color por bg
                padding="20px",
                border_radius="8px",
                margin_top="20px",
                box_shadow="0 2px 4px rgba(0,0,0,0.1)"
            ),
            
            rx.flex(
                rx.text("Para más información visita la "),
                rx.link(
                    "documentación oficial",
                    href=self.info['enlace'],
                    color="blue"
                ),
                rx.text("."),
                gap="1",  # Espacio entre elementos
            ),
            
            font_family="Arial, sans-serif",
            max_width="800px",
            margin="0 auto",
            padding="20px",
            line_height="1.6"
        )

# Crear y ejecutar la aplicación
app = rx.App()
app.add_page(FlaskInfo)  # No es necesario especificar route="/" ya que es la ruta por defecto
app.compile()