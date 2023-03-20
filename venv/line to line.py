import tkinter as tk
import random
import time
import pyautogui
import csv
from nltk.corpus import  words
import json


def save_element_positions_to_csv(list_of_Element_position, Samples_number):
    # Define the output file path
    output_file_path = f"C:\\Users\\abulabn\\Desktop\\Test\\{Samples_number}.csv"

    # Save the list of element positions to a CSV file
    with open(output_file_path, "w") as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Element', 'x1', 'y1', 'x2', 'y2', 'String', 'Checked/Unchecked'])
        for i in range(len(list_of_Element_position)):
            if len(list_of_Element_position[i]) == 3:
                csv_out.writerow([list_of_Element_position[i][0], list_of_Element_position[i][1][0]-calculate_shift(root)[0], list_of_Element_position[i][2][0]-calculate_shift(root)[0], list_of_Element_position[i][1][1]-calculate_shift(root)[0], list_of_Element_position[i][2][1]-calculate_shift(root)[1]])
            elif len(list_of_Element_position[i]) == 4:
                csv_out.writerow([list_of_Element_position[i][0], list_of_Element_position[i][1][0], list_of_Element_position[i][2][0], list_of_Element_position[i][1][1], list_of_Element_position[i][2][1], list_of_Element_position[i][3]])
            elif len(list_of_Element_position[i]) == 5:
                csv_out.writerow([list_of_Element_position[i][0], list_of_Element_position[i][1][0], list_of_Element_position[i][2][0], list_of_Element_position[i][1][1], list_of_Element_position[i][2][1], list_of_Element_position[i][3], list_of_Element_position[i][4]])

    return output_file_path
class Coordinates:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "x2": self.x2,
            "y2": self.y2,
        }
class Font:
    def __init__(self, size='', style='', color='', weight=''):
        self.size = size
        self.style = style
        self.color = color
        self.weight = weight
    def to_dict(self):
        return {
            "size": self.size,
            "style": self.style,
            "color": self.color,
            "weight": self.weight
        }
class annotations:
    def __init__(self, Type, coordinates, text, font, checked):
        self.Type = Type
        self.coordinates = coordinates
        self.text = text
        self.font = font
        self.checked = checked
    def to_dict(self):
        return {
            "Type": self.Type,
            "coordinates": self.coordinates.to_dict(),
            "text": self.text,
            "font": self.font.to_dict(),
            "checked": self.checked
                }
def generate_json(list_of_elements, filename, Sample_number):
    """
    Generates a JSON object from a list of elements and writes it to a file.
    Each element in the list should be in the format (label, (x, y), (x2, y2), text, checked, font)

    :param list_of_elements: list, elements to convert to JSON
    :param filename: string, the name of the file to write the JSON to
    :return: None
    """
    image_dict = {"image": Sample_number, "annotations": []}
    for element in list_of_elements:
        Type_Element = element[0]
        x, y = element[1]
        x2, y2 = element[2]
        coord_text = element[3] if len(element) > 3 else ''
        coord_checked = element[4] if len(element) > 4 else ''
        font_style,font_size,font_color,font_weight = element[5] if len(element) > 5 else ''
        coord = Coordinates(x, y, x2, y2)
        font = Font(font_style, font_size, font_color, font_weight)

        # Annotations =annotations(Type_Element, coord, font, coord_text, coord_checked)
        label_dict = annotations(Type_Element, coord, coord_text, font,coord_checked).to_dict()

        image_dict["annotations"].append(label_dict)

    with open(filename, 'w') as outfile:
        json.dump(image_dict, outfile, indent=4)

    print(f"JSON object successfully written to {filename}")
class RandomFont:
    def __init__(self):
        pass

    def font_style(self):
        # Generate random font style
        font_style = random.choice(["Arial", "Courier", "Helvetica", "courier 9", "courier 10"])
        return font_style

    def font_size(self):
        # Generate random font size
        font_size = random.randint(6, 10)
        return font_size

    def font_color(self):
        # Generate random font color
        font_color = random.choice(["black", "red", "green", "blue", "orange", "purple", "brown", "grey"])
        return font_color

    def font_weight(self):
        # Generate random font weight
        font_weight = random.choice(["normal", "bold"])
        return font_weight


    def random_font(self):
        # Generate random font
        font = (self.font_style(), self.font_size(), self.font_weight(), self.font_color())
        return font


