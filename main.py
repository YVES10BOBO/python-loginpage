from flet import (
    Page, TextField, Checkbox, ElevatedButton, Row, Column, Text, MainAxisAlignment, TextAlign, ControlEvent, app,
    ThemeMode
)

def main(page: Page) -> None:
    page.title = 'Signup'
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # Setup our fields
    text_username = TextField(label="Username", text_align=TextAlign.LEFT, width=200)
    text_password = TextField(label="Password", text_align=TextAlign.LEFT, width=200, password=True)
    checkbox_signup = Checkbox(label='I agree to the terms and conditions', value=False)
    button_submit = ElevatedButton(text="Sign Up", width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(e: ControlEvent) -> None:
        print("Username:", text_username.value)
        print("Password:", text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome, {text_username.value}!', size=20)],
                alignment=MainAxisAlignment.CENTER
            )
        )

    # Link the functions to our UI components
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the page - Sign Up
    page.add(
        Row(
            controls=[
                Column(
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ],
            alignment=MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    app(target=main)

