import reflex as rx
from typing import List

import os


def listme(list: list):
    for i in list:
        return i


directory = os.listdir(".")

# The rx.foreach component takes an iterable(list, tuple or dict) and a
# function that renders each item in the list.


def list_files() -> rx.Component:
    return rx.box(rx.text(len(directory)))


# print(directory)


def boxes(lt: str):
    return rx.square(
        lt,
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
