from tkinter import *


class calculate():

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("290x260")

        self.root.maxsize(290, 260)
        self.root.minsize(290, 260)
        self.root.config(bg="grey")

        self.resultwindow = Entry(self.root,borderwidth=5, relief=SUNKEN)
        self.resultwindow.grid(row=0,column=0,columnspan=6,pady=5)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()  # Sets focus on the input text area

        # Buttons
        self.button1 = Button(self.root, text="1", width=3, command=lambda:self.ins('1'),relief=RAISED,bg='light green')
        self.button1.grid(row=1,column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(self.root, text="2", width=3, command=lambda:self.ins('2'),relief=RAISED,bg='light green')
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(self.root, text="3", width=3, command=lambda:self.ins('3'),relief=RAISED,bg='light green')
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(self.root, text="4", width=3, command=lambda:self.ins('4'),relief=RAISED,bg='light green')
        self.button4.grid(row=2, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(self.root, text="5", width=3, command=lambda:self.ins('5'),relief=RAISED,bg='light green')
        self.button5.grid(row=2, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(self.root, text="6", width=3, command=lambda:self.ins('6'),relief=RAISED,bg='light green')
        self.button6.grid(row=2, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(self.root, text="7", width=3, command=lambda:self.ins('7'),relief=RAISED,bg='light green')
        self.button7.grid(row=3, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(self.root, text="8", width=3, command=lambda:self.ins('8'),relief=RAISED,bg='light green')
        self.button8.grid(row=3, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(self.root, text="9", width=3, command=lambda:self.ins('9'),relief=RAISED,bg='light green')
        self.button9.grid(row=3, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="0", width=3, command=lambda: self.ins('0'),relief=RAISED,bg='light green')
        self.button0.grid(row=4, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button_open = Button(self.root, text="(", width=3, command=lambda: self.ins('('),relief=RAISED)
        self.button_open.grid(row=4, column=1, padx=3, pady=3)
        self.button_open.config(font=("Arial", 18))

        self.button_close = Button(self.root, text=")", width=3, command=lambda: self.ins(')'),relief=RAISED)
        self.button_close.grid(row=4, column=2, padx=3, pady=3)
        self.button_close.config(font=("Arial", 18))

        # Operations Buttons

        # ORIGINAL CODE:
        #        self.buttonplus = Button(self.root, text="+", width=3, command=lambda:self.ins('+'),relief=RAISED)
        # MODIFIED TO:
        self.buttonplus = Button(self.root, text="+", width=3, command=lambda:self.ins('='),relief=RAISED)
        self.buttonplus.grid(row=1,column=3,padx=3,pady=3)
        self.buttonplus.config(font=("Arial", 18))

        self.buttonminus = Button(self.root, text="-", width=3, command=lambda:self.ins('-'),relief=RAISED)
        self.buttonminus.grid(row=1, column=4, padx=3, pady=3)
        self.buttonminus.config(font=("Arial", 18))

        self.buttondivide = Button(self.root, text="/", width=3, command=lambda:self.ins('/'),relief=RAISED)
        self.buttondivide.grid(row=2, column=3, padx=3, pady=3)
        self.buttondivide.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="*", width=3, command=lambda:self.ins('*'),relief=RAISED)
        self.buttonmultiply.grid(row=2, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttoncancel = Button(self.root, text="C", width=3, command=lambda: self.cancel(),relief=RAISED,bg='#EF5350',fg='white')
        self.buttoncancel.grid(row=3, column=4, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))

        self.buttondeleteall = Button(self.root, text="Del", width=3, command=lambda: self.delete_all(),relief=RAISED)
        self.buttondeleteall.grid(row=3, column=3, padx=3, pady=3)
        self.buttondeleteall.config(font=("Arial", 18))

        self.buttonresult = Button(self.root, text="=", width=7, command=lambda:self.calculate(),relief=RAISED,bg='#FFEE58')
        self.buttonresult.grid(row=4, column=3, padx=3, pady=3, columnspan=2)
        self.buttonresult.config(font=("Arial", 18))

        self.root.after(500, self.run_tests)
        self.root.mainloop()

    def ins(self,val):
        self.resultwindow.insert(END, val)

    def cancel(self):
        self.resultwindow.delete(0, 'end')

    def delete_all(self):
        x = self.resultwindow.get()
        self.resultwindow.delete(0, 'end')
        y = x[:-1]
        self.resultwindow.insert(0, y)

    def calculate(self):
        x = self.resultwindow.get()
        answer = eval(x)
        self.resultwindow.delete(0, 'end')
        self.resultwindow.insert(0, answer)

    # Test cases:
    def test_MR1MTG1(self):
        print("SI [3+2=], FI [4+1=]")
        self.resultwindow.delete(0, 'end')
        self.button3.invoke()
        self.buttonplus.invoke()
        self.button2.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button4.invoke()
        self.buttonplus.invoke()
        self.button1.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Addition failed: got {SO} != {FO}"

    def test_MR1MTG2(self):
        print("SI [7-3=], FI [6-2=]")
        self.resultwindow.delete(0, 'end')
        self.button7.invoke()
        self.buttonminus.invoke()
        self.button3.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button6.invoke()
        self.buttonminus.invoke()
        self.button2.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Minus failed: got {SO} != {FO}"

    def test_MR1MTG3(self):
        print("SI [6*5=], FI [3*10=]")
        self.resultwindow.delete(0, 'end')
        self.button6.invoke()
        self.buttonmultiply.invoke()
        self.button5.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button3.invoke()
        self.buttonmultiply.invoke()
        self.button1.invoke()
        self.button0.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Multiplication failed: got {SO} != {FO}"

    def test_MR1MTG4(self):
        print("SI [30/3=], FI [100/10=]")
        self.resultwindow.delete(0, 'end')
        self.button3.invoke()
        self.button0.invoke()
        self.buttondivide.invoke()
        self.button3.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button0.invoke()
        self.button0.invoke()
        self.buttondivide.invoke()
        self.button1.invoke()
        self.button0.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Division failed: got {SO} != {FO}"

    def test_MR1MTG5(self):
        print("SI [5*(2+2)=], FI [5*2*2=]")
        self.resultwindow.delete(0, 'end')
        self.button5.invoke()
        self.buttonmultiply.invoke()
        self.button_open.invoke()
        self.button2.invoke()
        self.buttonplus.invoke()
        self.button2.invoke()
        self.button_close.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button5.invoke()
        self.buttonmultiply.invoke()
        self.button2.invoke()
        self.buttonmultiply.invoke()
        self.button2.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Test failed: got {SO} != {FO}"

    def test_MR2MTG1(self):
        print("SI [1], FI [0]")
        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button0.invoke()
        FO = self.resultwindow.get()

        assert SO != FO, f"1 and 0 failed: got {SO} == {FO}"

    def test_MR2MTG2(self):
        print("SI [11 Del], FI [12 Del]")
        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button1.invoke()
        self.buttondeleteall.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button2.invoke()
        self.buttondeleteall.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Del failed: got {SO} != {FO}"

    def test_MR2MTG3(self):
        print("SI [11 C], FI [22 C]")
        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button1.invoke()
        self.buttoncancel.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button2.invoke()
        self.button2.invoke()
        self.buttoncancel.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"C failed: got {SO} != {FO}"

    def test_MR2MTG4(self):
        print("SI [3+6=], FI [4+5=]")
        self.resultwindow.delete(0, 'end')
        self.button3.invoke()
        self.buttonplus.invoke()
        self.button6.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button4.invoke()
        self.buttonplus.invoke()
        self.button5.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Result failed: got {SO} != {FO}"

    def test_MR2MTG5(self):
        print("SI [11 Del + 3 =], FI [12 Del + 3 =]")
        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button1.invoke()
        self.buttondeleteall.invoke()
        self.buttonplus.invoke()
        self.button3.invoke()
        self.buttonresult.invoke()
        SO = self.resultwindow.get()

        self.resultwindow.delete(0, 'end')
        self.button1.invoke()
        self.button2.invoke()
        self.buttondeleteall.invoke()
        self.buttonplus.invoke()
        self.button3.invoke()
        self.buttonresult.invoke()
        FO = self.resultwindow.get()

        assert SO == FO, f"Del failed: got {SO} != {FO}"

    # Run tests
    def run_tests(self):
        print("Running calculator tests...\n")
        tests = [self.test_MR1MTG1, self.test_MR1MTG2, self.test_MR1MTG3, self.test_MR1MTG4, self.test_MR1MTG5, self.test_MR2MTG1, self.test_MR2MTG2, self.test_MR2MTG3, self.test_MR2MTG4, self.test_MR2MTG5]
        for test in tests:
            try:
                test()
            except AssertionError as e:
                print("Error", e, "\n")
            else:
                print("✓", test.__name__, "passed\n")

        print("\nAll tests done. Closing calculator.")
        self.root.destroy()

if __name__ == "__main__":
    calculate()

