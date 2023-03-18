import random
import time
import tkinter
import pyautogui
from nltk.corpus import  words
import csv

# root = tkinter.Tk()
# n = random.randint(5, 10)
# root.geometry("1700x1000")
# # set the Gui maximized
# root.state('zoomed')
def bulid_window():
    root = tkinter.Tk()
    n = random.randint(5, 10)
    root.geometry("1700x1000")
    # set the Gui maximized
    root.state('zoomed')


# ####################################################################################################
### description: this function generates a non-repeating random number to be used later for positioning elements
### parameter:
### rval: None
####################################################################################################
def Random_Positions():
  randomlist = []
  for i in range(0, 1400):
    o = random.randrange(0, 1000, 2)
    if o not in randomlist:
      randomlist.append(o)
  return randomlist
def Random_Positions_x():
  randomlist = []
  for i in range(0, 1400):
    o = random.randrange(0, 1700, 2)
    if o not in randomlist:
      randomlist.append(o)
  return randomlist
word_list = words.words()
# a function random_sentence to create a random sentence
def random_sentence(n):
    sentence = ""
    for i in range(0, n):
        sentence += random.choice(word_list) + " "
    return sentence

def in_interval(x, interval):
    return interval[0] <= x <= interval[1]

def pixel_of_height(n):
    return 1 * n

def pixel_of_width(n):
    return 1 * n
# a function to create a random string
def random_string(n):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890+-*/:;.,!@#$%^&*()"
    String = ""
    for c in range(n):
        String += random.choice(chars)
    return String
# a function to create a random choice of two options (True or False) with a probability of 80% for True
def random_choice_80():
    choice = random.choices([True, False], weights=[80, 20], k=1)
    return choice[0]
def random_choice_50():
    choice = random.choices([True, False], weights=[50, 50], k=1)
    return choice[0]
def take_screenshot(path, region, filename, sample_number):
    # Take the screenshot
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot with sample number
    screenshot.save(path + filename + str(sample_number) + ".png")
list_of_Element_position = []

#a function to change the font style of the text
list_of_Font = ["Arial",  "Courier",  "Helvetica",  "courier 9","courier 10"]

def random_font_style(Button, Label ,Text, Checkbutton, Radiobutton):
    if random_choice_50() == True:
        Button =btn.configure(font=(random.choice(list_of_Font), Random_Font_size, "bold"))
        Label =lbl.configure(font=(random.choice(list_of_Font), Random_Font_size, "bold"))
        Text =txt.configure(font=(random.choice(list_of_Font), Random_Font_size, "bold"))
        Checkbutton =chk.configure(font=(random.choice(list_of_Font), Random_Font_size, "bold"))
        Radiobutton =rad.configure(font=(random.choice(list_of_Font), Random_Font_size, "bold"))
    else:
        Button =btn.configure(font=(random.choice(list_of_Font), Random_Font_size))
        Label =lbl.configure(font=(random.choice(list_of_Font), Random_Font_size))
        Text = txt.configure(font=(random.choice(list_of_Font), Random_Font_size))
        Checkbutton = chk.configure(font=(random.choice(list_of_Font), Random_Font_size))
        Radiobutton = rad.configure(font=(random.choice(list_of_Font), Random_Font_size))
# a function to change the color of the text
list_of_color = ["red", "blue", "green", "black"]
def random_font_color(Button, Label, Text,  Checkbutton, Radiobutton):
    if random_choice_50() == True:
        Button =btn.configure(fg=random.choice(list_of_color))
        Label =lbl.configure(fg=random.choice(list_of_color))
        Text = txt.configure(fg=random.choice(list_of_color))
        Checkbutton = chk.configure(fg=random.choice(list_of_color))
        Radiobutton = rad.configure(fg=random.choice(list_of_color))

    else:
        Button =btn.configure(fg="black")
        Label =lbl.configure(fg="black")
        Text = txt.configure(fg="black")
        Checkbutton = chk.configure(fg=random.choice(list_of_color))
        Radiobutton = rad.configure(fg=random.choice(list_of_color))
