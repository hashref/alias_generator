from tkinter import Button, Tk
import string
import random
from email_validator import validate_email, EmailNotValidError

from gui.components import TextBox, Logo, EntryBox
from gui.theme import THEME_BACKGROUND_COLOR

ALLOWED_CHARS = string.ascii_letters + string.digits
ALIAS_SIZE = 7


class GUI:
    window: Tk
    logo: Logo
    entrybox: EntryBox
    resultbox: TextBox
    button: Button

    def __init__(self) -> None:
        window = Tk()
        window.config(padx=50, background=THEME_BACKGROUND_COLOR)
        window.title("Alias Generator")

        self.logo = Logo()
        self.entrybox = EntryBox(label_text="Email:", row=1, column=0)
        self.entrybox.set_focus()
        self.resultbox = TextBox(label_text="Alias:", row=2, column=0)

        button = Button(
            text="Generate",
            borderwidth=0,
            highlightbackground=THEME_BACKGROUND_COLOR,
            command=self.button_handler,
            width=15,
        )
        button.grid(row=4, column=0, columnspan=2, pady=15)
        window.bind("<Return>", self.button_handler)
        self.button = button

        self.window = window

        window.mainloop()

    def button_handler(self, event=None) -> None:
        email = self.entrybox.get_text()
        try:
            validate_email(email)
        except EmailNotValidError:
            self.resultbox.update_text("Invalid Email Address!!")
        else:
            alias = "".join(random.choice(ALLOWED_CHARS) for _ in range(ALIAS_SIZE))
            email_parts = email.split("@")
            aliased_email = f"{email_parts[0]}+{alias}@{email_parts[1]}"
            self.resultbox.update_text(aliased_email)
            self.window.clipboard_clear()
            self.window.clipboard_append(aliased_email)
