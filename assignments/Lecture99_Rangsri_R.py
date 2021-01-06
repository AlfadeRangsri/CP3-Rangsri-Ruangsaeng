from tkinter import *

def leftClickButton(event):
    hight = float(textHight.get())
    weight = float(textWeight.get())
    bmi = weight / ((hight/100)**2)
    if bmi > 30:
        labelResult.configure(text="อ้วนมาก")
    elif bmi >= 25:
        labelResult.configure(text="อ้วน")
    elif bmi >= 18.6:
        labelResult.configure(text="เหมาะสม")
    elif bmi < 18.6:
        labelResult.configure(text="ผอมเกินไป")

mainWindow = Tk()
labelHight = Label(mainWindow, text='Height')
labelHight.grid(row=0, column=0)
textHight = Entry(mainWindow)
textHight.grid(row=0, column=1)
labelunit = Label(mainWindow, text='CM').grid(row=0, column=2)

labelWeight = Label(mainWindow, text='Weight')
labelWeight.grid(row=1, column=0)
textWeight = Entry(mainWindow)
textWeight.grid(row=1, column=1)
labelunit2 = Label(mainWindow, text='KG').grid(row=1, column=2)

calculateButton = Button(mainWindow, text='Calculate')
calculateButton.grid(row=2, column=0)
calculateButton.bind("<Button-1>", leftClickButton)

labelResult = Label(mainWindow, text='BMI')
labelResult.grid(row=2, column=1)
mainWindow.mainloop()