class RandomTextGenerator:
    def __init__(self):
        self.word_list = words.words()
        self.chars = "abcdefghijklmnopqrstuvwxyz1234567890+-*/:;.,!@#$%^&*()"

    def random_sentence(self, n):
        sentence = ""
        for i in range(0, n):
            sentence += random.choice(self.word_list) + " "
        return sentence.strip()

    def random_string(self, n):
        String = ""
        for c in range(n):
            String += random.choice(self.chars)
        return String

    def generate(self,n):
        if random.random() < 0.8:
            return self.random_sentence(random.randint(1, n))
        else:
            return self.random_string(random.randint(10, 20))


def get_element_position(element):
    # Get the element position
    element_position = element.winfo_geometry().split("+")
    element_position[0] = element_position[0].split("x")
    element_position[1] = int(element_position[1])
    element_position[2] = int(element_position[2])

    return element_position

def random_size():
    # Generate random button sizes
    width = random.randint(5, 20)
    height = random.randint(1, 4)
    return (width, height)
def take_screenshot(path, region, filename, sample_number):
    # Take the screenshot
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot with sample number
    screenshot.save(path + filename + str(sample_number) + ".png")
Samples_number = 0
# a funktion that looking for the max heingt of the buttons
def max_height( height_list):
    max_height = 0
    #loop to find the max heinght
    for i in range(len(height_list)):
        if height_list[i] > max_height:
            max_height = height_list[i]
    return max_height
height_list = []
def list_height( height):

    height_list.append(height)
    return height_list
#function to create buttons
def create_buttons(num_rows, num_cols, screen_width, screen_height, list_of_element_positions, root, max_hight_value,max_width_value,horizental_distance,vertical_distance):
    """
       Creates a button with a random font and size, and adds its position to the list_of_element_positions.
       The position is based on the maximum height and width values of the elements already in the row and column.
    """
    btn = tk.Button(root)

    # config the font of the button
    rf = RandomFont()
    font = rf.random_font()
    generator = RandomTextGenerator()

    btn.config(font=(font[0:2]), fg=font[3])
    # Place button on the window line by line
    #if the max value is smaller than 10 than x position ,still the same els than replace the x position
    if max_height_value < screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        btn.place(x=screen_width / horizental_distance * j, y=screen_height / vertical_distance * i)
    elif max_height_value > screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        btn.place(x=screen_width / horizental_distance * j, y=max_height_value)
    elif max_height_value < screen_height / vertical_distance * i and max_width_value > screen_width / horizental_distance * j:
        btn.place(x=max_width_value, y=screen_height / vertical_distance * i)
    else:
        btn.place(x=max_width_value, y=max_height_value)
    # Set button size randomly
    #to make button with random size biger than text in it we need to make the button bigger than the text how ?
    #we need to make the button bigger than the text and the text bigger than the button


    btn.config(text=generator.generate(1))
    btn.config(width=random_size()[0], height=random_size()[1])
    #config the text of the button

    # Update the window
    root.update()
    time.sleep(0.1)


    # Get button position coordinates
    widget_x1, widget_y1 = btn.winfo_rootx(), btn.winfo_rooty()
    widget_x2, widget_y2 = widget_x1 + btn.winfo_width(), widget_y1 + btn.winfo_height()
    button_position = ("Button " + str(i) + "_" + str(j), (widget_x1, widget_x2), (widget_y1, widget_y2))
    # Set button font randomly


    list_of_element_positions.append(button_position)
    # Return the list of button positions
    return list_of_element_positions
