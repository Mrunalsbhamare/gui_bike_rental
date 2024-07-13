from tkinter import *
from PIL import Image , ImageTk
from customtkinter import *
import datetime

class bike_rental :

    def __init__(self) :

        self.list = {
            "Honda Shine": 15,
            "Hero Glamour": 10,
            "KTM 200 Duke": 5,
        }
        self.list2 = {}

    def bikes_available(self) :
        available_bikes = "\n".join(f"{bike}: {quantity}" for bike, quantity in self.list.items())
        return f"Available bikes :\n\n{available_bikes}"
    
    def bike_names(self) :
        return 'Bikes names are as follows\n\n' +  "\n".join(self.list.keys())

    def rent_shine(self):
        rent = (
                "Honda Shine's rent:\n"
                "Daily   =   ₹350\n"
                "Weekly  =   ₹2100\n"
                "Monthly =   ₹6000\n"
            )
        return rent
    
    def rent_glamour(self) :
            rent = (
                "Hero Glamour's rent:\n"
                "Daily   =   ₹350\n"
                "Weekly  =   ₹2000\n"
                "Monthly =   ₹6000\n"
            )
            return rent
    
    def rent_ktm(self):

        rent = (
                "KTM 200 Duke's rent:\n"
                "Daily   =   ₹800\n"
                "Weekly  =   ₹4500\n"
                "Monthly =   ₹12000\n"
            )
        return rent
    
    def discount(self):
        return (
            "**** Exclusive Discount ****\n\n"
            "Flat ₹500 off on total weekly charges of any bike & \n"
            "Heavy ₹1000 off on total monthly charges of KTM 200 Duke"
        )
    
class customer(bike_rental) :
    def rent_bike(self, customer_name, bike_name, quantity) :

        if customer_name== "":
            return "Please enter name"
        elif bike_name == "" :
            return "Please enter bikes name"
        elif bike_name == "Enter bikes name here...." :
            return "Please enter bikes name"
        elif quantity == ""  "Enter quantity here....":
            return "Please enter quantity"
        elif quantity == "Enter quantity here....":
            return "Please enter quantity"
        else:    
            if customer_name in self.list2 :
                return "Customer already exists\nRegister with different name\n"
            else:
                if bike_name in self.list:
                    if self.list[bike_name] >= quantity:
                        self.list[bike_name] -= quantity
                        time = datetime.datetime.now()

                        details = ("Bike rented successfully \n"
                                "Your details are \n"
                                    "\n"
                                    f"Name: {customer_name}\n"
                                    f"Bike: {bike_name}\n"
                                    f"Quantity: {quantity}\n"
                                    f"Date & Time: {datetime.datetime.now()}\n"
                                    )
                        self.list2[customer_name] = {}
                        self.list2[customer_name]["Name"] = customer_name
                        self.list2[customer_name]["Bike"] = bike_name
                        self.list2[customer_name]["Quantity"] = quantity
                        self.list2[customer_name]["Date & Time"] = time

                        return details
                        
                    else:
                        return f"Insufficient stock for {bike_name}.\n"
                else:
                    return "Invalid bike name.\n"
        
    def enquiry(self,customer_name) :

        if customer_name in self.list2 :
            bike_name = self.list2[customer_name]["Bike"]
            quantity = self.list2[customer_name]["Quantity"]
            issue_time = self.list2[customer_name]["Date & Time"]
            current_time = datetime.datetime.now()
            final = (current_time - issue_time)
            total_hours = final.total_seconds() / 3600
            details = (
                    f"Your details:\n"
                    f"Name: {customer_name}\n"
                    f"Bike: {bike_name}\n"
                    f"Quantity: {quantity}\n"
                    f"Issuing Date & Time:    {issue_time} \n"
                    f"Hours since issuing:     {total_hours}"
                )
            return details
        elif customer_name == "":
            return "Please enter registered name first"
        else:
            return "No rental records found for this customer.\n"

    def return_bike(self,customer_name) :

        if customer_name == "":
            return "Please enter registered name"
        elif customer_name not in self.list2 :
            return "No bike rented to this person"
        else:
            if customer_name in self.list2 :
                quant = self.list2[customer_name]["Quantity"]
                bike_name = self.list2[customer_name]["Bike"]
                issue_time = self.list2[customer_name]["Date & Time"]
                current_time = datetime.datetime.now()
                final = (current_time - issue_time)
                total_hours = final.total_seconds() / 3600
                self.list[bike_name] += quant

                if bike_name == "Honda Shine" :
                    if total_hours < 24 :
                        return(
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            f"Your Bill is ₹{350*quant}")
                    elif total_hours > 24 and total_hours < 168:
                        days = total_hours/ 24
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f'Your Bill = ₹{350*days*quant}')
                    elif total_hours > 168 and total_hours < 720 :
                        weeks = total_hours / 168
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours}hrs\n\n"                       
                            
                            f'Your Bill = ₹{2100*weeks*quant}'
                            f"Applying exclusive discount Final Bill = {(2100*weeks*quant)-500}")
                    else :
                        months = total_hours / 720
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f"Your Bill = ₹{6000*months*quant}")
                
                elif bike_name == "Hero Glamour" :
                    if total_hours < 24 :
                        return(
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f"Your Bill is ₹{350*quant}")
                    elif total_hours > 24 and total_hours < 168:
                        days = total_hours/ 24
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f'Your Bill = ₹{350*days*quant}')
                    elif total_hours > 168 and total_hours < 720 :
                        weeks = total_hours / 168
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f'Your Bill = ₹{2000*weeks*quant}'
                            f"Applying exclusive discount Final Bill = {(2000*weeks*quant)-500}")
                    else :
                        months = total_hours / 720
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f"Your Bill = ₹{6000*months*quant}")

                elif bike_name == "KTM 200 Duke" :
                    if total_hours < 24 :
                        return(
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f"Your Bill is ₹{800*quant}")
                    elif total_hours > 24 and total_hours < 168:
                        days = total_hours/ 24
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f'Your Bill = ₹{800*days*quant}')
                    elif total_hours > 168 and total_hours < 720 :
                        weeks = total_hours / 168
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            

                            f'Your Bill = ₹{4500*weeks*quant}'
                            f"Applying exclusive discount Final Bill = {(4500*weeks*quant)-500}")
                    else :
                        months = total_hours / 720
                        return (
                            f"Your details:\n"
                            f"Name: {customer_name}\n"
                            f"Bike: {bike_name}\n"
                            f"Quantity: {quant}\n"
                            f"Time : {total_hours} hrs\n\n"
                            
                            
                            f"Your Bill = ₹{12000*months*quant}"
                            f"Applying exclusive  discount Final Bill = {(12000*weeks*quant)-1000}")
                    
                

            










