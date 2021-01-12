import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import messagebox

class Kalkulator(object):
	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		self.valUsia = IntVar()
		self.valTinggi = IntVar()
		self.valBerat = IntVar()
		self.valStr = StringVar()
		

		self.fontstyle = "Helvetica 11 bold"
		
		self.title = Label(root, text="Aplikasi Hitung BMI", font="Helvetica 18 bold underline")
		self.title.pack()

		self.nama = Label(root, text="Nama", font=self.fontstyle)
		self.nama.place(x=25, y=60)
		self.entryNama = Entry(root, text="", width=30, textvariable=self.valStr)
		self.entryNama.place(x=150, y=61)

		self.kelamin = Label(root, text="Jenis Kelamin", font=self.fontstyle)
		self.kelamin.place(x=25, y=90)

		self.pilihLaki = Radiobutton(root, text="Laki-Laki", value=1, font=self.fontstyle)
		self.pilihLaki.place(x=150, y=90)
		self.pilihBini = Radiobutton(root, text="Perempuan", value=2, font=self.fontstyle)
		self.pilihBini.place(x=250, y=90)

		self.usia = Label(root, text="Usia", font=self.fontstyle)
		self.usia.place(x=25, y=120)
		self.spin1 = Spinbox(root, from_=0, to=100, width=5, textvariable=self.valUsia)
		self.spin1.place(x=150, y=120)
		self.tahun = Label(root, text="Tahun", font=self.fontstyle)
		self.tahun.place(x=200, y=120)

		self.tinggi = Label(root, text="Tinggi", font=self.fontstyle)
		self.tinggi.place(x=25, y=150)
		self.spin2 = Spinbox(root, from_=0, to=200, width=5, textvariable=self.valTinggi)
		self.spin2.place(x=150, y=150)
		self.cm = Label(root, text="Cm", font=self.fontstyle)
		self.cm.place(x=200, y=150)

		self.berat = Label(root, text="Berat", font=self.fontstyle)
		self.berat.place(x=25, y=180)
		self.spin3 = Spinbox(root, from_=0, to=150, width=5, textvariable=self.valBerat)
		self.spin3.place(x=150, y=180)
		self.tahun = Label(root, text="Kg", font=self.fontstyle)
		self.tahun.place(x=200, y=180)

		self.resetButton = Button(root, text="Reset", command=self.reset , width=20, font=self.fontstyle)
		self.resetButton.place(x=25, y=230)
		self.submitButton = Button(root, text="Submit", command=self.hitung , width=20, font=self.fontstyle)
		self.submitButton.place(x=190, y=230)

		self.hasilperhitungan = Label(root, text="Hasil Perhitungan", font="Helvetica 11 bold underline")
		self.hasilperhitungan.place(x=400, y=61)

		self.hasil = Label(root, text="0", font="Helvetica 50 bold")
		self.hasil.place(relx=0.77, rely=0.55, anchor=CENTER)

		self.bmi = Label(root, text="Normal BMI Range", font="Helvetica 11 bold")
		self.bmi.place(x=450, y=220)
		self.bmiAngka = Label(root, text="18.5 - 24.9", font="Helvetica 11 bold")
		self.bmiAngka.place(x=480, y=240)

		self.copyright = Label(root, text="copyright@19.83.0351 - Muhammad Ichwan")
		self.copyright.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

	def reset(self):
		self.valStr.set("")
		self.valUsia.set(0)
		self.valTinggi.set(0)
		self.valBerat.set(0)

	def hitung(self):
		valBerat = float(self.spin3.get())
		valTinggi = float(self.spin2.get())
		valNama = self.entryNama.get()

		try:
			hitungBMI = valBerat / (valTinggi / 100) ** 2
			self.hasil.configure(text=f"{hitungBMI}"[:5])
			if hitungBMI < 18.5:
				self.kurus = Label(root, text="Kurus", font="Helvetica 15 bold", fg="purple")
				self.kurus.place(x=490, y=120)
			elif hitungBMI < 24.9:
				self.ideal = Label(root, text="Ideal", font="Helvetica 15 bold", fg="green")
				self.ideal.place(x=490, y=120)
			elif hitungBMI < 29.9:
				self.gemuk = Label(root, text="Gemuk", font="Helvetica 15 bold", fg="orange")
				self.gemuk.place(x=490, y=120)
			else:
				self.obese = Label(root, text="Obese", font="Helvetica 15 bold", fg="red")
				self.obese.place(x=490, y=120)
				
		except:
			if valNama is "":
				print(messagebox.showerror("Error", "Nama tidak boleh kosong"))

			elif valTinggi == 0:
				print(messagebox.showerror("Error", "Tinggi Badan harus bernilai lebih dari 0"))


if __name__ == '__main__':
	root = tk.Tk()
	root.title('Kalkulator BMI Sederhana')
	Kalkulator(root)
	root.geometry("670x330")
	root.mainloop()