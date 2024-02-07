"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import os 
import reflex as rx
from boletines.views.navbar import navbar
from boletines.views.body import body
from boletines.views.output import output
from boletines.tests import test1

current = os.getcwd()
ls = os.listdir("assets")

#@rx.page(
#    title="Boletines Oficiales - ARG",
#    description="A beautiful app built with Reflex",
#    image="escudo.png"
#    #meta=meta
#)



class State(rx.State):
    """The app state."""
    #rx.var()
    #def bole_date(self) -> str:
    #    args = self.router.page.params
    #    date = args.get('date', [])
    #    #return f"Archivos de {", ".join(date)}"
    
    pass

@rx.page(title="Boletines Oficiales - ARG")
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.center(
                rx.vstack(
                    body(),
                    width="100%"
                ),
                bg="black"

            )
        ),
        output(current),
        output(ls),
        bg="black",
    )

@rx.page(title="Boletines Oficiales - ARG")
def test() -> rx.Component:
    return rx.text(
        "testing grounds biotch",
        test1.but()
    )

# Add state and page to the app.
app = rx.App()
#app.add_page(index)
