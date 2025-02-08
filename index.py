"""Welcome to Reflex! This file outlines the steps to create a basic app."""

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
            rx.heading("Bienvenido  a Reflex Con Mouredev!", size="9"),
            rx.text(
                "Get started by editing  -  Empieza editando  ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!  Chequea nuestros docuentos"),
                href="https://reflex.dev/docs/getting-started/introduction/",
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

