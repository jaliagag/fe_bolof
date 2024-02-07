import reflex as rx

class TestingGround (rx.State):
    text: str = "Holanda"
    
    def view_method(self):
        current_page_route = self.router.page.path
        current_page_url = self.router.page.raw_path
        print(current_page_route)
        print(current_page_url)


    @rx.var
    def show_me(self) -> str:
        return self.text.upper()

def but() -> rx.Component:
    return rx.text(
        TestingGround.view_method()
    )