root = CTk()

root.geometry("1300x705")

root.title("Bike Rental System")

root.config(bg="#1e3d59")

c1 = customer()

user_name = StringVar()
value = StringVar()
bike_name = StringVar()
quantity = IntVar()

def entry_name(user_name):

    if user_name == "":
        return "Please enter name"
    else:
        return f"Welcome {user_name} !!!"

def b1_gui():
    
    input2.delete(0,END)
    input3.delete(0.0,END)
    input4.delete(0,END)
    input3.insert(END, entry_name(user_name.get()))
    
def b2_gui():

    input3.delete(0.0,END)
    input3.insert(END, c1.bike_names())
    
def b3_gui():

    input3.delete(0.0,END)
    input3.insert(END, c1.bikes_available())

def b4_gui():

    input3.delete(0.0,END)
    input3.insert(END, c1.discount())

def b5_gui():

    input3.delete(0.0,END)
    input3.insert(END, c1.enquiry(user_name.get()))

def b6_gui(choice):

    value = b6.get()
    if value == "Honda Shine" :
        input3.delete(0.0,END)
        input3.insert(END, c1.rent_shine())
    elif value == "Hero Glamour" :
        input3.delete(0.0,END)
        input3.insert(END, c1.rent_glamour())
    elif value == "KTM 200 Duke" :
        input3.delete(0.0,END)
        input3.insert(END, c1.rent_ktm())

def b7_gui():

    input2.delete(0,END)
    input3.delete(0.0,END)
    input4.delete(0,END)
    input2.insert(0,"Enter bikes name here....")
    input2.bind('<FocusIn>',lambda args:input2.delete('0','end'))
    input3.insert(END, c1.bikes_available() + "\n\n" + "Enter bikes name in box above and click 'Submit Bikes Name' ")

def b8_gui():

    input3.delete(0.0,END)
    input3.insert(END , c1.return_bike(user_name.get()))

def b10_gui() :

    input4.delete(0,END)
    input3.delete(0.0,END)
    input4.insert(0,"Enter quantity here....")
    input4.bind('<FocusIn>',lambda args:input4.delete('0','end'))
    input3.insert(END, c1.bikes_available() + "\n\n" + "Enter quantity of bike in box above and click 'Submit Quantity'")
    

def b11_gui() :

    input3.delete(0.0,END)
    input3.insert(END, c1.rent_bike(user_name.get(),bike_name.get(),quantity.get()))

def b12_gui() :

    input1.delete(0,END)
    input2.delete(0,END)
    input3.delete(0.0,END)
    input4.delete(0,END)

    











frame = CTkFrame(master = root , fg_color= "#45454B" , border_color="#002A54", border_width=2 ,corner_radius= 32,
                  width = 750 , height= 650)
frame.grid( row = 0 , column = 0 , padx = 20, pady = 15 )

label1 = CTkLabel(master = frame , text = "Enter your name :",font = ("Arial",13), text_color= "#FFFFFF")
label1.grid(row = 0,column = 0 , padx = 15)

