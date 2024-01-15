"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from boletines.views.navbar import navbar
from boletines.views.menu import menu
from boletines.views.body import body
from boletines.components.list_files import list_files


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.center(
                menu(),
                body(),

            )
        )
        #rx.center(
        #    #menu(),
        #    rx.vstack(
        #        body(),
        #        list_files(),
        #        max_width="1200px",
        #        width="100%",
        #        margin_y="1em",

        #    )

        #)
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