def create_label(lbl, btn, txt, chk, rad, Random_Position_Label_x, Random_Position_Label_y, i, list_of_Element_position):
        lbl.place(x=Random_Position_Label_x[i], y=Random_Position_Label_y[i])

        if (random_choice_80() == True):
            String_Label = random_sentence(random.randint(1, 4))
        else:
            String_Label = random_string(Random_Text_Size)
        lbl.config(text=String_Label)
        random_font_color(btn, lbl, txt, chk, rad)
        random_font_style(btn, lbl, txt, chk, rad)
        root.update()
        root.after(5)
        # time.sleep(5)

        print(String_Label)
        widget_x1, widget_x2 = lbl.winfo_rootx(), lbl.winfo_rootx() + lbl.winfo_width()
        widget_y1, widget_y2 = lbl.winfo_rooty(), lbl.winfo_rooty() + lbl.winfo_height()
        Label_position_x = (widget_x1, widget_x2)
        Label_position_y = (widget_y1, widget_y2)
        Label_Position = ("Label ", Label_position_x, Label_position_y, String_Label)
        list_of_Element_position.append(Label_Position)


def create_label_1(lbl, btn, txt, chk, rad, Randomly_Element, Randomly_Element_selected, Random_Position_Label_x, Random_Position_Label_y, i,String_Label):
        lbl.place(x=Random_Position_Label_x[i], y=Random_Position_Label_y[i])
        lbl.config(text=String_Label)

        random_font_color(btn, lbl, txt, chk, rad)
        random_font_style(btn, lbl, txt, chk, rad)
        root.update()
        root.after(1)
        widget_x1, widget_x2 = lbl.winfo_rootx(), lbl.winfo_rootx() + lbl.winfo_width()
        widget_y1, widget_y2 = lbl.winfo_rooty(), lbl.winfo_rooty() + lbl.winfo_height()
        Label_position_x = (widget_x1, widget_x2)
        Label_position_y = (widget_y1, widget_y2)
        return Label_position_x, Label_position_y
        lbl.grid_forget()
        root.update()
        root.after(1)





x = random.randint(5, 300)

  #tkinter.Button(root, text="Button ", height=1, width=1).place(x=17*i,y=24*3)
Samples_number =0

filename = "list_of_elements.txt"

