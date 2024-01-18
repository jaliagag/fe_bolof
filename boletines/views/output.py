import reflex as rx


def output(sometext: str) -> rx.Component:
    return rx.text(sometext, color="white")
