# colour_text.py
# Library test.
#
# 2024 (C) DAREKPAGES
# Python 3.11.10

from sys import path
path.append(r'ctx.py')
import ctx

gph= [" ,-------------, ", " | ####  ####  | ", " | #   # #   # | ", " | #   # ####  | ", 
      " | #   # #     | ", " | ####  #     | ", " '-------------' "]

print('')
for i in range(0, 7):
    print(ctx.ft_bold_white+ctx.bg_cyan, gph[i], ctx.clr)