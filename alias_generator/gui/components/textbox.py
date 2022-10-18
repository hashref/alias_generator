from tkinter import Label

from ..theme import THEME_BACKGROUND_COLOR, THEME_FONT_FACE, THEME_FOREGROUND_COLOR


class TextBox:

    label: Label
    text: Label

    def __init__(
        self,
        label_text: str,
        row: int,
        column: int,
    ) -> None:

        self.label = Label(
            text=label_text,
            foreground=THEME_FOREGROUND_COLOR,
            background=THEME_BACKGROUND_COLOR,
            font=(THEME_FONT_FACE, 14, "bold"),
            padx=10,
        )
        self.label.grid(row=row, column=column)

        self.text = Label(
            text="Results Here",
            foreground=THEME_FOREGROUND_COLOR,
            background=THEME_BACKGROUND_COLOR,
            font=(THEME_FONT_FACE, 14, "normal"),
            width=25,
            anchor="w",
        )

        self.text.grid(row=row, column=column + 1, pady=5)

    def update_text(self, text: str) -> None:
        self.text.config(text=text)
