# ctx
## Adding colors to texts in the command line
When creating scripts that can only have a text interface (in the *command line*), sometimes there is a need to highlight the text with a color or even a colored background.

The color of the text can be changed by adding the appropriate *ANSI* code to the text, which will be interpreted by the `print()` function as a color change. 
Although this is a simple process, there is then a problem with the readability of such code, which in effect slows down coding or possible changes in the code.

![code exam](https://github.com/user-attachments/assets/98be3ae1-657f-4714-bbf1-0616056f552e)

Wondering how to simplify it, I created a library that simplified adding color to text. I wanted to be able to **add color names**. For example:

`print(COLOR_TEXT, COLOR_BACKGROUND, any_text, ...)`

![efekt 1](https://github.com/user-attachments/assets/e33b83d2-ac33-44cb-b636-6114f7c07bf4)

The library is small and does not need any additional libraries.


The use is simple:

`print(text_color, background_color, text, ...)`

Installation:
Insert the library ***ctx.py*** into the shared directory of the python libraries, or simply into the directory where the script is located.
