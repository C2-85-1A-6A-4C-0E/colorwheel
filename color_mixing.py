import colorsys

primaries = red, green, blue = (255,0,0), (0,255,0), (0,0,255)
magenta, cyan, yellow = (255,0,255), (0,255,255), (255,255,0)

colors = red, magenta, blue, cyan, green, yellow
names  = "red", "magenta", "blue", "cyan", "green", "yellow"
def add_colors(a, b, weight=0.5):
    x = colorsys.rgb_to_hsv(*a)
    y = colorsys.rgb_to_hsv(*b)

    s = x[1]*weight + y[1]*(1-weight)
    v = x[2]*weight + y[2]*(1-weight)

    h1, h2 = min(x[0], y[0]), max(x[0], y[0])
    if h2 - h1 > 0.5:
        h1 += 1
        dif = abs(h1 - h2)
        dif *= weight
        h = min(h1, h2) + dif
    else:
        dif = abs(h1 - h2)
        dif *= weight
        h = h1 + dif
    while h > 1:
        h -= 1
    color = colorsys.hsv_to_rgb(h, s, v)
    return color

if __name__ == "__main__":
    for color, next_color, name, next_name in zip(colors, colors[1:], names, names[1:]):
        print(f"{name} and {next_name} add to {add_colors(color, next_color)}")