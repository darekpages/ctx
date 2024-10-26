# ctx
## Adding colors to texts in the command line
When creating scripts that can only have a text interface (in the *command line*), sometimes there is a need to highlight the text with a color or even a colored background.

The color of the text can be changed by adding the appropriate *ANSI* code to the text, which will be interpreted by the `print()` function as a color change. 
Although this is a simple process, there is then a problem with the readability of such code, which in effect slows down coding or possible changes in the code.



Wondering how to simplify it, I created a library that simplified adding color to text. I wanted to be able to **add color names**. The library is small and does not 
need any additional libraries.

The use is simple:

`print(text_color, background_color, text, ...)`



Installation:
Insert the library into the shared directory of the python libraries, or simply into the directory where the script is located.
