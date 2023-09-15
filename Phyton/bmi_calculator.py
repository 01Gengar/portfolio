# Body Mass Index calculator

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_label = Label(self.__mainwindow, text="Weight (kg):", borderwidth=2, relief=GROOVE)
        self.__weight_label.grid(row=0, column=0, sticky=E+W)
        self.__weight_value = Entry()
        self.__weight_value.grid(row=0, column=1)

        self.__height_label = Label(self.__mainwindow, text="Height (cm):", borderwidth=2, relief=GROOVE)
        self.__height_label.grid(row=1, column=0, sticky=E+W)
        self.__height_value = Entry()
        self.__height_value.grid(row=1, column=1)

        self.__result_title = Label(self.__mainwindow, text="Result:", borderwidth=2, relief=GROOVE)
        self.__result_title.grid(row=2, column=0, sticky=E + W)
        self.__result_text = Label(self.__mainwindow, text="", borderwidth=2, relief=GROOVE)
        self.__result_text.grid(row=2, column=1, sticky=E+W)

        self.__explanation_title = Label(self.__mainwindow, text="Explanation:", borderwidth=2, relief=GROOVE)
        self.__explanation_title.grid(row=3, column=0, sticky=E + W)
        self.__explanation_text = Label(self.__mainwindow, text="", borderwidth=2, relief=GROOVE)
        self.__explanation_text.grid(row=3, column=1, sticky=E+W)

        self.__calculate_button = Button(self.__mainwindow, text="Calculate", command=self.calculate_BMI,
                                         background="green", foreground="white")
        self.__calculate_button.grid(row=4, column=0)

        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop,
                                    background="red", foreground="white")
        self.__stop_button.grid(row=4, column=1)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get()) / 100
            if weight <= 0 or height <= 0:
                raise ValueError("positive")
        except ValueError as ve:
            if "positive" in str(ve):
                text = "positive"
            else:
                text = "numbers"
            self.__explanation_text.configure(text=f"Error: height and weight must be {text}.")
            self.reset_fields()
        else:
            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)
            self.__result_text.configure(text=bmi)
            if bmi > 25:
                self.__explanation_text.configure(text="You are overweight.")
            elif bmi >= 18.5:
                self.__explanation_text.configure(text="Your weight is normal.")
            else:
                self.__explanation_text.configure(text="You are underweight.")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