#function to create labels
def create_labels(num_rows, num_cols, screen_width, screen_height, list_of_element_positions, root,max_hight_value,max_width_value,horizental_distance,vertical_distance):
    lbl = tk.Label(root)
    # Place button on the window line by line

    if max_height_value < screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        lbl.place(x=screen_width / horizental_distance * j, y=screen_height / vertical_distance * i)
    elif max_height_value > screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        lbl.place(x=screen_width / horizental_distance * j, y=max_height_value)
    elif max_height_value < screen_height / vertical_distance * i and max_width_value > screen_width / horizental_distance * j:
        lbl.place(x=max_width_value, y=screen_height / vertical_distance * i)
    else:
        lbl.place(x=max_width_value, y=max_height_value)
    # config the font of the button
    rf = RandomFont()
    font = rf.random_font()
    lbl.config(font=(font[0:2]), fg=font[3])

    # Set button size randomly
    random_word_number =random.randint(1, 4)

    generator = RandomTextGenerator()
    lbl.config(text=generator.generate(5))
    # lbl.config(width=random_size()[0], height=random_size()[1])

    # Configure the font of the Label widget using random_font() function
    # lbl.configure(font=random_font(root))
    root.update()
    time.sleep(0.1)
    # Get button position coordinates
    widget_x1, widget_y1 = lbl.winfo_rootx(), lbl.winfo_rooty()
    widget_x2, widget_y2 = widget_x1 + lbl.winfo_width(), widget_y1 + lbl.winfo_height()
    label_position = ("Label " + str(i) + "_" + str(j), (widget_x1, widget_x2), (widget_y1, widget_y2))
    list_of_element_positions.append(label_position)
    # Return the list of button positions
    return list_of_element_positions
#function to create radiobuttons
def create_radiobuttons(num_rows, num_cols, screen_width, screen_height, list_of_element_positions, root,max_hight_value,max_width_value,horizental_distance,vertical_distance):
    rad = tk.Radiobutton(root)
    # Place radiobutton on the window line by line

    # Set radiobutton size randomly
    rad.config(width=random_size()[0], height=random_size()[1])
    if max_height_value < screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        rad.place(x=screen_width / horizental_distance * j, y=screen_height / vertical_distance * i)
    elif max_height_value > screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        rad.place(x=screen_width / horizental_distance * j, y=max_height_value)
    elif max_height_value < screen_height / vertical_distance * i and max_width_value > screen_width / horizental_distance * j:
        rad.place(x=max_width_value, y=screen_height / vertical_distance * i)
    else:
        rad.place(x=max_width_value, y=max_height_value)
    # Configure the font of the Radiobutton widget using random_font() function
    rf = RandomFont()
    font = rf.random_font()
    rad.config(font=(font[0:2]), fg=font[3])
    generator = RandomTextGenerator()

    rad.configure(text=generator.generate(1))
    root.update()
    time.sleep(0.1)

    # Get radiobutton position coordinates
    widget_x1, widget_y1 = rad.winfo_rootx(), rad.winfo_rooty()
    widget_x2, widget_y2 = widget_x1 + rad.winfo_width(), widget_y1 + rad.winfo_height()
    radiobutton_position = ("Radiobutton " + str(i) + "_" + str(j), (widget_x1, widget_x2), (widget_y1, widget_y2))
    list_of_element_positions.append(radiobutton_position)
    # Return the list of radiobutton positions
    return list_of_element_positions
#function to create checkbuttons
def create_checkbuttons(num_rows, num_cols, screen_width, screen_height, list_of_element_positions, root,max_hight_value,max_width_value,horizental_distance,vertical_distance):
    chk = tk.Checkbutton(root, text='check')

    # Place checkbutton on the window line by line
    if max_height_value < screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        chk.place(x=screen_width / horizental_distance * j, y=screen_height / vertical_distance * i)
    elif max_height_value > screen_height / vertical_distance * i and max_width_value < screen_width / horizental_distance * j:
        chk.place(x=screen_width / horizental_distance * j, y=max_height_value)
    elif max_height_value < screen_height / vertical_distance * i and max_width_value > screen_width / horizental_distance * j:
        chk.place(x=max_width_value, y=screen_height / vertical_distance * i)
    else:
        chk.place(x=max_width_value, y=max_height_value)
    # Set checkbutton size randomly
    # Configure the font of the Checkbutton widget using random_font() function
    rf = RandomFont()
    font = rf.random_font()
    chk.config(font=(font[0:2]), fg=font[3])
    generator = RandomTextGenerator()
    chk.configure(text=generator.generate(1))
    root.update()
    time.sleep(0.1)
    # Get checkbutton position coordinates
    widget_x1, widget_y1 = chk.winfo_rootx(), chk.winfo_rooty()
    widget_x2, widget_y2 = widget_x1 + chk.winfo_width(), widget_y1 + chk.winfo_height()
    checkbutton_position = ("Checkbutton " + str(i) + "_" + str(j), (widget_x1, widget_x2), (widget_y1, widget_y2))
    list_of_element_positions.append(checkbutton_position)
    # Return the list of checkbutton positions
    return list_of_element_positions