input1 = CTkEntry(master= frame , textvariable = user_name , font = ('Arial',13), width = 200,text_color= "#000000",
                   fg_color="#F5F5F5")
input1.grid(row = 0 , column= 1, sticky= W , pady = 15)

photo = Image.open("C:\\Users\\bhama\\Desktop\\motorcycle-logo.jpg")
resized = photo.resize((500,420), Image.ANTIALIAS)
final = ImageTk.PhotoImage(resized)

label_i1 = Label(root , image = final , width = 500 , height = 420)
label_i1.grid(row = 0 ,column = 1 )

input2 = CTkEntry(master = root, textvariable= bike_name,  width= 825  ,fg_color="#F5F5F5",text_color= "#000000",
                  corner_radius= 32)
input2.grid(row = 1 , column = 0 , pady = 10,padx = 20)

input4 = CTkEntry(master = root,textvariable= quantity,  width= 825 ,text_color= "#000000",
                  fg_color="#F5F5F5", corner_radius= 32)
input4.grid(row = 2 , column = 0 , pady = 10)

input3 = CTkTextbox(master = root,  width= 825 , height= 200,text_color= "#FFFFFF",
                    fg_color="#45454B", corner_radius= 32)
input3.grid(row = 3 , column = 0 , pady = 10)

photo2 = Image.open("C:\\Users\\bhama\\Desktop\\bike.jpeg")
resized2 = photo2.resize((500,243), Image.ANTIALIAS)
final2 = ImageTk.PhotoImage(resized2)

label_i2 = Label(root , image = final2 , width = 500 , height = 243)
label_i2.grid(row = 3 ,column= 1 , padx = 15)



b1 = CTkButton(master = frame ,text = "Save",font = ("Arial",11) , corner_radius= 32,text_color= "#FFFFFF" ,
                fg_color="transparent",border_color="#FFCC70",border_width=2,command = b1_gui)
b1.grid(row = 1, column = 1, pady = 5, sticky = W, padx = 33 )

b2 = CTkButton(master =frame , text = "Check Bikes Name", font = ("Arial", 13), corner_radius= 32 ,
                command= b2_gui, width= 168)
b2.grid( row = 3, column = 1 , pady = 20, sticky= W, padx = 16 )

b3 = CTkButton(master =frame , text = "Check available bikes", font = ("Arial", 13), corner_radius= 32,
               command= b3_gui,width= 172)
b3.grid( row = 3, column = 2, sticky= W , padx = 160 )

b4 = CTkButton(master =frame , text = "Check Ongoing Discount", font = ("Arial", 13), corner_radius= 32,
               command = b4_gui, )
b4.grid( row = 4, column = 1 , sticky= W, pady = 15, padx = 16)

b5 = CTkButton(master =frame , text = "Enquiry about rented bike", font = ("Arial", 13), corner_radius= 32,
               command= b5_gui, width= 100)
b5.grid( row = 4, column = 2, sticky= W , padx = 160)

b6 = CTkComboBox(master =frame ,values=["Rent enquiry","Honda Shine","Hero Glamour","KTM 200 Duke"]
                 , font = ("Arial", 13), corner_radius= 32 , fg_color="#0093E9",width= 168,
                   command= b6_gui )
b6.grid( row = 5, column = 1 , pady = 20, sticky= W, padx = 16)

b7 = CTkButton(master =frame , text = "Rent a bike", font = ("Arial", 13),
                corner_radius= 32, command= b7_gui,width= 172)
b7.grid( row = 5, column = 2, sticky= W , padx = 160)

b8 = CTkButton(master =frame , text = "Return bike", font = ("Arial", 13),
               command= b8_gui, corner_radius= 32 , width= 168)
b8.grid( row = 6, column = 1 , sticky= W , pady = 15, padx = 16)

b9 = CTkButton (master= frame , text = "Quit", corner_radius=32, width= 172)
b9.grid(row = 6 , column = 2, sticky = W , padx = 160)
b9.bind('<Button-1>', quit)

b10 = CTkButton(master = root ,text = "Submit Bikes Name",font = ("Arial",11) , corner_radius= 32,
                fg_color="transparent",border_color="#FFCC70",border_width=2,command = b10_gui)
b10.grid(row = 1, column = 1 , pady = 10, sticky = W, padx = 13 )

b11 = CTkButton(master = root ,text = "Submit Quantity",font = ("Arial",11) , corner_radius= 32,
                fg_color="transparent",border_color="#FFCC70",border_width=2,command = b11_gui)
b11.grid(row = 2, column = 1 , pady = 10, sticky = W, padx = 13 )

b12 = CTkButton(master = frame ,text = "Clear / New Entry",font = ("Arial",11) , corner_radius= 32,
                text_color= "#FFFFFF",
                fg_color="transparent",border_color="#FFCC70",border_width=2,command = b12_gui)
b12.grid(row = 0, column = 2, pady = 5, sticky = W, padx = 174 )

root.mainloop()
