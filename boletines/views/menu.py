import reflex as rx

def menu() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Sidebar",
                text_align="center",
                margin_bottom="1em",
            ),
            width="250px",
            padding_x="2em",
            padding_y="1em",
        ),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="500",
        padding_y="5em",
        bg="lightgray"
    )