import reflex as rx
from boletines.components.link_button import link_button

import os

directory = os.listdir(".")

def list_files() -> rx.Component:
    return rx.box(rx.text(len(directory)))


def boxes(lt: str):
    return rx.square(
        link_button(lt, "hola"),
        bg="blue",
        color="white",
        margin="2em",
        padding=10
    )


def index2():
    return rx.responsive_grid(
        rx.foreach(directory, boxes),
        columns=[2, 4, 6],
    )
