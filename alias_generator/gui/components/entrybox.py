from tkinter import Entry, Label

from ..theme import THEME_BACKGROUND_COLOR, THEME_FONT_FACE, THEME_FOREGROUND_COLOR


class EntryBox:

    label: Label
    entry: Entry

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

        self.entry = Entry(
            foreground=THEME_FOREGROUND_COLOR,
            background=THEME_BACKGROUND_COLOR,
            highlightbackground="gray",
            highlightthickness=0,
            font=(THEME_FONT_FACE, 14, "normal"),
            width=25,
            takefocus=True,
        )

        self.entry.grid(row=row, column=column + 1, pady=5)

    def set_focus(self):
        self.entry.focus_set()

    def get_text(self):
        return self.entry.get()