#function to calculate the shift in x and y direction
def calculate_shift(root):
    lbl = tk.Label(root, text="")
    # Place button on the window line by line
    lbl.place(x=0, y=0)
    # Set button size randomly
    lbl.config(width=0, height=0)
    root.update()
    time.sleep(0.01)
    #get the zero position of the window

    widget_x1, widget_y1 = lbl.winfo_rootx(), lbl.winfo_rooty()

    return widget_x1, widget_y1
    
#list to height of one row

#loop to create 5 samples
while Samples_number < 5:

    root = tk.Tk()
    n = random.randint(5, 10)
    root.update()
    list_of_Element_position = []

    # Get the current screen width and height
    step = 1
    random_number = random.uniform(1, 3)
    screen_width = int (root.winfo_screenwidth()/round(random_number / step) )
    screen_height = int (root.winfo_screenheight()/round(random_number / step) )

    # make the window fullscreen
    root.attributes('-fullscreen', True)
    root.update()

    # Define the region of the screen to capture
    x, y = root.winfo_x(), root.winfo_y()
    screen_width, screen_height = root.winfo_width(), root.winfo_height()
    region = (x, y, screen_width,  screen_height)
    max_height = 0
    Rows_number = 5
    Columns_number = 5
    max_height_value=0
    max_width_value=0
    disatnince_between_elements_horizontal =10
    disatnince_between_elements_vertical =10
    for i in range(Rows_number):
        #find the maximum height of the elements in the line

        max_height = Columns_number * i

        list_of_row_height = []
        list_of_column_width = []
        max_width_value = 0

        max_width = 0
        for j in range(Columns_number):
            x=random.randint(0, 3)
            if x == 0:
                 create_buttons(i, j, screen_width, screen_height, list_of_Element_position, root,max_height_value,max_width_value,disatnince_between_elements_vertical,disatnince_between_elements_horizontal)
            elif x == 1:
                create_labels(i, j, screen_width, screen_height, list_of_Element_position, root,max_height_value,max_width_value,disatnince_between_elements_vertical,disatnince_between_elements_horizontal)
            elif x == 2:
                create_radiobuttons(i, j, screen_width, screen_height, list_of_Element_position, root,max_height_value,max_width_value,disatnince_between_elements_vertical,disatnince_between_elements_horizontal)
            elif x == 3:
                create_checkbuttons(i, j, screen_width, screen_height, list_of_Element_position, root,max_height_value,max_width_value,disatnince_between_elements_vertical,disatnince_between_elements_horizontal)
            #find the maximum height of the elements in the line
            
            list_of_row_height.append(list_of_Element_position[max_height][2][1])
            list_of_Element_position
            list_of_column_width.append(list_of_Element_position[max_height][1][1])
            # max_width = max_width + 1
            max_width_value = max(list_of_column_width)
            max_height= max_height + 1
        max_height_value =  max(list_of_row_height)
        max_width_value = max(list_of_column_width)


    path = "C:\\Users\\abulabn\\Desktop\\Test\\"
    filename = "screenshot_region_"
    take_screenshot(path,region, filename, Samples_number)
    # #         file.writelines(" ".join(["the number of the iteration is ", str(Samples_number), str(list_of_Element_position)]) + "\n")

    save_element_positions_to_csv(list_of_Element_position, Samples_number)
    Samples_number = Samples_number + 1
    # destroy the gui
    print(list_of_Element_position)
    root.destroy()

    root.mainloop()



