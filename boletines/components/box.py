import reflex as rx


def box(lt: str) -> rx.Component:
    return rx.button(
        rx.vstack(
            rx.image(src="folder.png", width="50px", height="auto", alt="a folder image"),
            rx.vstack(
                rx.text(lt)
            )
        ),
        variant="outline",
        bg="white",
        padding=10,
        margin="1em",
        on_click=rx.redirect("https://www.google.com", external=True)
        # link_button(lt, "hola"), bg="blue", color="white", margin="2em", padding=10
    )