while Samples_number < 30:
    root = tkinter.Tk()
    n = random.randint(5, 10)
    root.update()

    # Get the current screen width and height
    step = 0.8
    random_number = random.uniform(1, 2)
    screen_width = int (root.winfo_screenwidth()/round(random_number / step) )
    screen_height = int (root.winfo_screenheight()/round(random_number / step) )

    # Set the dimensions of the window
    root.geometry(f"{screen_width}x{screen_height}")
    root.update()

    # Define the region of the screen to capture
    x, y = root.winfo_rootx(), root.winfo_rooty()
    screen_width, screen_height = root.winfo_width(), root.winfo_height()
    region = (x, y, screen_width,  screen_height)
    list_of_Element_position = []
    Random_Position_Button_x = []
    Random_Position_Button_x = Random_Positions_x()
    Random_Position_Button_y = []
    Random_Position_Button_y = Random_Positions()
    Random_Position_Label_x = []
    Random_Position_Label_x = Random_Positions_x()
    Random_Position_Label_y = []
    Random_Position_Label_y = Random_Positions()
    Random_Position_Text_x = []
    Random_Position_Text_x = Random_Positions_x()
    Random_Position_Text_y = []
    Random_Position_Text_y = Random_Positions()
    Random_Position_Check_x = []
    Random_Position_Check_x = Random_Positions_x()
    Random_Position_Check_y = []
    Random_Position_Check_y = Random_Positions()
    Random_Position_Radio_x = []
    Random_Position_Radio_x = Random_Positions_x()
    Random_Position_Radio_y = []
    Random_Position_Radio_y = Random_Positions()
    Random_Position_Combo_x = []
    Random_Position_Combo_x = Random_Positions_x()
    Random_Position_Combo_y = []
    Random_Position_Combo_y = Random_Positions()
    Random_Position_List_x = []
    Random_Position_List_x = Random_Positions_x()
    Random_Position_List_y = []
    Random_Position_List_y = Random_Positions()
    Random_Position_Scroll_x = []
    Random_Position_Scroll_x = Random_Positions_x()
    Random_Position_Scroll_y = []
    Random_Position_Scroll_y = Random_Positions()
    Random_Position_Scale_x = []
    Random_Position_Scale_x = Random_Positions_x()
    Random_Position_Scale_y = []
    Random_Position_Scale_y = Random_Positions()
    Random_Position_Spin_x = []
    Random_Position_Spin_x = Random_Positions_x()
    Random_Position_Spin_y = []
    Random_Position_Spin_y = Random_Positions()
    Random_Position_Menu_x = []
    Random_Position_Menu_x = Random_Positions_x()
    Random_Position_Menu_y = []
    Random_Position_Menu_y = Random_Positions()
    Random_Position_MenuButton_x = []
    Random_Position_MenuButton_x = Random_Positions_x()
    Random_Position_MenuButton_y = []
    Random_Position_MenuButton_y = Random_Positions()
    Random_Position_Message_x = []
    Random_Position_Message_x = Random_Positions_x()
    Random_Position_Message_y = []
    Random_Position_Message_y = Random_Positions()
    Random_Position_PanedWindow_x = []
    Random_Position_PanedWindow_x = Random_Positions_x()
    for i in range(0, 300):

        Randomly_Height = random.randint(20, 40)
        Randomly_Width = random.randint(40, 200)
        Randomly_Height_text = random.randint(1, 2)
        Randomly_Width_text = random.randint(20, 40)
        Randomly_Element = random.randint(1, 15)
        Randomly_Element_selected = random.randint(1, 15)
        Random_Text_Size = random.randint(3, 15)
        Random_Font_size = random.randrange(7, 12, 1)
        txt = tkinter.Text(root, height=Randomly_Height_text, width=Randomly_Width_text)
        lbl = tkinter.Label(root, text='label', font=("Arial", Random_Font_size, "bold"))
        chk = tkinter.Checkbutton(root)
        rad = tkinter.Radiobutton(root, text='radio')
        combo = tkinter.ttk.Combobox(root, values=[1, 2, 3, 4, 5])
        btn = tkinter.Button(root)

        listbox = tkinter.Listbox(root)
        scroll = tkinter.Scrollbar(root)
        scale = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL)
        spin = tkinter.Spinbox(root, from_=0, to=100)
        menu = tkinter.Menu(root)
        menubutton = tkinter.Menubutton(root, text='menu')
        message = tkinter.Message(root, text='message')

        j = len(list_of_Element_position)
        if len(list_of_Element_position) == 0:
            # btn = tkinter.Button(root, )
            btn.place(height=Randomly_Height, width=Randomly_Width,x=0, y=0)
            # time.sleep(0.1)
            root.update()

            widget_x1, widget_x2 = btn.winfo_rootx(), btn.winfo_rootx() + btn.winfo_width()
            widget_y1, widget_y2 = btn.winfo_rooty(), btn.winfo_rooty() + btn.winfo_height()
            position_x = (widget_x1, widget_x2)
            position_y = (widget_y1, widget_y2)
            Button_Position = ("Button ", position_x, position_y)
            list_of_Element_position.append(Button_Position)

            shift_x = list_of_Element_position [0][1][0]
            shift_y = list_of_Element_position [0][2][0]
        # root.after(1)
        # a loop to check if the position of the element is not overlapping with the previous elements and avaiding overlapping
        for k in range(0, j):
            if (in_interval(Random_Position_Button_x[i]+shift_x,
            (list_of_Element_position[k][1][0]-pixel_of_width(Randomly_Width)*2, list_of_Element_position[k][1][1])) == True) \
                    and (in_interval(Random_Position_Button_y[i]+shift_y,(list_of_Element_position[k][2][0]-pixel_of_height(Randomly_Height), list_of_Element_position[k][2][1])) == True) \
                    or (in_interval(Random_Position_Label_x[i]+shift_x,(list_of_Element_position[k][1][0] -pixel_of_width(Randomly_Width), list_of_Element_position[k][1][1])) == True) \
                    and (in_interval( Random_Position_Label_y[i]+shift_y,(list_of_Element_position[k][2][0] -pixel_of_height(Randomly_Height)*2, list_of_Element_position[k][2][1])) == True) \
                    or (in_interval(Random_Position_Text_x[i]+shift_x,(list_of_Element_position[k][1][0]-pixel_of_width(Randomly_Width), list_of_Element_position[k][1][1])) == True ) \
                    or ( in_interval( Random_Position_Text_y[i]+shift_y,(list_of_Element_position[k][2][0] -pixel_of_height(Randomly_Height), list_of_Element_position[k][2][1])) == True)\
                    or (in_interval(Random_Position_Check_x[i]+shift_x,(list_of_Element_position[k][1][0] -pixel_of_width(Randomly_Width), list_of_Element_position[k][1][1])) == True) \
                    and (in_interval(Random_Position_Check_y[i]+shift_y,(list_of_Element_position[k][2][0] -pixel_of_height(Randomly_Height), list_of_Element_position[k][2][1])) == True) \
                    or (in_interval(Random_Position_Radio_x[i]+shift_x,(list_of_Element_position[k][1][0] -pixel_of_width(Randomly_Width), list_of_Element_position[k][1][1])) == True) \
                    and (in_interval(Random_Position_Radio_y[i]+shift_y,(list_of_Element_position[k][2][0] -pixel_of_height(Randomly_Height), list_of_Element_position[k][2][1])) == True) :
                Randomly_Element = 0

        #creating the elements
        #creating the button
        if (Randomly_Element == Randomly_Element_selected ):
            btn = tkinter.Button(root, height=Randomly_Height, width=Randomly_Width)

            btn.place(height=Randomly_Height, width=Randomly_Width,x=Random_Position_Button_x[i], y=Random_Position_Button_y[i])

            #wait for  one second
            # time.sleep(.8)
            root.update()
            root.update_idletasks()

            #getting the position of the button
            widget_x1, widget_x2 = btn.winfo_rootx(), btn.winfo_rootx() + btn.winfo_width()
            widget_y1, widget_y2 = btn.winfo_rooty(), btn.winfo_rooty() + btn.winfo_height()
            position_x = (widget_x1, widget_x2)
            position_y = (widget_y1, widget_y2)

            Button_Position = ("Button ", position_x, position_y)
            string_of_button=""
            #change the text of the button randomly
            if (random_choice_80()== True):

                string_of_button = random_sentence(1)

                if (Randomly_Width < len(string_of_button)):

                    btn.config(text ="")
                    Button_Position = ("Button ", position_x, position_y,)
                else:
                    btn.config(text = string_of_button)
                    Button_Position = ( "Button ", position_x, position_y, string_of_button)
            else:
                string_of_button = random_string(Random_Text_Size)
                if (Randomly_Width < len(string_of_button)):
                    btn.config(text="")
                    Button_Position = ("Button ", position_x, position_y,)
                else:
                    btn.config(text=string_of_button)
                    Button_Position = ("Button ", position_x, position_y, string_of_button)


            list_of_Element_position.append(Button_Position)

        Randomly_Element_selected = random.randint(1, 15)

        #creating the label
        if (Randomly_Element == Randomly_Element_selected ):
            create_label(lbl, btn, txt, chk, rad, Random_Position_Label_x,
                         Random_Position_Label_y, i, list_of_Element_position)
            Randomly_Element_selected = random.randint(1, 15)

        #creating the text
        if (Randomly_Element ==Randomly_Element_selected):
            txt.place(x=Random_Position_Text_x[i], y=Random_Position_Text_y[i])

            # change the text of the label to the random string of words
            String_Text = random_sentence(random.randint(1, 3))
            if (random_choice_80 ()== True):
                String_Text = random_sentence(random.randint(1, 3))
                txt.insert(tkinter.END, String_Text)
                Text_Position = ("Text ", position_x, position_y, String_Text)
            else:
                String_Text = random_string(Random_Text_Size)
                txt.insert(tkinter.END, String_Text)
                Text_Position = ("Text ", position_x, position_y, String_Text)
            root.update()

            widget_x1, widget_x2 =txt.winfo_rootx(), txt.winfo_rootx() + txt.winfo_width()
            widget_y1, widget_y2 = txt.winfo_rooty() , txt.winfo_rooty() + txt.winfo_height()
            Text_position_x = (widget_x1, widget_x2)
            Text_position_y = (widget_y1, widget_y2)
            Text_Position = ("Text", Text_position_x, Text_position_y,(String_Text))

            # change the text of the label to the random string of words
            list_of_Element_position.append(Text_Position)
        #add a check box to the list of element position
        Randomly_Element_selected = random.randint(1, 15)
        #creating the check box
        if (Randomly_Element ==Randomly_Element_selected):
            chk.place(x=Random_Position_Check_x[i], y=Random_Position_Check_y[i])
            Check_Scale = random.randint(0, 1)
            Check_position_x = (0, 0)
            Check_position_y = (0, 0)
            String_Check=""
            #click the check box
            if ( Check_Scale == 1):
                chk.select()
            else:
                chk.deselect()
            if (random_choice_80() == True):
                String_Check = random_sentence(1)
                chk.config(text=String_Check)
                Check_Position = ("Checkbutton ", Check_position_x, Check_position_y, String_Check)
            else:
                String_Check = random_string(Random_Text_Size)
                chk.config(text=String_Check)
                Check_Position = ("Checkbutton ", Check_position_x, Check_position_y, String_Check)
            root.update()
            create_label_1(lbl, btn, txt, chk, rad, Randomly_Element, Randomly_Element_selected, Random_Position_Check_x,Random_Position_Check_y, i,String_Check)
            # time.sleep(.4)
            widget_x1, widget_x2 = chk.winfo_rootx(), chk.winfo_rootx() + chk.winfo_width()
            widget_y1, widget_y2 = chk.winfo_rooty(), chk.winfo_rooty() + chk.winfo_height()
            Check_position_x = (widget_x1, widget_x2)
            Check_position_y = (widget_y1, widget_y2)
            if ( Check_Scale == 1):
                Check_Position = ("Checkbutton", Check_position_x, Check_position_y,String_Check, "Checked")
            else:
                Check_Position = ("Checkbutton ", Check_position_x, Check_position_y,String_Check, "Unchecked")
            list_of_Element_position.append(Check_Position)
        Randomly_Element_selected = random.randint(1, 15)
        #creating the radio button
        if (Randomly_Element ==Randomly_Element_selected):
            rad.place(x=Random_Position_Radio_x[i], y=Random_Position_Radio_y[i])

            radio_scale = random.randint(0, 1)
            if (radio_scale == 1):
                rad.select()
            else:
                rad.deselect()


            root.update()

            String_Radio = random_sentence(2)
            rad.configure(text=String_Radio)
            create_label_1(lbl, btn, txt, chk, rad, Randomly_Element, Randomly_Element_selected, Random_Position_Radio_x,Random_Position_Radio_y, i,String_Radio)

            widget_x1, widget_x2 = rad.winfo_rootx(), rad.winfo_rootx() + rad.winfo_width()
            widget_y1, widget_y2 = rad.winfo_rooty(), rad.winfo_rooty() + rad.winfo_height()
            Radio_position_x = (widget_x1, widget_x2)
            Radio_position_y = (widget_y1, widget_y2)

            if (radio_scale == 1):
                Radio_Position = ("Radiobutton", Radio_position_x, Radio_position_y,String_Radio, "Checked")
            else:
                Radio_Position = ("Radiobutton ", Radio_position_x, Radio_position_y,String_Radio, "Unchecked")

            list_of_Element_position.append(Radio_Position)

    #change the font style of the string to radomly  font for each button
    # change the color of font to random color
    # make screenshot of the Gui and save it in the folder
    # myScreenshot = pyautogui.screenshot()
    # path = "C:\\Users\\abulabn\\Desktop\\Test\\"
    # myScreenshot.save(path +"screenshot" + str(Samples_number) + ".png")

    # #filter the  element depending on the name of the element
    # list_of_Button_position = [x for x in list_of_Element_position if x[0] == "Button "]
    # list_of_Label_position = [x for x in list_of_Element_position if x[0] == "Label "]
    # list_of_Text_position = [x for x in list_of_Element_position if x[0] == "Text"]
    # list_of_Check_position = [x for x in list_of_Element_position if x[0] == "Check"]
    # list_of_Radio_position = [x for x in list_of_Element_position if x[0] == "Radiobutton "]
    # list_of_Scale_position = [x for x in list_of_Element_position if x[0] == "Scale"]
    #
    # #dictionary of the element position
    # # for i in range(len(list_of_Button_position)):
    # #     dict = {"x1-x2": list_of_Button_position[i][1], "y1-y2": list_of_Button_position[i][2]}
    #

    # df = pd.DataFrame(dict)
    # print(df)
    # df.to_csv("C:\\Users\\abulabn\\Desktop\\Test\\test.csv")

    #save the list of element position in a csv file in the folder
    with open("C:\\Users\\abulabn\\Desktop\\Test\\" + str(Samples_number) + ".csv", "w") as out:
        csv_out=csv.writer(out)
        #add a title to the csv file
        # csv_out.writerow(["ScreenShot{}".format(Samples_number)])
        # acsses to fist value of of the second  element of the list
        csv_out.writerow(['Element', 'x1',  'y1', 'x2','y2', 'String', 'Checked/Unchecked'])
        for i in range(len(list_of_Element_position)):
            if len(list_of_Element_position[i]) == 3:
                csv_out.writerow([list_of_Element_position[i][0],list_of_Element_position[i][1][0],list_of_Element_position[i][2][0] ,list_of_Element_position[i][1][1],list_of_Element_position[i][2][1]])
            if len( list_of_Element_position[i]) == 4:
                csv_out.writerow(
                    [list_of_Element_position[i][0], list_of_Element_position[i][1][0], list_of_Element_position[i][2][0],list_of_Element_position[i][1][1], list_of_Element_position[i][2][1], list_of_Element_position[i][3]])

            if len( list_of_Element_position[i]) == 5:
                csv_out.writerow([list_of_Element_position[i][0], list_of_Element_position[i][1][0], list_of_Element_position[i][2][0],list_of_Element_position[i][1][1], list_of_Element_position[i][2][1], list_of_Element_position[i][3], list_of_Element_position[i][4]])


    #print the fist 10 buttons position


    root.destroy()
    #print the time of the execution
    # #print the number of the iteration
    # print("the number of the iteration is ", Samples_number)
    # print(list_of_Element_position)
    # lines[Samples_number]= "the number of the iteration is "+ str(Samples_number) +str(list_of_Element_position) + "\n"
    # with open(filename, "w") as file:
    path = "C:\\Users\\abulabn\\Desktop\\Test\\"
    filename = "screenshot_region_"
    take_screenshot(path,region, filename, Samples_number)
    #         file.writelines(" ".join(["the number of the iteration is ", str(Samples_number), str(list_of_Element_position)]) + "\n")
    Samples_number = Samples_number + 1
    # destroy the gui
    root.mainloop()



