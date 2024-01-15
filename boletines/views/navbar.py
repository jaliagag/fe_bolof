import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
        ),
        position="sticky",
        width="100%",
        top="0px",
        z_index="999",
        bg="lightgray"
    )