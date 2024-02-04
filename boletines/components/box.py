import reflex as rx
from boletines.components.link_button import link_button

def box(lt: str):
    return rx.square(
        link_button(lt, "hola"),
        bg="blue",
        color="white",
        margin="2em",
        padding=10
    )