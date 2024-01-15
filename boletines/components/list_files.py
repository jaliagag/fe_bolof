import reflex as rx

import os

def listme(list: list):
    for i in list:
        return i

directory = os.listdir(".")

def list_files() -> rx.Component:
    return rx.box(
        rx.text(directory)

    )

#print(directory)