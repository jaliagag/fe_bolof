import reflex as rx
from boletines.components.box import box
import os

directory = os.listdir(".")

def body():
    return rx.responsive_grid(
        rx.foreach(directory, box),
        columns=[2, 4, 6],
    )