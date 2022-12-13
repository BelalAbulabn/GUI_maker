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
  for i in range(0, 140):
    o = random.randrange(0, 1700, 10)
    if o not in randomlist:
      randomlist.append(o)
  return randomlist
def Random_Positions_x():
  randomlist = []
  for i in range(0, 140):
    o = random.randrange(0, 2100, 10)
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
    return 15 * n + 35

def pixel_of_width(n):
    return 7 * n + 25
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


x = random.randint(5, 300)

  #tkinter.Button(root, text="Button ", height=1, width=1).place(x=17*i,y=24*3)
Samples_number =0





while Samples_number < 20:
    root = tkinter.Tk()
    n = random.randint(5, 10)
    root.geometry("1700x1000")
    # set the Gui maximized
    root.state('zoomed')
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
    for i in range(0, 60):

        Randomly_Height = random.randint(1, 2)
        Randomly_Width = random.randint(1, 10)
        Randomly_Width_Text = random.randint(20,30)
        Randomly_X_Position_Button = random.randint(1, 6)
        Randomly_Y_Position_Button = random.randint(1, 500)
        Randomly_X_Position_Label = random.randint(1, 9)
        Randomly_Y_Position_Label = random.randint(1, 500)
        Randomly_Element = random.randint(1, 15)
        Randomly_Element_selected = random.randint(1, 15)
        Random_Text_Size = random.randint(3, 15)
        Randomly_X_Position_Label = random.randint(1, 7)
        Randomly_Y_Position_Label = random.randint(1, 9)
        Random_Font_size = random.randrange(7, 12, 1)
        z=str(i)
        txt = tkinter.Text(root, height=Randomly_Height, width=Randomly_Width_Text)
        btn = tkinter.Button(root, height=Randomly_Height, width=Randomly_Width)
        lbl = tkinter.Label(root, text='label', font=("Arial", Random_Font_size, "bold"))
        chk = tkinter.Checkbutton(root)
        rad = tkinter.Radiobutton(root, text='radio')
        combo = tkinter.ttk.Combobox(root, values=[1, 2, 3, 4, 5])
        listbox = tkinter.Listbox(root)
        scroll = tkinter.Scrollbar(root)
        scale = tkinter.Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL)
        spin = tkinter.Spinbox(root, from_=0, to=100)
        menu = tkinter.Menu(root)
        menubutton = tkinter.Menubutton(root, text='menu')
        message = tkinter.Message(root, text='message')

        j = len(list_of_Element_position)
        if len(list_of_Element_position) == 0:
            btn = tkinter.Button(root, height=Randomly_Height, width=Randomly_Width)
            btn.place(x=0, y=0)
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
        #a loop to check if the position of the element is not overlapping with the previous elements and avaiding overlapping
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
            btn.place(x=Random_Position_Button_x[i], y=Random_Position_Button_y[i])
            root.update()
            widget_x1, widget_x2 = btn.winfo_rootx(), btn.winfo_rootx() + btn.winfo_width()
            widget_y1, widget_y2 = btn.winfo_rooty() , btn.winfo_rooty() + btn.winfo_height()
            position_x = (widget_x1, widget_x2)
            position_y = (widget_y1, widget_y2)
            #change the text of the button randomly
            if (random_choice_80()== True):
                string_of_button = random_sentence(1)
                if (Randomly_Width < len(string_of_button) ):
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
            # print("Button Place", Button_Position, i)
            list_of_Element_position.append(Button_Position)

        Randomly_Element_selected = random.randint(1, 15)
        #creating the label
        if (Randomly_Element == Randomly_Element_selected):
            lbl.place(x=Random_Position_Label_x[i], y=Random_Position_Label_y[i])
            # change the text of the label to the random string of words
            # String_Label = random_sentence(random.randint(1, 5))

            if (random_choice_80 ()== True):
                String_Label = random_sentence(random.randint(1, 5))
                lbl.config(text=String_Label)
                Label_Position = ("Label ", position_x, position_y, String_Label)

            else:
                String_Label = random_string(Random_Text_Size)
                lbl.config(text=String_Label)
                Label_Position = ("Label ", position_x, position_y, String_Label)

            root.update()
            root.after(1)
            widget_x1, widget_x2 = lbl.winfo_rootx(), lbl.winfo_rootx() + lbl.winfo_width()
            widget_y1, widget_y2 = lbl.winfo_rooty() , lbl.winfo_rooty() + lbl.winfo_height()
            Label_position_x = (widget_x1, widget_x2)
            Label_position_y = (widget_y1, widget_y2)
            Label_Position = ("Label ", Label_position_x, Label_position_y,(String_Label))
            # print("Label Place", Label_position_y, i)
            list_of_Element_position.append(Label_Position)
        Randomly_Element_selected = random.randint(1, 15)
        #creating the text
        if (Randomly_Element ==Randomly_Element_selected):
            txt.place(x=Random_Position_Text_x[i], y=Random_Position_Text_y[i ])
            # change the text of the label to the random string of words
            # String_Text = random_sentence(random.randint(1, 3))
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
            # change the text of the label to the random string of words
            Text_Position = ("Text", Text_position_x, Text_position_y,(String_Text))
            list_of_Element_position.append(Text_Position)
        #add a check box to the list of element position
        Randomly_Element_selected = random.randint(1, 15)
        #creating the check box
        if (Randomly_Element ==Randomly_Element_selected):
            chk.place(x=Random_Position_Check_x[i], y=Random_Position_Check_y[i])
            Check_Scale = random.randint(0, 1)
            #click the check box
            if ( Check_Scale == 1):
                chk.select()
            else:
                chk.deselect()
            root.update()
            widget_x1, widget_x2 = chk.winfo_rootx(), chk.winfo_rootx() + chk.winfo_width()
            widget_y1, widget_y2 = chk.winfo_rooty(), chk.winfo_rooty() + chk.winfo_height()
            Check_position_x = (widget_x1, widget_x2)
            Check_position_y = (widget_y1, widget_y2)
            if (random_choice_80() == True):
                String_Check = random_sentence(1)
                chk.config(text=String_Check)
                Check_Position = ("Check ", Check_position_x, Check_position_y, String_Check)
            else:
                String_Check = random_string(Random_Text_Size)
                chk.config(text=String_Check)
                Check_Position = ("Check ", Check_position_x, Check_position_y, String_Check)
            if ( Check_Scale == 1):
                Check_Position = ("Check", Check_position_x, Check_position_y,String_Check, "Checked")
            else:
                Check_Position = ("Check ", Check_position_x, Check_position_y,String_Check, "Unchecked")
            list_of_Element_position.append(Check_Position)
        Randomly_Element_selected = random.randint(1, 15)
        #creating the radio button
        if (Randomly_Element ==Randomly_Element_selected):
            rad.place(x=Random_Position_Radio_x[i], y=Random_Position_Radio_y[i])
            root.update()
            radio_scale = random.randint(0, 1)
            if (radio_scale == 1):
                rad.select()
            else:
                rad.deselect()
            widget_x1, widget_x2 = rad.winfo_rootx(), rad.winfo_rootx() + rad.winfo_width()
            widget_y1, widget_y2 = rad.winfo_rooty(), rad.winfo_rooty() + rad.winfo_height()
            Radio_position_x = (widget_x1, widget_x2)
            Radio_position_y = (widget_y1, widget_y2)
            String_Radio = random_sentence(1)
            rad.configure(text=String_Radio)
            if (radio_scale == 1):
                Radio_Position = ("Radio", Radio_position_x, Radio_position_y,String_Radio, "Checked")
            else:
                Radio_Position = ("Radio ", Radio_position_x, Radio_position_y,String_Radio, "Unchecked")

            list_of_Element_position.append(Radio_Position)



    #change the font style of the string to radomly  font for each button
        random_font_style(btn,lbl,txt,chk,rad)
    # change the color of font to random color
        random_font_color(btn,lbl,txt,chk,rad)
    # make screenshot of the Gui and save it in the folder
    myScreenshot = pyautogui.screenshot()
    path = "C:\\Users\\abulabn\\Desktop\\Test\\"
    myScreenshot.save(path +"screenshot" + str(Samples_number) + ".png")

    print(len(list_of_Element_position))
    #filter the  element depending on the name of the element
    list_of_Button_position = [x for x in list_of_Element_position if x[0] == "Button "]
    list_of_Label_position = [x for x in list_of_Element_position if x[0] == "Label "]
    list_of_Text_position = [x for x in list_of_Element_position if x[0] == "Text"]
    list_of_Check_position = [x for x in list_of_Element_position if x[0] == "Check"]
    list_of_Radio_position = [x for x in list_of_Element_position if x[0] == "Radio "]
    list_of_Scale_position = [x for x in list_of_Element_position if x[0] == "Scale"]

    #dictionary of the element position
    # for i in range(len(list_of_Button_position)):
    #     dict = {"x1-x2": list_of_Button_position[i][1], "y1-y2": list_of_Button_position[i][2]}

    #print the  lentgtosf list of button position
    print("the length of the list of button position is ", len(list_of_Button_position))
    print("the length of the list of label position is ", len(list_of_Label_position))
    print("the length of the list of text position is ", len(list_of_Text_position))
    print("the length of the list of check position is ", len(list_of_Check_position))
    print("the length of the list of radio position is ", len(list_of_Radio_position))
    print("the length of the list of scale position is ", len(list_of_Scale_position))


    # df = pd.DataFrame(dict)
    # print(df)
    # df.to_csv("C:\\Users\\abulabn\\Desktop\\Test\\test.csv")

    print(list_of_Element_position)
    #save the list of element position in a csv file in the folder
    with open("C:\\Users\\abulabn\\Desktop\\Test\\" + str(Samples_number) + ".csv", "w") as out:
        csv_out=csv.writer(out)
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
    Samples_number= Samples_number + 1
    #destroy the gui

    root.destroy()
    #print the time of the execution
    #print the number of the iteration
    print("the number of the iteration is ", Samples_number)

    root.mainloop()



