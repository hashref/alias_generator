from tkinter import Canvas, PhotoImage

from ..theme import THEME_BACKGROUND_COLOR


class Logo:
    canvas: Canvas
    image: PhotoImage

    def __init__(self) -> None:
        canvas = Canvas(
            background=THEME_BACKGROUND_COLOR,
            width=105,
            height=105,
            borderwidth=0,
            highlightthickness=0,
        )

        image = PhotoImage(file="alias_generator/assets/mb_alias_image_100_100.png")
        canvas.create_image(55, 55, image=image)

        canvas.grid(row=0, column=0, columnspan=2, pady=20)

        self.image = image
        self.canvas = canvas
