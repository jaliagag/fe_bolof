"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from boletines.views.navbar import navbar
from boletines.views.menu import menu
from boletines.views.body import body
from boletines.components.list_files import list_files, index2


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            #menu(),
            rx.center(
                rx.vstack(
                    #body(),
                    #list_files(),
                    index2(),
                    width="100%"
                ),
                bg="black"

            )
        ),
        bg="black",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
