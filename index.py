"""  ."""

import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Pagina de Bienvenida!", size="9"),
            rx.text(
                "Empieza editando  ",
                size="5",
            ),
            rx.link(
                rx.button("HazClic"),
                href="https://www.facebook.com//",
                is_external=True,
            ),
            spacing="3",
            justify="center",
            min_height="95vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)

