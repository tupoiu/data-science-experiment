import tkinter as tk
from math import floor, sin, cos, sqrt
import time


def to_hexadecimal(color: list) -> str:
    out = "#"
    out += hex(color[0])[2:] if len(hex(color[0])) == 4 else f"0{hex(color[0])[2:]}"
    out += hex(color[1])[2:] if len(hex(color[1])) == 4 else f"0{hex(color[1])[2:]}"
    out += hex(color[2])[2:] if len(hex(color[2])) == 4 else f"0{hex(color[2])[2:]}"
    return out
# print(to_hexadecimal([255,100,255]))


def fmt(x: float) -> int:
    return floor(x) % 256


def fmt_c(col: list) -> list:
    return [fmt(col[0]), fmt(col[1]), fmt(col[2])]


def rotate2(col: list, a: float):
    return [
        col[0]*cos(a) - col[1]*sin(a),
        col[0]*sin(a) + col[1]*cos(a),
        col[2]
    ]


def lerp(col: list, rg=1., gb=1., rb=1.):
    total = rg + gb + rb
    rg /= total
    gb /= total
    rb /= total
    return [
        (1 - rg - rb) * col[0] + rg * col[1] + rb * col[2],
        (1 - gb - rg) * col[1] + rg * col[0] + gb * col[2],
        (1 - gb - rb) * col[2] + gb * col[1] + rb * col[0]
    ]


root = tk.Tk()
height = 400
width = 800
l = 4

pixels = []

canvas = tk.Canvas(root, bg="white", height=height, width=width)
for i in range(floor(width/l)):
    for j in range(floor(height/l)):
        # color = [
        #     fmt(-i*j+2*i*i+j*j*j),
        #     fmt(255*sin(sqrt(10*i+j)/4) + 1000*sin(sqrt(7*i+j)/4)),
        #     fmt(255 * sin(sqrt(10 * i + j) / 4) + 500 * sin(sqrt(7 * i + j) / 4))
        # ]

        # color = [ # Cascade
        #     100+100*cos(i-sqrt(100*j)),
        #     100+100*sin(i+sqrt(100*j)),
        #     100+100*sin(i),
        # ]

        # color = [ # Wave
        #     100 + 100 * cos(j + 5*cos(i)),
        #     100 + 100 * cos(j/2 + 5*cos(i)),
        #     100 + 100 * cos(j/4 + 5*cos(i)),
        # ]
        # color = lerp(color, 10/(j+1), 0, 10*(1+sin(i/10)))

        # color = [ # Hypnosis
        #     100 + 100 * cos(i-j/2 + 10 * cos(j/6)) + 25 + 25 * cos(i/2 + 10 * cos(j/6)),
        #     0,
        #     100 + 100 * cos(i-j + 10 * cos(j/6)) + 25 + 25 * cos(i/3 + 10 * cos(j/6)),
        # ]

        # color = [ # Slices
        #     50 + 50*cos(i - j + 10*cos(0.1 + j/6)),
        #     50 + 50 * cos(i - j / 2 + 10 * cos(j / 6)) + 25 + 25 * cos(i / 2 + 10 * cos(j / 6)),
        #     25 + 25 * cos(i - j + 10 * cos(j / 6)) + 25 + 25 * cos(i / 3 + 10 * cos(j / 6)),
        # ]
        # if i+j/2 > width/(4*l):
        #     color = [color[1], color[0], color[2]]
        # if i+j/2 > 1.5*width/(4*l):
        #     color = [color[2], color[1], color[0]]
        # if i-j > 4*height/(4*l):
        #     color = [color[0], color[1], color[1]]
        # if j > height/(2*l):
        #     color = [200, color[2], 100]

        color = [  # Wave
            0,
            (i*i*i - 5*j - 5*i) % 256,
            (i*i*i - 2*j) % 256,
        ]
        if i < width/(4*l):
            color = [200, color[2], 100]
        else:
            color = [0.5*color[1], 0.5*color[1], 0.3*color[1]+0.2*color[2]]

        color = fmt_c(color)
        canvas.create_rectangle(i*l, j*l, i*l+l, j*l+l, fill=to_hexadecimal(color), outline="")

canvas.pack()
root.update()
root.mainloop()