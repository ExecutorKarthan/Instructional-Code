#raw_input = input("Give me a color? \n")
#processed_input = raw_input.lower()
raw_color_list = "yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white"
reference_colors = []
start_cut = 0
stop_cut = raw_color_list.index(",")
for index in range(0, len(raw_color_list)):
    reference_colors.append(raw_color_list[start_cut:stop_cut])
    start_cut = stop_cut+2
    stop_cut = raw_color_list.index(",", start_cut)
real_color = False
for ref in reference_colors:
    if(processed_input == ref):
        print("Color is real and part of module")
        real_color = True
        break
if(real_color == False):
    print("Color is not supported")

