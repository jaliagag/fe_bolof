import reflex as rx


def link_button(date: str, q_items: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.vstack(
                rx.image(src="folder.png", width="50px", height="auto",alt="a folder image"),
                rx.vstack(
                    rx.text(date, color="white"),
                    rx.text(q_items, color="white"),
                    align_items="center",
                ),
            ),
        ),
    )
