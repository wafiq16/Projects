import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter.messagebox

operator =""

root = Tk()
root.geometry("1548x800+0+0")
root.title("StartEOR")

#========================================FRAME=========================================================
#========================================FRAME=========================================================
#========================================FRAME=========================================================

MainFrame =Frame(root, bg="aliceblue", bd=2, relief=RIDGE)
MainFrame.pack(side=TOP)

UserInputFrame =Frame(MainFrame, bg="aliceblue", bd=0, padx=10, relief=RIDGE)
UserInputFrame.grid(row=0,column=0, sticky=NW)

PropFrame =Frame(UserInputFrame, bg="aliceblue", bd=0, padx=10, relief=RIDGE)
PropFrame.grid(row=0, sticky=NW)

ButtonsFrames =Frame(UserInputFrame, bg="aliceblue")
ButtonsFrames.grid(row=1,column=0, sticky=W)

ScreeningFrames =Frame(MainFrame, bg="aliceblue", bd=3, relief=GROOVE)
ScreeningFrames.grid(row=0,column=1, sticky=NSEW)

###style
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } }, # [left margin, upper margin, right margin, margin beetwen tab and frames]
        "TNotebook.Tab": {
			"configure": {
				"padding": [115, 10], # [space beetwen text and horizontal tab-button border, space between text and vertical tab_button border]
				"background": 'cyan4', #tab bg color
				"foreground": 'white', #font color
				"font" :("Times", 20, "bold"),  #font settings
			},
			"map": {
				"background": [("selected", 'VioletRed2')],  # Color of active tab
				"expand": [("selected", [1, 1, 1, 0])],  # [expanse of text]
			}}})

style.theme_use("MyStyle")
###

TabFrame = ttk.Notebook(ScreeningFrames)
Sum = Frame(TabFrame, bg="aliceblue")
Sum.pack(fill=BOTH)
Detail = Frame(TabFrame, bg="aliceblue")
Detail.pack(fill=BOTH)
WF = Frame(TabFrame, bg="aliceblue")
WF.pack(fill=BOTH)
TabFrame.add(Sum, text='Summary Screening')
TabFrame.add(Detail, text='Detail')
TabFrame.add(WF, text='Weight Factor')
TabFrame.grid()

List =Frame(Sum, bg="aliceblue")
List.grid(row=0,column=0, sticky=EW)
L1 = Frame(List, bg="aliceblue", bd=3, relief=GROOVE)
L1.grid(row=0, sticky=EW)
L11 = Frame(L1, bg="aliceblue", bd=3, relief=GROOVE)
L11.grid(row=0, sticky=EW)
L12 = Frame(L1, bg="aliceblue", bd=3, relief=GROOVE)
L12.grid(row=1, sticky=EW)
L2 = Frame(List, bg="aliceblue", bd=3, relief=GROOVE)
L2.grid(row=1, sticky=EW)
L21 = Frame(L2, bg="aliceblue", bd=3, relief=GROOVE)
L21.grid(row=0, sticky=EW)
L22 = Frame(L2, bg="aliceblue", bd=3, relief=GROOVE)
L22.grid(row=1, sticky=EW)
L3 = Frame(List, bg="aliceblue", bd=3, relief=GROOVE)
L3.grid(row=2, sticky=EW)
L31 = Frame(L3, bg="aliceblue", bd=3, relief=GROOVE)
L31.grid(row=0, sticky=EW)
L32 = Frame(L3, bg="aliceblue", bd=3, relief=GROOVE)
L32.grid(row=1, sticky=EW)
L4 = Frame(List, bg="aliceblue", bd=3, relief=GROOVE)
L4.grid(row=3, sticky=EW)
L41 = Frame(L4, bg="aliceblue", bd=3, relief=GROOVE)
L41.grid(row=0, sticky=EW)
L42 = Frame(L4, bg="aliceblue", bd=3, relief=GROOVE)
L42.grid(row=1, sticky=EW)
L5 = Frame(List, bg="aliceblue", bd=3, relief=GROOVE)
L5.grid(row=4, sticky=EW)
L51 = Frame(L5, bg="aliceblue", bd=3, relief=GROOVE)
L51.grid(row=0, sticky=EW)
L52 = Frame(L5, bg="aliceblue", bd=3, relief=GROOVE)
L52.grid(row=1, sticky=EW)

spiderradar =Frame(Sum, bg="aliceblue", bd=3, width=700, height=700, relief=GROOVE)
spiderradar.grid(row=0,column=1, sticky=W)

#====================================TEXT INPUT========================================================
#====================================TEXT INPUT========================================================
#====================================TEXT INPUT========================================================

text_Title = StringVar()
text_API = StringVar()
text_formation = StringVar()
text_ft = StringVar()
text_cp = StringVar()
text_thickness = StringVar()
text_degF = StringVar()
text_so = StringVar()
text_composition = StringVar()
text_md = StringVar()
text_por = StringVar()
score_MNit = StringVar()
score_MHyd = StringVar()
score_MCOO = StringVar()
score_MWAG = StringVar()
score_INit = StringVar()
score_IHyd = StringVar()
score_ICOO = StringVar()
score_IHWAG = StringVar()
score_Pol = StringVar()
score_ASP = StringVar()
score_SPA = StringVar()
score_Com = StringVar()
score_Ste = StringVar()
score_Hot = StringVar()
score_Mic = StringVar()

wf_api1 = StringVar()
wf_api2 = StringVar()
wf_api3 = StringVar()
wf_api4 = StringVar()
wf_api5 = StringVar()
wf_api6 = StringVar()
wf_api7 = StringVar()
wf_api8 = StringVar()
wf_api9 = StringVar()
wf_api10 = StringVar()
wf_api11 = StringVar()
wf_api12 = StringVar()
wf_api13 = StringVar()
wf_api14 = StringVar()
wf_api15 = StringVar()

wf_vis1 = StringVar()
wf_vis2 = StringVar()
wf_vis3 = StringVar()
wf_vis4 = StringVar()
wf_vis5 = StringVar()
wf_vis6 = StringVar()
wf_vis7 = StringVar()
wf_vis8 = StringVar()
wf_vis9 = StringVar()
wf_vis10 = StringVar()
wf_vis11 = StringVar()
wf_vis12 = StringVar()
wf_vis13 = StringVar()
wf_vis14 = StringVar()
wf_vis15 = StringVar()

wf_por1 = StringVar()
wf_por2 = StringVar()
wf_por3 = StringVar()
wf_por4 = StringVar()
wf_por5 = StringVar()
wf_por6 = StringVar()
wf_por7 = StringVar()
wf_por8 = StringVar()
wf_por9 = StringVar()
wf_por10 = StringVar()
wf_por11 = StringVar()
wf_por12 = StringVar()
wf_por13 = StringVar()
wf_por14 = StringVar()
wf_por15 = StringVar()

wf_sat1 = StringVar()
wf_sat2 = StringVar()
wf_sat3 = StringVar()
wf_sat4 = StringVar()
wf_sat5 = StringVar()
wf_sat6 = StringVar()
wf_sat7 = StringVar()
wf_sat8 = StringVar()
wf_sat9 = StringVar()
wf_sat10 = StringVar()
wf_sat11 = StringVar()
wf_sat12 = StringVar()
wf_sat13 = StringVar()
wf_sat14 = StringVar()
wf_sat15 = StringVar()

wf_for1 = StringVar()
wf_for2 = StringVar()
wf_for3 = StringVar()
wf_for4 = StringVar()
wf_for5 = StringVar()
wf_for6 = StringVar()
wf_for7 = StringVar()
wf_for8 = StringVar()
wf_for9 = StringVar()
wf_for10 = StringVar()
wf_for11 = StringVar()
wf_for12 = StringVar()
wf_for13 = StringVar()
wf_for14 = StringVar()
wf_for15 = StringVar()

wf_per1 = StringVar()
wf_per2 = StringVar()
wf_per3 = StringVar()
wf_per4 = StringVar()
wf_per5 = StringVar()
wf_per6 = StringVar()
wf_per7 = StringVar()
wf_per8 = StringVar()
wf_per9 = StringVar()
wf_per10 = StringVar()
wf_per11 = StringVar()
wf_per12 = StringVar()
wf_per13 = StringVar()
wf_per14 = StringVar()
wf_per15 = StringVar()

wf_thi1 = StringVar()
wf_thi2 = StringVar()
wf_thi3 = StringVar()
wf_thi4 = StringVar()
wf_thi5 = StringVar()
wf_thi6 = StringVar()
wf_thi7 = StringVar()
wf_thi8 = StringVar()
wf_thi9 = StringVar()
wf_thi10 = StringVar()
wf_thi11 = StringVar()
wf_thi12 = StringVar()
wf_thi13 = StringVar()
wf_thi14 = StringVar()
wf_thi15 = StringVar()

wf_dep1 = StringVar()
wf_dep2 = StringVar()
wf_dep3 = StringVar()
wf_dep4 = StringVar()
wf_dep5 = StringVar()
wf_dep6 = StringVar()
wf_dep7 = StringVar()
wf_dep8 = StringVar()
wf_dep9 = StringVar()
wf_dep10 = StringVar()
wf_dep11 = StringVar()
wf_dep12 = StringVar()
wf_dep13 = StringVar()
wf_dep14 = StringVar()
wf_dep15 = StringVar()

wf_tem1 = StringVar()
wf_tem2 = StringVar()
wf_tem3 = StringVar()
wf_tem4 = StringVar()
wf_tem5 = StringVar()
wf_tem6 = StringVar()
wf_tem7 = StringVar()
wf_tem8 = StringVar()
wf_tem9 = StringVar()
wf_tem10 = StringVar()
wf_tem11 = StringVar()
wf_tem12 = StringVar()
wf_tem13 = StringVar()
wf_tem14 = StringVar()
wf_tem15 = StringVar()

#=====================================CALCULATOR=======================================================
#=====================================CALCULATOR=======================================================
#=====================================CALCULATOR=======================================================

def ref():
	if 0 in (len(text_API.get()),
			  len(text_cp.get()),
			  len(text_so.get()),
			  len(text_por.get()),
			  len(text_md.get()),
			  len(text_ft.get()),
			  len(text_degF.get())
		 ):
		tkinter.messagebox.showinfo("Warning!", "Box is empty! Write something")
	else:

		APIMCO2 = float(text_API.get())
		if 22 <= APIMCO2 < 30:
			SAPIMC = 1/3 * float(wf_api1.get())
			d18.config(bg='green yellow')
		elif 30 <= APIMCO2 <= 37:
			SAPIMC = 2/3 * float(wf_api1.get())
			d18.config(bg='green2')
		elif 37 < APIMCO2 <= 45:
			SAPIMC = 1 * float(wf_api1.get())
			d18.config(bg='green4')
		else:
			SAPIMC = 0
			d18.config(bg='red')

		APIMHC = float(text_API.get())
		if 23 <= APIMHC < 35:
			SAPIMH = 1/3 * float(wf_api2.get())
			d19.config(bg='green yellow')
		elif 35 <= APIMHC <= 38.3:
			SAPIMH = 2/3 * float(wf_api2.get())
			d19.config(bg='green2')
		elif 38.3 < APIMHC <= 57:
			SAPIMH = 1 * float(wf_api2.get())
			d19.config(bg='green4')
		else:
			SAPIMH = 0
			d19.config(bg='red')

		APIMW = float(text_API.get())
		if 33 <= APIMW < 35:
			SAPIMW = 1/3 * float(wf_api3.get())
			d20.config(bg='green yellow')
		elif 35 <= APIMW <= 37:
			SAPIMW = 2/3 * float(wf_api3.get())
			d20.config(bg='green2')
		elif 37 < APIMW <= 39:
			SAPIMW = 1 * float(wf_api3.get())
			d20.config(bg='green4')
		else:
			SAPIMW = 0
			d20.config(bg='red')

		APIMN = float(text_API.get())
		if 35 <= APIMN < 39:
			SAPIMN = 1/3 * float(wf_api4.get())
			d21.config(bg='green yellow')
		elif 39 <= APIMN <= 47.6:
			SAPIMN = 2/3 * float(wf_api4.get())
			d21.config(bg='green2')
		elif 47.6 < APIMN <= 54:
			SAPIMN = 1 * float(wf_api4.get())
			d21.config(bg='green4')
		else:
			SAPIMN = 0
			d21.config(bg='red')

		APIIN = float(text_API.get())
		if 16 <= APIIN < 25:
			SAPIIN = 3/3 * float(wf_api5.get())
			d22.config(bg='green4')
		elif 25 <= APIIN <= 34.6:
			SAPIIN = 2/3 * float(wf_api5.get())
			d22.config(bg='green2')
		elif 34.6 < APIIN <= 54:
			SAPIIN = 1/3 * float(wf_api5.get())
			d22.config(bg='green yellow')
		else:
			SAPIIN = 0
			d22.config(bg='red')

		APIICO2 = float(text_API.get())
		if 11 <= APIICO2 < 20:
			SAPIIC = 3/3 * float(wf_api6.get())
			d23.config(bg='green4')
		elif 20 <= APIICO2 <= 24:
			SAPIIC = 2/3 * float(wf_api6.get())
			d23.config(bg='green2')
		elif 24 < APIICO2 <= 35:
			SAPIIC = 1/3 * float(wf_api6.get())
			d23.config(bg='green yellow')
		else:
			SAPIIC = 0
			d23.config(bg='red')

		APIIH = float(text_API.get())
		if 22 <= APIIH < 24:
			SAPIIH = 3/3 * float(wf_api7.get())
			d24.config(bg='green4')
		elif 24 <= APIIH <= 35:
			SAPIIH = 2/3 * float(wf_api7.get())
			d24.config(bg='green2')
		elif 35 < APIIH <= 48:
			SAPIIH = 1/3 * float(wf_api7.get())
			d24.config(bg='green yellow')
		else:
			SAPIIH = 0
			d24.config(bg='red')

		APIIHW = float(text_API.get())
		if 9.3 <= APIIHW < 24:
			SAPIIHW = 3/3 * float(wf_api8.get())
			d25.config(bg='green4')
		elif 24 <= APIIHW <= 31:
			SAPIIHW = 2/3 * float(wf_api8.get())
			d25.config(bg='green2')
		elif 31 < APIIHW <= 41:
			SAPIIHW = 1/3 * float(wf_api8.get())
			d25.config(bg='green yellow')
		else:
			SAPIIHW = 0
			d25.config(bg='red')

		APIP = float(text_API.get())
		if 13 <= APIP < 24:
			SAPIP = 1/3 * float(wf_api9.get())
			d26.config(bg='green yellow')
		elif 24 <= APIP <= 35:
			SAPIP = 2/3 * float(wf_api9.get())
			d26.config(bg='green2')
		elif 35 < APIP <= 42.5:
			SAPIP = 3/3 * float(wf_api9.get())
			d26.config(bg='green4')
		else:
			SAPIP = 0
			d26.config(bg='red')

		APIASP = float(text_API.get())
		if 20 <= APIASP < 24:
			SAPIASP = 1/3 * float(wf_api10.get())
			d27.config(bg='green yellow')
		elif 24 <= APIASP <= 32.6:
			SAPIASP = 2/3 * float(wf_api10.get())
			d27.config(bg='green2')
		elif 32.6 < APIASP <= 35:
			SAPIASP = 3/3 * float(wf_api10.get())
			d27.config(bg='green4')
		else:
			SAPIASP = 0
			d27.config(bg='red')

		APISPA = float(text_API.get())
		if 22 <= APISPA < 24:
			SAPISPA = 1/3 * float(wf_api11.get())
			d28.config(bg='green yellow')
		elif 24 <= APISPA <= 31:
			SAPISPA = 2/3 * float(wf_api11.get())
			d28.config(bg='green2')
		elif 31 < APISPA <= 39:
			SAPISPA = 3/3 * float(wf_api11.get())
			d28.config(bg='green4')
		else:
			SAPISPA = 0
			d28.config(bg='red')

		APIC = float(text_API.get())
		if 10 <= APIC < 23.6:
			SAPIC = 3/3 * float(wf_api12.get())
			d29.config(bg='green4')
		elif 23.6 <= APIC <= 32:
			SAPIC = 2/3 * float(wf_api12.get())
			d29.config(bg='green2')
		elif 32 < APIC <= 38:
			SAPIC = 1/3 * float(wf_api12.get())
			d29.config(bg='green yellow')
		else:
			SAPIC = 0
			d29.config(bg='red')

		APIST = float(text_API.get())
		if 8 <= APIST < 14.5:
			SAPIST = 3/3 * float(wf_api13.get())
			d30.config(bg='green4')
		elif 14.5 <= APIST <= 24:
			SAPIST = 2/3 * float(wf_api13.get())
			d30.config(bg='green2')
		elif 24 < APIST <= 30:
			SAPIST = 1/3 * float(wf_api13.get())
			d30.config(bg='green yellow')
		else:
			SAPIST = 0
			d30.config(bg='red')

		APIHOT = float(text_API.get())
		if 12 <= APIHOT < 18.6:
			SAPIHOT = 3/3 * float(wf_api14.get())
			d31.config(bg='green4')
		elif 18.6 <= APIHOT <= 22:
			SAPIHOT = 2/3 * float(wf_api14.get())
			d31.config(bg='green2')
		elif 22 < APIHOT <= 25:
			SAPIHOT = 1/3 * float(wf_api14.get())
			d31.config(bg='green yellow')
		else:
			SAPIHOT = 0
			d31.config(bg='red')

		APIMIC = float(text_API.get())
		if 12 <= APIMIC < 20:
			SAPIMIC = 1/3 * float(wf_api15.get())
			d32.config(bg='green yellow')
		elif 20 <= APIMIC <= 26.6:
			SAPIMIC = 2/3 * float(wf_api15.get())
			d32.config(bg='green2')
		elif 26.6 < APIMIC <= 33:
			SAPIMIC = 3/3 * float(wf_api15.get())
			d32.config(bg='green4')
		else:
			SAPIMIC = 0
			d32.config(bg='red')

		VISMCO2 = float(text_cp.get())
		if 0 <= VISMCO2 < 2.1:
			SVISMC = 3 / 3 * float(wf_vis1.get())
			d34.config(bg='green yellow')
		elif 2.1 <= VISMCO2 <= 15:
			SVISMC = 2 / 3 * float(wf_vis1.get())
			d34.config(bg='green2')
		elif 15 < VISMCO2 <= 35:
			SVISMC = 1 / 3 * float(wf_vis1.get())
			d34.config(bg='green4')
		else:
			SVISMC = 0
			d34.config(bg='red')

		VISMHC = float(text_cp.get())
		if 0.04 <= VISMHC < 200:
			SVISMH = 3 / 3 * float(wf_vis2.get())
			d35.config(bg='green4')
		elif 200 <= VISMHC <= 1000:
			SVISMH = 2 / 3 * float(wf_vis2.get())
			d35.config(bg='green2')
		elif 1000 < VISMHC <= 18000:
			SVISMH = 1 / 3 * float(wf_vis2.get())
			d35.config(bg='green yellow')
		else:
			SVISMH = 0
			d35.config(bg='red')

		VISMW = float(text_cp.get())
		if 0.07 <= VISMW < 0.1:
			SVISMW = 3 / 3 * float(wf_vis3.get())
			d36.config(bg='green4')
		elif 0.1 <= VISMW <= 0.2:
			SVISMW = 2 / 3 * float(wf_vis3.get())
			d36.config(bg='green2')
		elif 0.2 < VISMW <= 0.4:
			SVISMW = 1 / 3 * float(wf_vis3.get())
			d36.config(bg='green yellow')
		else:
			SVISMW = 0
			d36.config(bg='red')

		VISMN = float(text_cp.get())
		if 0 <= VISMN < 0.07:
			SVISMN = 3 / 3 * float(wf_vis4.get())
			d37.config(bg='green4')
		elif 0.07 <= VISMN <= 0.1:
			SVISMN = 2 / 3 * float(wf_vis4.get())
			d37.config(bg='green2')
		elif 0.1 < VISMN <= 0.2:
			SVISMN = 1 / 3 * float(wf_vis4.get())
			d37.config(bg='green yellow')
		else:
			SVISMN = 0
			d37.config(bg='red')

		VISIN = float(text_cp.get())
		if 0 <= VISIN < 2256.8:
			SVISIN = 3 / 3 * float(wf_vis5.get())
			d38.config(bg='green4')
		elif 2256.8 <= VISIN <= 10000:
			SVISIN = 2 / 3 * float(wf_vis5.get())
			d38.config(bg='green2')
		elif 10000 < VISIN <= 18000:
			SVISIN = 1 / 3 * float(wf_vis5.get())
			d38.config(bg='green yellow')
		else:
			SVISIN = 0
			d38.config(bg='red')

		VISICO2 = float(text_cp.get())
		if 0.6 <= VISICO2 < 65.5:
			SVISIC = 3 / 3 * float(wf_vis6.get())
			d39.config(bg='green4')
		elif 65.5 <= VISICO2 <= 200:
			SVISIC = 2 / 3 * float(wf_vis6.get())
			d39.config(bg='green2')
		elif 200 < VISICO2 <= 592:
			SVISIC = 1 / 3 * float(wf_vis6.get())
			d39.config(bg='green yellow')
		else:
			SVISIC = 0
			d39.config(bg='red')

		VISIH = float(text_cp.get())
		if 0.25 <= VISIH < 2:
			SVISIH = 3 / 3 * float(wf_vis7.get())
			d40.config(bg='green4')
		elif 2 <= VISIH <= 3:
			SVISIH = 2 / 3 * float(wf_vis7.get())
			d40.config(bg='green2')
		elif 3 < VISIH <= 4:
			SVISIH = 1 / 3 * float(wf_vis7.get())
			d40.config(bg='green yellow')
		else:
			SVISIH = 0
			d40.config(bg='red')

		VISIHW = float(text_cp.get())
		if 0.17 <= VISIHW < 3000:
			SVISIHW = 3 / 3 * float(wf_vis8.get())
			d41.config(bg='green4')
		elif 3000 <= VISIHW <= 10000:
			SVISIHW = 2 / 3 * float(wf_vis8.get())
			d41.config(bg='green2')
		elif 10000 < VISIHW <= 16000:
			SVISIHW = 1 / 3 * float(wf_vis8.get())
			d41.config(bg='green yellow')
		else:
			SVISIHW = 0
			d41.config(bg='red')

		VISP = float(text_cp.get())
		if 0.4 <= VISP < 100:
			SVISP = 3 / 3 * float(wf_vis9.get())
			d42.config(bg='green4')
		elif 100 <= VISP <= 1000:
			SVISP = 2 / 3 * float(wf_vis9.get())
			d42.config(bg='green2')
		elif 1000 < VISP <= 4000:
			SVISP = 1 / 3 * float(wf_vis9.get())
			d42.config(bg='green yellow')
		else:
			SVISP = 0
			d42.config(bg='red')

		VISASP = float(text_cp.get())
		if 11 <= VISASP < 200:
			SVISASP = 3 / 3 * float(wf_vis10.get())
			d43.config(bg='green4')
		elif 200 <= VISASP <= 1000:
			SVISASP = 2 / 3 * float(wf_vis10.get())
			d43.config(bg='green2')
		elif 1000 < VISASP <= 6500:
			SVISASP = 1 / 3 * float(wf_vis10.get())
			d43.config(bg='green yellow')
		else:
			SVISASP = 0
			d43.config(bg='red')

		VISSPA = float(text_cp.get())
		if 3 <= VISSPA < 9:
			SVISSPA = 3 / 3 * float(wf_vis11.get())
			d44.config(bg='green4')
		elif 9 <= VISSPA <= 11:
			SVISSPA = 2 / 3 * float(wf_vis11.get())
			d44.config(bg='green2')
		elif 11 < VISSPA <= 15.6:
			SVISSPA = 1 / 3 * float(wf_vis11.get())
			d44.config(bg='green yellow')
		else:
			SVISSPA = 0
			d44.config(bg='red')

		VISC = float(text_cp.get())
		if 1000 <= VISC < 1200:
			SVISC = 3 / 3 * float(wf_vis12.get())
			d45.config(bg='green4')
		elif 1200 <= VISC <= 2500:
			SVISC = 2 / 3 * float(wf_vis12.get())
			d45.config(bg='green2')
		elif 2500 < VISC <= 5000:
			SVISC = 1 / 3 * float(wf_vis12.get())
			d45.config(bg='green yellow')
		else:
			SVISC = 0
			d45.config(bg='red')
			e31.config(foreground="red")

		VISST = float(text_cp.get())
		if 10 <= VISST < 1000:
			SVISST = 3 / 3 * float(wf_vis13.get())
			d46.config(bg='green4')
		elif 1000 <= VISST <= 32971.3:
			SVISST = 2 / 3 * float(wf_vis13.get())
			d46.config(bg='green2')
		elif 32971.3 < VISST <= 5000000:
			SVISST = 1 / 3 * float(wf_vis13.get())
			d46.config(bg='green yellow')
		else:
			SVISST = 0
			d46.config(bg='red')
			e32.config(foreground="red")

		VISHOT = float(text_cp.get())
		if 170 <= VISHOT < 2002:
			SVISHOT = 3 / 3 * float(wf_vis14.get())
			d47.config(bg='green4')
		elif 2002 <= VISHOT <= 5000:
			SVISHOT = 2 / 3 * float(wf_vis14.get())
			d47.config(bg='green2')
		elif 5000 < VISHOT <= 8000:
			SVISHOT = 1 / 3 * float(wf_vis14.get())
			d47.config(bg='green yellow')
		else:
			SVISHOT = 0
			d47.config(bg='red')
			e33.config(foreground="red")

		VISMIC = float(text_cp.get())
		if 1.7 <= VISMIC < 1000:
			SVISMIC = 3 / 3 * float(wf_vis15.get())
			d48.config(bg='green4')
		elif 1000 <= VISMIC <= 3000:
			SVISMIC = 2 / 3 * float(wf_vis15.get())
			d48.config(bg='green2')
		elif 3000 < VISMIC <= 8900:
			SVISMIC = 1 / 3 * float(wf_vis15.get())
			d48.config(bg='green yellow')
		else:
			SVISMIC = 0
			d48.config(bg='red')

		PORMCO2 = float(text_por.get())
		if 3 <= PORMCO2 < 10:
			SPORMC = 1 * float(wf_por1.get())
			d50.config(bg='green yellow')
		elif 10 <= PORMCO2 <= 25:
			SPORMC = 1 * float(wf_por1.get())
			d50.config(bg='green2')
		elif 25 < PORMCO2 <= 37:
			SPORMC = 1 * float(wf_por1.get())
			d50.config(bg='green4')
		else:
			SPORMC = 0
			d50.config(bg='red')

		PORMHC = float(text_por.get())
		if 4.25 <= PORMHC < 15:
			SPORMH = 1 * float(wf_por2.get())
			d51.config(bg='green yellow')
		elif 15 <= PORMHC <= 25:
			SPORMH = 1 * float(wf_por2.get())
			d51.config(bg='green2')
		elif 25 < PORMHC <= 45:
			SPORMH = 1 * float(wf_por2.get())
			d51.config(bg='green4')
		else:
			SPORMH = 0
			d51.config(bg='red')

		PORMW = float(text_por.get())
		if 11 <= PORMW < 15:
			SPORMW = 1 * float(wf_por3.get())
			d52.config(bg='green yellow')
		elif 15 <= PORMW <= 20:
			SPORMW = 1 * float(wf_por3.get())
			d52.config(bg='green2')
		elif 10 < PORMW <= 24:
			SPORMW = 1 * float(wf_por3.get())
			d52.config(bg='green4')
		else:
			SPORMW = 0
			d52.config(bg='red')

		PORMN = float(text_por.get())
		if 7.5 <= PORMN < 10:
			SPORMN = 1 * float(wf_por4.get())
			d53.config(bg='green yellow')
		elif 10 <= PORMN <= 11.2:
			SPORMN = 1 * float(wf_por4.get())
			d53.config(bg='green2')
		elif 11.2 < PORMN <= 14:
			SPORMN = 1 * float(wf_por4.get())
			d53.config(bg='green4')
		else:
			SPORMN = 0
			d53.config(bg='red')

		PORIN = float(text_por.get())
		if 11 <= PORIN < 15:
			SPORIN = 1 * float(wf_por5.get())
			d54.config(bg='green yellow')
		elif 15 <= PORIN <= 20:
			SPORIN = 1 * float(wf_por5.get())
			d54.config(bg='green2')
		elif 20 < PORIN <= 28:
			SPORIN = 1 * float(wf_por5.get())
			d54.config(bg='green4')
		else:
			SPORIN = 0
			d54.config(bg='red')

		PORICO2 = float(text_por.get())
		if 17 <= PORICO2 < 20:
			SPORIC = 1 * float(wf_por6.get())
			d55.config(bg='green yellow')
		elif 20 <= PORICO2 <= 25:
			SPORIC = 1 * float(wf_por6.get())
			d55.config(bg='green2')
		elif 25 < PORICO2 <= 32:
			SPORIC = 1 * float(wf_por6.get())
			d55.config(bg='green4')
		else:
			SPORIC = 0
			d55.config(bg='red')

		PORIH = float(text_por.get())
		if 5 <= PORIH < 10:
			SPORIH = 1 * float(wf_por7.get())
			d56.config(bg='green yellow')
		elif 10 <= PORIH <= 15:
			SPORIH = 1 * float(wf_por7.get())
			d56.config(bg='green2')
		elif 15 < PORIH <= 22:
			SPORIH = 1 * float(wf_por7.get())
			d56.config(bg='green4')
		else:
			SPORIH = 0
			d56.config(bg='red')

		PORIHW = float(text_por.get())
		if 18 <= PORIHW < 20:
			SPORIHW = 1 * float(wf_por8.get())
			d57.config(bg='green yellow')
		elif 20 <= PORIHW <= 25:
			SPORIHW = 1 * float(wf_por8.get())
			d57.config(bg='green2')
		elif 25 < PORIHW <= 31.9:
			SPORIHW = 1 * float(wf_por8.get())
			d57.config(bg='green4')
		else:
			SPORIHW = 0
			d57.config(bg='red')

		PORP = float(text_por.get())
		if 10.4 <= PORP < 15:
			SPORP = 1 * float(wf_por9.get())
			d58.config(bg='green yellow')
		elif 15 <= PORP <= 25:
			SPORP = 1 * float(wf_por9.get())
			d58.config(bg='green2')
		elif 25 < PORP <= 33:
			SPORP = 1 * float(wf_por9.get())
			d58.config(bg='green4')
		else:
			SPORP = 0
			d58.config(bg='red')

		PORASP = float(text_por.get())
		if 26 <= PORASP < 28:
			SPORASP = 1 * float(wf_por10.get())
			d59.config(bg='green yellow')
		elif 28 <= PORASP <= 30:
			SPORASP = 1 * float(wf_por10.get())
			d59.config(bg='green2')
		elif 30 < PORASP <= 32:
			SPORASP = 1 * float(wf_por10.get())
			d59.config(bg='green4')
		else:
			SPORASP = 0
			d59.config(bg='red')

		PORSPA = float(text_por.get())
		if 16 <= PORSPA < 16.2:
			SPORSPA = 1 * float(wf_por11.get())
			d60.config(bg='green yellow')
		elif 16.2 <= PORSPA <= 16.4:
			SPORSPA = 1 * float(wf_por11.get())
			d60.config(bg='green2')
		elif 16.4 < PORSPA <= 16.8:
			SPORSPA = 1 * float(wf_por11.get())
			d60.config(bg='green4')
		else:
			SPORSPA = 0
			d60.config(bg='red')

		PORC = float(text_por.get())
		if 14 <= PORC < 20:
			SPORC = 1 * float(wf_por12.get())
			d61.config(bg='green yellow')
		elif 20 <= PORC <= 25:
			SPORC = 1 * float(wf_por12.get())
			d61.config(bg='green2')
		elif 25 < PORC <= 35:
			SPORC = 1 * float(wf_por12.get())
			d61.config(bg='green4')
		else:
			SPORC = 0
			d61.config(bg='red')

		PORST = float(text_por.get())
		if 12 <= PORST < 25:
			SPORST = 1 * float(wf_por13.get())
			d62.config(bg='green yellow')
		elif 25 <= PORST <= 40:
			SPORST = 1 * float(wf_por13.get())
			d62.config(bg='green2')
		elif 40 < PORST <= 65:
			SPORST = 1 * float(wf_por13.get())
			d62.config(bg='green4')
		else:
			SPORST = 0
			d62.config(bg='red')

		PORHOT = float(text_por.get())
		if 25 <= PORHOT < 30:
			SPORHOT = 1 * float(wf_por14.get())
			d63.config(bg='green yellow')
		elif 30 <= PORHOT <= 35:
			SPORHOT = 1 * float(wf_por14.get())
			d63.config(bg='green2')
		elif 35 < PORHOT <= 37:
			SPORHOT = 1 * float(wf_por14.get())
			d63.config(bg='green4')
		else:
			SPORHOT = 0
			d63.config(bg='red')

		PORMIC = float(text_por.get())
		if 12 <= PORMIC < 19:
			SPORMIC = 1 * float(wf_por15.get())
			d64.config(bg='green yellow')
		elif 19 <= PORMIC <= 23:
			SPORMIC = 1 * float(wf_por15.get())
			d64.config(bg='green2')
		elif 23 < PORMIC <= 26:
			SPORMIC = 1 * float(wf_por15.get())
			d64.config(bg='green4')
		else:
			SPORMIC = 0
			d64.config(bg='red')

		SATMCO2 = float(text_so.get())
		if 15 <= SATMCO2 < 30:
			SSATMC = 1 * float(wf_sat1.get())
			d66.config(bg='green yellow')
		elif 30 <= SATMCO2 <= 46:
			SSATMC = 1 * float(wf_sat1.get())
			d66.config(bg='green2')
		elif 46 < SATMCO2 <= 89:
			SSATMC = 1 * float(wf_sat1.get())
			d66.config(bg='green4')
		else:
			SSATMC = 0
			d66.config(bg='red')

		SATMHC = float(text_so.get())
		if 30 <= SATMHC < 50:
			SSATMH = 1 * float(wf_sat2.get())
			d67.config(bg='green yellow')
		elif 50 <= SATMHC <= 75:
			SSATMH = 1 * float(wf_sat2.get())
			d67.config(bg='green2')
		elif 75 < SATMHC <= 98:
			SSATMH = 1 * float(wf_sat2.get())
			d67.config(bg='green4')
		else:
			SSATMH = 0
			d67.config(bg='red')

		SATMW = float(text_so.get())
		if 40 <= SATMW < 50:
			SSATMW = 1 * float(wf_sat3.get())
			d68.config(bg='green yellow')
		elif 50 <= SATMW <= 75:
			SSATMW = 1 * float(wf_sat3.get())
			d68.config(bg='green2')
		elif 75 < SATMW <= 80:
			SSATMW = 1 * float(wf_sat3.get())
			d68.config(bg='green4')
		else:
			SSATMW = 0
			d68.config(bg='red')

		SATMN = float(text_so.get())
		if 40 <= SATMN < 60:
			SSATMN = 1 * float(wf_sat4.get())
			d69.config(bg='green yellow')
		elif 60 <= SATMN <= 70:
			SSATMN = 1 * float(wf_sat4.get())
			d69.config(bg='green2')
		elif 70 < SATMN <= 80:
			SSATMN = 1 * float(wf_sat4.get())
			d69.config(bg='green4')
		else:
			SSATMN = 0
			d69.config(bg='red')

		SATIN = float(text_so.get())
		if 47 <= SATIN < 50:
			SSATIN = 1 * float(wf_sat5.get())
			d70.config(bg='green yellow')
		elif 50 <= SATIN <= 71:
			SSATIN = 1 * float(wf_sat5.get())
			d70.config(bg='green2')
		elif 71 < SATIN <= 98.5:
			SSATIN = 1 * float(wf_sat5.get())
			d70.config(bg='green4')
		else:
			SSATIN = 0
			d70.config(bg='red')

		SATICO2 = float(text_so.get())
		if 42 <= SATICO2 < 50:
			SSATIC = 1 * float(wf_sat6.get())
			d71.config(bg='green yellow')
		elif 50 <= SATICO2 <= 60:
			SSATIC = 1 * float(wf_sat6.get())
			d71.config(bg='green2')
		elif 60 < SATICO2 <= 78:
			SSATIC = 1 * float(wf_sat6.get())
			d71.config(bg='green4')
		else:
			SSATIC = 0
			d71.config(bg='red')

		SATIH = float(text_so.get())
		if 75 <= SATIH < 78:
			SSATIH = 1 * float(wf_sat7.get())
			d72.config(bg='green yellow')
		elif 78 <= SATIH <= 80:
			SSATIH = 1 * float(wf_sat7.get())
			d72.config(bg='green2')
		elif 80 < SATIH <= 83:
			SSATIH = 1 * float(wf_sat7.get())
			d72.config(bg='green4')
		else:
			SSATIH = 0
			d72.config(bg='red')

		SATIHW = float(text_so.get())
		if 35 <= SATIHW < 60:
			SSATIHW = 1 * float(wf_sat8.get())
			d73.config(bg='green yellow')
		elif 60 <= SATIHW <= 72:
			SSATIHW = 1 * float(wf_sat8.get())
			d73.config(bg='green2')
		elif 72 < SATIHW <= 83:
			SSATIHW = 1 * float(wf_sat8.get())
			d73.config(bg='green4')
		else:
			SSATIHW = 0
			d73.config(bg='red')

		SATP = float(text_so.get())
		if 34 <= SATP < 50:
			SSATP = 1 * float(wf_sat9.get())
			d74.config(bg='green yellow')
		elif 50 <= SATP <= 70:
			SSATP = 1 * float(wf_sat9.get())
			d74.config(bg='green2')
		elif 70 < SATP <= 82:
			SSATP = 1 * float(wf_sat9.get())
			d74.config(bg='green4')
		else:
			SSATP = 0
			d74.config(bg='red')

		SATASP = float(text_so.get())
		if 35 <= SATASP < 45:
			SSATASP = 1 * float(wf_sat10.get())
			d75.config(bg='green yellow')
		elif 45 <= SATASP <= 63.7:
			SSATASP = 1 * float(wf_sat10.get())
			d75.config(bg='green2')
		elif 63.7 < SATASP <= 74.8:
			SSATASP = 1 * float(wf_sat10.get())
			d75.config(bg='green4')
		else:
			SSATASP = 0
			d75.config(bg='red')

		SATSPA = float(text_so.get())
		if 43.5 <= SATSPA < 45:
			SSATSPA = 1 * float(wf_sat11.get())
			d76.config(bg='green yellow')
		elif 45 <= SATSPA <= 48:
			SSATSPA = 1 * float(wf_sat11.get())
			d76.config(bg='green2')
		elif 48 < SATSPA <= 53:
			SSATSPA = 1 * float(wf_sat11.get())
			d76.config(bg='green4')
		else:
			SSATSPA = 0
			d76.config(bg='red')

		SATC = float(text_so.get())
		if 50 <= SATC < 60:
			SSATC = 1 * float(wf_sat12.get())
			d77.config(bg='green yellow')
		elif 60 <= SATC <= 70:
			SSATC = 1 * float(wf_sat12.get())
			d77.config(bg='green2')
		elif 70 < SATC <= 94:
			SSATC = 1 * float(wf_sat12.get())
			d77.config(bg='green4')
		else:
			SSATC = 0
			d77.config(bg='red')

		SATST = float(text_so.get())
		if 35 <= SATST < 50:
			SSATST = 1 * float(wf_sat13.get())
			d78.config(bg='green yellow')
		elif 50 <= SATST <= 70:
			SSATST = 1 * float(wf_sat13.get())
			d78.config(bg='green2')
		elif 70 < SATST <= 90:
			SSATST = 1 * float(wf_sat13.get())
			d78.config(bg='green4')
		else:
			SSATST = 0
			d78.config(bg='red')

		SATHOT = float(text_so.get())
		if 15 <= SATHOT < 30:
			SSATHOT = 1 * float(wf_sat14.get())
			d79.config(bg='green yellow')
		elif 30 <= SATHOT <= 63:
			SSATHOT = 1 * float(wf_sat14.get())
			d79.config(bg='green2')
		elif 63 < SATHOT <= 85:
			SSATHOT = 1 * float(wf_sat14.get())
			d79.config(bg='green4')
		else:
			SSATHOT = 0
			d79.config(bg='red')

		SATMIC = float(text_so.get())
		if 55 <= SATMIC < 57:
			SSATMIC = 1 * float(wf_sat15.get())
			d80.config(bg='green yellow')
		elif 57 <= SATMIC <= 61:
			SSATMIC = 1 * float(wf_sat15.get())
			d80.config(bg='green2')
		elif 61 < SATMIC <= 65:
			SSATMIC = 1 * float(wf_sat15.get())
			d80.config(bg='green4')
		else:
			SSATMIC = 0
			d80.config(bg='red')

		PERMCO2 = float(text_md.get())
		if 1.5 <= PERMCO2 < 50:
			SPERMC = 1/3 * float(wf_per1.get())
			d98.config(bg='green yellow')
		elif 50 <= PERMCO2 <= 201.1:
			SPERMC = 2/3 * float(wf_per1.get())
			d98.config(bg='green2')
		elif 201.1 < PERMCO2 <= 4500:
			SPERMC = 3/3 * float(wf_per1.get())
			d98.config(bg='green4')
		else:
			SPERMC = 0
			d98.config(bg='red')

		PERMHC = float(text_md.get())
		if 0.1 <= PERMHC < 250:
			SPERMH = 1/3 * float(wf_per2.get())
			d99.config(bg='green yellow')
		elif 250 <= PERMHC <= 1000:
			SPERMH = 2/3 * float(wf_per2.get())
			d99.config(bg='green2')
		elif 1000 < PERMHC <= 5000:
			SPERMH = 3/3 * float(wf_per2.get())
			d99.config(bg='green4')
		else:
			SPERMH = 0
			d99.config(bg='red')

		PERMW = float(text_md.get())
		if 130 <= PERMW < 140:
			SPERMW = 1/3 * float(wf_per3.get())
			d100.config(bg='green yellow')
		elif 140 <= PERMW <= 250:
			SPERMW = 2/3 * float(wf_per3.get())
			d100.config(bg='green2')
		elif 250 < PERMW <= 1000:
			SPERMW = 3/3 * float(wf_per3.get())
			d100.config(bg='green4')
		else:
			SPERMW = 0
			d100.config(bg='red')

		PERMN = float(text_md.get())
		if 0.2 <= PERMN < 10:
			SPERMN = 1/3 * float(wf_per4.get())
			d101.config(bg='green yellow')
		elif 10 <= PERMN <= 15:
			SPERMN = 2/3 * float(wf_per4.get())
			d101.config(bg='green2')
		elif 15 < PERMN <= 35:
			SPERMN = 3/3 * float(wf_per4.get())
			d101.config(bg='green4')
		else:
			SPERMN = 0
			d101.config(bg='red')

		PERIN = float(text_md.get())
		if 3 <= PERIN < 250:
			SPERIN = 1/3 * float(wf_per5.get())
			d102.config(bg='green yellow')
		elif 250 <= PERIN <= 1041.7:
			SPERIN = 2/3 * float(wf_per5.get())
			d102.config(bg='green2')
		elif 1041.7 < PERIN <= 2800:
			SPERIN = 3/3 * float(wf_per5.get())
			d102.config(bg='green4')
		else:
			SPERIN = 0
			d102.config(bg='red')

		PERICO2 = float(text_md.get())
		if 30 <= PERICO2 < 50:
			SPERIC = 1/3 * float(wf_per6.get())
			d103.config(bg='green yellow')
		elif 50 <= PERICO2 <= 217:
			SPERIC = 2/3 * float(wf_per6.get())
			d103.config(bg='green2')
		elif 217 < PERICO2 <= 1000:
			SPERIC = 3/3 * float(wf_per6.get())
			d103.config(bg='green4')
		else:
			SPERIC = 0
			d103.config(bg='red')

		PERIH = float(text_md.get())
		if 40 <= PERIH < 100:
			SPERIH = 1/3 * float(wf_per7.get())
			d104.config(bg='green yellow')
		elif 100 <= PERIH <= 520:
			SPERIH = 2/3 * float(wf_per7.get())
			d104.config(bg='green2')
		elif 520 < PERIH <= 1000:
			SPERIH = 3/3 * float(wf_per7.get())
			d104.config(bg='green4')
		else:
			SPERIH = 0
			d104.config(bg='red')

		PERIHW = float(text_md.get())
		if 100 <= PERIHW < 250:
			SPERIHW = 1/3 * float(wf_per8.get())
			d105.config(bg='green yellow')
		elif 250 <= PERIHW <= 2392:
			SPERIHW = 2/3 * float(wf_per8.get())
			d105.config(bg='green2')
		elif 2392 < PERIHW <= 6600:
			SPERIHW = 3/3 * float(wf_per8.get())
			d105.config(bg='green4')
		else:
			SPERIHW = 0
			d105.config(bg='red')

		PERP = float(text_md.get())
		if 1.8 <= PERP < 200:
			SPERP = 1/3 * float(wf_per9.get())
			d106.config(bg='green yellow')
		elif 200 <= PERP <= 1000:
			SPERP = 2/3 * float(wf_per9.get())
			d106.config(bg='green2')
			SPERP = 3/3 * float(wf_per9.get())
			d106.config(bg='green4')
		else:
			SPERP = 0
			d106.config(bg='red')

		PERASP = float(text_md.get())
		if 10 <= PERASP < 200:
			SPERASP = 1/3 * float(wf_per10.get())
			d107.config(bg='green yellow')
		elif 200 <= PERASP <= 700:
			SPERASP = 2/3 * float(wf_per10.get())
			d107.config(bg='green2')
		elif 700 < PERASP <= 1520:
			SPERASP = 3/3 * float(wf_per10.get())
			d107.config(bg='green4')
		else:
			SPERASP = 0
			d107.config(bg='red')

		PERSPA = float(text_md.get())
		if 50 <= PERSPA < 52:
			SPERSPA = 1/3 * float(wf_per11.get())
			d108.config(bg='green yellow')
		elif 52 <= PERSPA <= 55:
			SPERSPA = 2/3 * float(wf_per11.get())
			d108.config(bg='green2')
		elif 55 < PERSPA <= 60:
			SPERSPA = 3/3 * float(wf_per11.get())
			d108.config(bg='green4')
		else:
			SPERSPA = 0
			d108.config(bg='red')

		PERC = float(text_md.get())
		if 10 <= PERC < 1000:
			SPERC = 1/3 * float(wf_per12.get())
			d109.config(bg='green yellow')
		elif 1000 <= PERC <= 7000:
			SPERC = 2/3 * float(wf_per12.get())
			d109.config(bg='green2')
		elif 7000 < PERC <= 15000:
			SPERC = 3/3 * float(wf_per12.get())
			d109.config(bg='green4')
		else:
			SPERC = 0
			d109.config(bg='red')

		PERST = float(text_md.get())
		if 1 <= PERST < 1000:
			SPERST = 1/3 * float(wf_per13.get())
			d110.config(bg='green yellow')
		elif 1000 <= PERST <= 7000:
			SPERST = 2/3 * float(wf_per13.get())
			d110.config(bg='green2')
		elif 7000 < PERST <= 15000:
			SPERST = 3/3 * float(wf_per13.get())
			d110.config(bg='green4')
		else:
			SPERST = 0
			d110.config(bg='red')

		PERHOT = float(text_md.get())
		if 900 <= PERHOT < 2000:
			SPERHOT = 1/3 * float(wf_per14.get())
			d111.config(bg='green yellow')
		elif 2000 <= PERHOT <= 4000:
			SPERHOT = 2/3 * float(wf_per14.get())
			d111.config(bg='green2')
		elif 4000 < PERHOT <= 6000:
			SPERHOT = 3/3 * float(wf_per14.get())
			d111.config(bg='green4')
		else:
			SPERHOT = 0
			d111.config(bg='red')

		PERMIC = float(text_md.get())
		if 180 <= PERMIC < 185:
			SPERMIC = 1/3 * float(wf_per15.get())
			d112.config(bg='green yellow')
		elif 185 <= PERMIC <= 195:
			SPERMIC = 2/3 * float(wf_per15.get())
			d112.config(bg='green2')
		elif 195 < PERMIC <= 200:
			SPERMIC = 3/3 * float(wf_per15.get())
			d112.config(bg='green4')
		else:
			SPERMIC = 0
			d112.config(bg='red')

		DEPMCO2 = float(text_ft.get())
		if 1500 <= DEPMCO2 < 3000:
			SDEPMC = 1/3 * float(wf_dep1.get())
			d130.config(bg='green yellow')
		elif 3000 <= DEPMCO2 <= 6171.2:
			SDEPMC = 2/3 * float(wf_dep1.get())
			d130.config(bg='green2')
		elif 6171.2 < DEPMCO2 <= 13365:
			SDEPMC = 3/3 * float(wf_dep1.get())
			d130.config(bg='green4')
		else:
			SDEPMC = 0
			d130.config(bg='red')

		DEPMHC = float(text_ft.get())
		if 4000 <= DEPMHC < 8000:
			SDEPMH = 1/3 * float(wf_dep2.get())
			d131.config(bg='green yellow')
		elif 8000 <= DEPMHC <= 11000:
			SDEPMH = 2/3 * float(wf_dep2.get())
			d131.config(bg='green2')
		elif 11000 < DEPMHC <= 15900:
			SDEPMH = 3/3 * float(wf_dep2.get())
			d131.config(bg='green4')
		else:
			SDEPMH = 0
			d131.config(bg='red')

		DEPMW = float(text_ft.get())
		if 7545 <= DEPMW < 8000:
			SDEPMW = 1/3 * float(wf_dep3.get())
			d132.config(bg='green yellow')
		elif 8000 <= DEPMW <= 8500:
			SDEPMW = 2/3 * float(wf_dep3.get())
			d132.config(bg='green2')
		elif 8500 < DEPMW <= 8887:
			SDEPMW = 3/3 * float(wf_dep3.get())
			d132.config(bg='green4')
		else:
			SDEPMW = 0
			d132.config(bg='red')

		DEPMN = float(text_ft.get())
		if 6000 <= DEPMN < 8000:
			SDEPMN = 1/3 * float(wf_dep4.get())
			d133.config(bg='green yellow')
		elif 8000 <= DEPMN <= 14633.3:
			SDEPMN = 2/3 * float(wf_dep4.get())
			d133.config(bg='green2')
		elif 14633.3 < DEPMN <= 18500:
			SDEPMN = 3/3 * float(wf_dep4.get())
			d133.config(bg='green4')
		else:
			SDEPMN = 0
			d133.config(bg='red')

		DEPIN = float(text_ft.get())
		if 1700 <= DEPIN < 5000:
			SDEPIN = 1/3 * float(wf_dep5.get())
			d134.config(bg='green yellow')
		elif 5000 <= DEPIN <= 7914.2:
			SDEPIN = 2/3 * float(wf_dep5.get())
			d134.config(bg='green2')
		elif 7914.2 < DEPIN <= 18500:
			SDEPIN = 3/3 * float(wf_dep5.get())
			d134.config(bg='green4')
		else:
			SDEPIN = 0
			d134.config(bg='red')

		DEPICO2 = float(text_ft.get())
		if 1150 <= DEPICO2 < 3000:
			SDEPIC = 1/3 * float(wf_dep6.get())
			d135.config(bg='green yellow')
		elif 3000 <= DEPICO2 <= 5000:
			SDEPIC = 2/3 * float(wf_dep6.get())
			d135.config(bg='green2')
		elif 5000 < DEPICO2 <= 8500:
			SDEPIC = 3/3 * float(wf_dep6.get())
			d135.config(bg='green4')
		else:
			SDEPIC = 0
			d135.config(bg='red')

		DEPIH = float(text_ft.get())
		if 6000 <= DEPIH < 6250:
			SDEPIH = 1/3 * float(wf_dep7.get())
			d136.config(bg='green yellow')
		elif 6250 <= DEPIH <= 6500:
			SDEPIH = 2/3 * float(wf_dep7.get())
			d136.config(bg='green2')
		elif 6500 < DEPIH <= 7000:
			SDEPIH = 3/3 * float(wf_dep7.get())
			d136.config(bg='green4')
		else:
			SDEPIH = 0
			d136.config(bg='red')

		DEPIHW = float(text_ft.get())
		if 2650 <= DEPIHW < 5000:
			SDEPIHW = 1/3 * float(wf_dep8.get())
			d137.config(bg='green yellow')
		elif 5000 <= DEPIHW <= 7218.71:
			SDEPIHW = 2/3 * float(wf_dep8.get())
			d137.config(bg='green2')
		elif 7218.71 < DEPIHW <= 9199:
			SDEPIHW = 3/3 * float(wf_dep8.get())
			d137.config(bg='green4')
		else:
			SDEPIHW = 0
			d137.config(bg='red')

		DEPP = float(text_ft.get())
		if 700 <= DEPP < 4000:
			SDEPP = 3/3 * float(wf_dep9.get())
			d138.config(bg='green4')
		elif 4000 <= DEPP <= 7000:
			SDEPP = 2/3 * float(wf_dep9.get())
			d138.config(bg='green2')
		elif 7000 < DEPP <= 9460:
			SDEPP = 1/3 * float(wf_dep9.get())
			d138.config(bg='green yellow')
		else:
			SDEPP = 0
			d138.config(bg='red')

		DEPASP = float(text_ft.get())
		if 2723 <= DEPASP < 2984.5:
			SDEPASP = 3/3 * float(wf_dep10.get())
			d139.config(bg='green4')
		elif 2984.5 <= DEPASP <= 5000:
			SDEPASP = 2/3 * float(wf_dep10.get())
			d139.config(bg='green2')
		elif 5000 < DEPASP <= 9000:
			SDEPASP = 1/3 * float(wf_dep10.get())
			d139.config(bg='green yellow')
		else:
			SDEPASP = 0
			d139.config(bg='red')

		DEPSPA = float(text_ft.get())
		if 625 <= DEPSPA < 1000:
			SDEPSPA = 3/3 * float(wf_dep11.get())
			d140.config(bg='green4')
		elif 1000 <= DEPSPA <= 2941.6:
			SDEPSPA = 2/3 * float(wf_dep11.get())
			d140.config(bg='green2')
		elif 2941.6 < DEPSPA <= 5300:
			SDEPSPA = 1/3 * float(wf_dep11.get())
			d140.config(bg='green yellow')
		else:
			SDEPSPA = 0
			d140.config(bg='red')

		DEPC = float(text_ft.get())
		if 400 <= DEPC < 5000:
			SDEPC = 3/3 * float(wf_dep12.get())
			d141.config(bg='green4')
		elif 5000 <= DEPC <= 8000:
			SDEPC = 2/3 * float(wf_dep12.get())
			d141.config(bg='green2')
		elif 8000 < DEPC <= 11300:
			SDEPC = 1/3 * float(wf_dep12.get())
			d141.config(bg='green yellow')
		else:
			SDEPC = 0
			d141.config(bg='red')
			e31.config(foreground="red")

		DEPST = float(text_ft.get())
		if 200 <= DEPST < 1643.6:
			SDEPST = 3/3 * float(wf_dep13.get())
			d142.config(bg='green4')
		elif 1643.6 <= DEPST <= 5000:
			SDEPST = 2/3 * float(wf_dep13.get())
			d142.config(bg='green2')
		elif 5000 < DEPST <= 9000:
			SDEPST = 1/3 * float(wf_dep13.get())
			d142.config(bg='green yellow')
		else:
			SDEPST = 0
			d142.config(bg='red')
			e32.config(foreground="red")

		DEPHOT = float(text_ft.get())
		if 500 <= DEPHOT < 1942:
			SDEPHOT = 3/3 * float(wf_dep14.get())
			d143.config(bg='green4')
		elif 1942 <= DEPHOT <= 2300:
			SDEPHOT = 2/3 * float(wf_dep14.get())
			d143.config(bg='green2')
		elif 2300 < DEPHOT <= 2950:
			SDEPHOT = 1/3 * float(wf_dep14.get())
			d143.config(bg='green yellow')
		else:
			SDEPHOT = 0
			d143.config(bg='red')
			e33.config(foreground="red")

		DEPMIC = float(text_ft.get())
		if 1572 <= DEPMIC < 2200:
			SDEPMIC = 1/3 * float(wf_dep15.get())
			d144.config(bg='green yellow')
		elif 2200 <= DEPMIC <= 3000:
			SDEPMIC = 2/3 * float(wf_dep15.get())
			d144.config(bg='green2')
		elif 3000 < DEPMIC <= 3464:
			SDEPMIC = 3/3 * float(wf_dep15.get())
			d144.config(bg='green4')
		else:
			SDEPMIC = 0
			d144.config(bg='red')

		TEMMCO2 = float(text_degF.get())
		if 82 <= TEMMCO2 < 100:
			STEMMC = 3/3 * float(wf_tem1.get())
			d146.config(bg='green4')
		elif 100 <= TEMMCO2 <= 150:
			STEMMC = 2/3 * float(wf_tem1.get())
			d146.config(bg='green2')
		elif 150 < TEMMCO2 <= 250:
			STEMMC = 1/3 * float(wf_tem1.get())
			d146.config(bg='green yellow')
		else:
			STEMMC = 0
			d146.config(bg='red')

		TEMMHC = float(text_degF.get())
		if 85 <= TEMMHC < 100:
			STEMMH = 3/3 * float(wf_tem2.get())
			d147.config(bg='green4')
		elif 100 <= TEMMHC <= 250:
			STEMMH = 2/3 * float(wf_tem2.get())
			d147.config(bg='green2')
		elif 250 < TEMMHC <= 329:
			STEMMH = 1/3 * float(wf_tem2.get())
			d147.config(bg='green yellow')
		else:
			STEMMH = 0
			d147.config(bg='red')

		TEMMW = float(text_degF.get())
		if 194 <= TEMMW < 220:
			STEMMW = 3/3 * float(wf_tem3.get())
			d148.config(bg='green4')
		elif 220 <= TEMMW <= 229.4:
			STEMMW = 2/3 * float(wf_tem3.get())
			d148.config(bg='green2')
		elif 229.4 < TEMMW <= 253:
			STEMMW = 1/3 * float(wf_tem3.get())
			d148.config(bg='green yellow')
		else:
			STEMMW = 0
			d148.config(bg='red')

		TEMMN = float(text_degF.get())
		if 190 <= TEMMN < 200:
			STEMMN = 3/3 * float(wf_tem4.get())
			d149.config(bg='green4')
		elif 200 <= TEMMN <= 300:
			STEMMN = 2/3 * float(wf_tem4.get())
			d149.config(bg='green2')
		elif 300 < TEMMN <= 325:
			STEMMN = 1/3 * float(wf_tem4.get())
			d149.config(bg='green yellow')
		else:
			STEMMN = 0
			d149.config(bg='red')

		TEMIN = float(text_degF.get())
		if 82 <= TEMIN < 150:
			STEMIN = 3/3 * float(wf_tem5.get())
			d150.config(bg='green4')
		elif 150 <= TEMIN <= 250:
			STEMIN = 2/3 * float(wf_tem5.get())
			d150.config(bg='green2')
		elif 250 < TEMIN <= 325:
			STEMIN = 1/3 * float(wf_tem5.get())
			d150.config(bg='green yellow')
		else:
			STEMIN = 0
			d150.config(bg='red')

		TEMICO2 = float(text_degF.get())
		if 82 <= TEMICO2 < 100:
			STEMIC = 3/3 * float(wf_tem6.get())
			d151.config(bg='green4')
		elif 100 <= TEMICO2 <= 150:
			STEMIC = 2/3 * float(wf_tem6.get())
			d151.config(bg='green2')
		elif 150 < TEMICO2 <= 198:
			STEMIC = 1/3 * float(wf_tem6.get())
			d151.config(bg='green yellow')
		else:
			STEMIC = 0
			d151.config(bg='red')

		TEMIH = float(text_degF.get())
		if 170 <= TEMIH < 173:
			STEMIH = 3/3 * float(wf_tem7.get())
			d152.config(bg='green4')
		elif 173 <= TEMIH <= 176:
			STEMIH = 2/3 * float(wf_tem7.get())
			d152.config(bg='green2')
		elif 176 < TEMIH <= 180:
			STEMIH = 1/3 * float(wf_tem7.get())
			d152.config(bg='green yellow')
		else:
			STEMIH = 0
			d152.config(bg='red')

		TEMIHW = float(text_degF.get())
		if 131 <= TEMIHW < 150:
			STEMIHW = 3/3 * float(wf_tem8.get())
			d153.config(bg='green4')
		elif 150 <= TEMIHW <= 200:
			STEMIHW = 2/3 * float(wf_tem8.get())
			d153.config(bg='green2')
		elif 200 < TEMIHW <= 267:
			STEMIHW = 1/3 * float(wf_tem8.get())
			d153.config(bg='green yellow')
		else:
			STEMIHW = 0
			d153.config(bg='red')

		TEMP = float(text_degF.get())
		if 74 <= TEMP < 100:
			STEMP = 3/3 * float(wf_tem9.get())
			d154.config(bg='green4')
		elif 100 <= TEMP <= 150:
			STEMP = 2/3 * float(wf_tem9.get())
			d154.config(bg='green')
		elif 150 < TEMP <= 237.2:
			STEMP = 1/3 * float(wf_tem9.get())
			d154.config(bg='green yellow')
		else:
			STEMP = 0
			d154.config(bg='red')
			e26.config(foreground="red")

		TEMASP = float(text_degF.get())
		if 80 <= TEMASP < 100:
			STEMASP = 3/3 * float(wf_tem10.get())
			d155.config(bg='green4')
		elif 100 <= TEMASP <= 150:
			STEMASP = 2/3 * float(wf_tem10.get())
			d155.config(bg='green2')
		elif 150 < TEMASP <= 200:
			STEMASP = 1/3 * float(wf_tem10.get())
			d155.config(bg='green yellow')
		else:
			STEMASP = 0
			d155.config(bg='red')
			e27.config(foreground="red")

		TEMSPA = float(text_degF.get())
		if 122 <= TEMSPA < 130:
			STEMSPA = 3/3* float(wf_tem11.get())
			d156.config(bg='green4')
		elif 130 <= TEMSPA <= 140:
			STEMSPA = 2/3 * float(wf_tem11.get())
			d156.config(bg='green2')
		elif 140 < TEMSPA <= 155:
			STEMSPA = 1/3 * float(wf_tem11.get())
			d156.config(bg='green yellow')
		else:
			STEMSPA = 0
			d156.config(bg='red')
			e28.config(foreground="red")

		TEMC = float(text_degF.get())
		if 64.4 <= TEMC < 100:
			STEMC = 3/3 * float(wf_tem12.get())
			d157.config(bg='green4')
		elif 100 <= TEMC <= 200:
			STEMC = 2/3 * float(wf_tem12.get())
			d157.config(bg='green2')
		elif 200 < TEMC <= 230:
			STEMC = 1/3 * float(wf_tem12.get())
			d157.config(bg='green yellow')
		else:
			STEMC = 0
			d157.config(bg='red')

		TEMST = float(text_degF.get())
		if 10 <= TEMST < 100:
			STEMST = 3/3 * float(wf_tem13.get())
			d158.config(bg='green4')
		elif 100 <= TEMST <= 220:
			STEMST = 2/3 * float(wf_tem13.get())
			d158.config(bg='green2')
		elif 220 < TEMST <= 350:
			STEMST = 1/3 * float(wf_tem13.get())
			d158.config(bg='green yellow')
		else:
			STEMST = 0
			d158.config(bg='red')

		TEMHOT = float(text_degF.get())
		if 75 <= TEMHOT < 90:
			STEMHOT = 3/3 * float(wf_tem14.get())
			d159.config(bg='green4')
		elif 90 <= TEMHOT <= 100:
			STEMHOT = 2/3 * float(wf_tem14.get())
			d159.config(bg='green2')
		elif 100 < TEMHOT <= 135:
			STEMHOT = 1/3 * float(wf_tem14.get())
			d159.config(bg='green yellow')
		else:
			STEMHOT = 0
			d159.config(bg='red')
			e33.config(foreground="red")

		TEMMIC = float(text_degF.get())
		if 86 <= TEMMIC < 88:
			STEMMIC = 3/3 * float(wf_tem15.get())
			d160.config(bg='green4')
		elif 88 <= TEMMIC <= 89:
			STEMMIC = 2/3 * float(wf_tem15.get())
			d160.config(bg='green2')
		elif 89 < TEMMIC <= 90:
			STEMMIC = 1/3 * float(wf_tem15.get())
			d160.config(bg='green yellow')
		else:
			STEMMIC = 0
			d160.config(bg='red')

		if entryformation.get() == 'Sandstone':
			SFORMC = 1 * float(wf_for1.get())
			d82.config(bg="green")
			SFORMH = 1 * float(wf_for2.get())
			d83.config(bg="green")
			SFORMW = 1 * float(wf_for3.get())
			d84.config(bg="green")
			SFORMN = 1 * float(wf_for4.get())
			d85.config(bg="green")
			SFORIN = 1 * float(wf_for5.get())
			d86.config(bg="green")
			SFORIC = 1 * float(wf_for6.get())
			d87.config(bg="green")
			SFORIH = 1 * float(wf_for7.get())
			d88.config(bg="green")
			SFORIHW = 1 * float(wf_for8.get())
			d89.config(bg="green")
			SFORP = 1 * float(wf_for9.get())
			d90.config(bg="green")
			SFORASP = 1 * float(wf_for10.get())
			d91.config(bg="green")
			SFORSPA = 1 * float(wf_for11.get())
			d92.config(bg="green")
			SFORC = 1 * float(wf_for12.get())
			d93.config(bg="green")
			SFORST = 1 * float(wf_for13.get())
			d94.config(bg="green")
			SFORHOT = 1 * float(wf_for14.get())
			d95.config(bg="green")
			SFORMIC = 1 * float(wf_for15.get())
			d96.config(bg="green")

		if entryformation.get() == 'Carbonate':
			SFORMC = 1 * float(wf_for1.get())
			d82.config(bg="green")
			SFORMH = 1 * float(wf_for2.get())
			d83.config(bg="green")
			SFORMW = 0 * float(wf_for3.get())
			d84.config(bg="red")
			SFORMN = 1 * float(wf_for4.get())
			d85.config(bg="green")
			SFORIN = 0 * float(wf_for5.get())
			d86.config(bg="red")
			SFORIC = 1 * float(wf_for6.get())
			d87.config(bg="green")
			SFORIH = 0 * float(wf_for7.get())
			d88.config(bg="red")
			SFORIHW = 1 * float(wf_for8.get())
			d89.config(bg="green")
			SFORP = 0 * float(wf_for9.get())
			d90.config(bg="red")
			SFORASP = 0 * float(wf_for10.get())
			d91.config(bg="red")
			SFORSPA = 0 * float(wf_for11.get())
			d92.config(bg="red")
			SFORC = 1 * float(wf_for12.get())
			d93.config(bg="green")
			SFORST = 0 * float(wf_for13.get())
			d94.config(bg="red")
			SFORHOT = 0 * float(wf_for14.get())
			d95.config(bg="red")
			SFORMIC = 0 * float(wf_for15.get())
			d96.config(bg="red")

		if entrythickness.get() == '< 20 ft':
			STHIMC = 0
			STHIMH = 1
			d115.config(bg="green")
			STHIMW = 0
			STHIMN = 1
			d117.config(bg="green")
			STHIIN = 0
			STHIIC = 0
			STHIIH = 0
			STHIIHW =0
			STHIP = 0
			STHIASP = 0
			STHISPA = 0
			STHIC = 1
			d125.config(bg="green")
			STHIST = 0
			d126.config(bg="red")
			STHIHOT = 0
			STHIMIC = 0

		if entrythickness.get() == '> 20 ft With Dip':
			STHIMC = 0 * float(wf_thi1.get())
			STHIMH = 1 * float(wf_thi2.get())
			d115.config(bg="green")
			STHIMW = 0 * float(wf_thi3.get())
			STHIMN = 1 * float(wf_thi4.get())
			d117.config(bg="green")
			STHIIN = 0 * float(wf_thi5.get())
			STHIIC = 0 * float(wf_thi6.get())
			STHIIH = 0 * float(wf_thi7.get())
			STHIIHW =0 * float(wf_thi8.get())
			STHIP = 0 * float(wf_thi9.get())
			STHIASP = 0 * float(wf_thi10.get())
			STHISPA = 0 * float(wf_thi11.get())
			STHIC = 0 * float(wf_thi12.get())
			d125.config(bg="red")
			STHIST = 0 * float(wf_thi13.get())
			d126.config(bg="red")
			STHIHOT = 0 * float(wf_thi14.get())
			STHIMIC = 0 * float(wf_thi15.get())

		if entrythickness.get() == '> 20 ft No Dip':
			STHIMC = 0 * float(wf_thi1.get())
			STHIMH = 0 * float(wf_thi2.get())
			d115.config(bg="red")
			STHIMW = 0 * float(wf_thi3.get())
			STHIMN = 1 * float(wf_thi4.get())
			d117.config(bg="red")
			STHIIN = 0 * float(wf_thi5.get())
			STHIIC = 0 * float(wf_thi6.get())
			STHIIH = 0 * float(wf_thi7.get())
			STHIIHW =0 * float(wf_thi8.get())
			STHIP = 0 * float(wf_thi9.get())
			STHIASP = 0 * float(wf_thi10.get())
			STHISPA = 0 * float(wf_thi11.get())
			STHIC = 1 * float(wf_thi12.get())
			d125.config(bg="green")
			STHIST = 1 * float(wf_thi13.get())
			d126.config(bg="green")
			STHIHOT = 0 * float(wf_thi14.get())
			STHIMIC = 0 * float(wf_thi15.get())



	TOTALSCOREMC = (SAPIMC + SVISMC + SPORMC + SSATMC + SPERMC + SDEPMC + STEMMC + SFORMC + STHIMC) / (
			float(wf_api1.get()) + float(wf_vis1.get()) + float(wf_por1.get()) + float(wf_sat1.get()) + float(
		wf_for1.get()) + float(wf_per1.get()) + float(wf_thi1.get()) + float(wf_dep1.get()) + float(wf_tem1.get())) * 100
	TOTALSCOREMH = (SAPIMH + SVISMH + SPORMH + SSATMH + SPERMH + SDEPMH + STEMMH + SFORMH + STHIMH) / (
				float(wf_api2.get()) + float(wf_vis2.get()) + float(wf_por2.get()) + float(wf_sat2.get()) + float(
			wf_for2.get()) + float(wf_per2.get()) + float(wf_thi2.get()) + float(wf_dep2.get()) + float(wf_tem2.get())) * 100
	TOTALSCOREMW = (SAPIMW + SVISMW + SPORMW + SSATMW + SPERMW + SDEPMW + STEMMW + SFORMW + STHIMW) / (
				float(wf_api3.get()) + float(wf_vis3.get()) + float(wf_por3.get()) + float(wf_sat3.get()) + float(
			wf_for3.get()) + float(wf_per3.get()) + float(wf_thi3.get()) + float(wf_dep3.get()) + float(wf_tem3.get())) * 100
	TOTALSCOREMN = (SAPIMN + SVISMN + SPORMN + SSATMN + SPERMN + SDEPMN + STEMMN + SFORMN + STHIMN) / (
				float(wf_api4.get()) + float(wf_vis4.get()) + float(wf_por4.get()) + float(wf_sat4.get()) + float(
			wf_for4.get()) + float(wf_per4.get()) + float(wf_thi4.get()) + float(wf_dep4.get()) + float(wf_tem4.get())) * 100
	TOTALSCOREIN = (SAPIIN + SVISIN + SPORIN + SSATIN + SPERIN + SDEPIN + STEMIN + SFORIN + STHIIN) / (
				float(wf_api5.get()) + float(wf_vis5.get()) + float(wf_por5.get()) + float(wf_sat5.get()) + float(
			wf_for5.get()) + float(wf_per5.get()) + float(wf_thi5.get()) + float(wf_dep5.get()) + float(wf_tem5.get())) * 100
	TOTALSCOREIC = (SAPIIC + SVISIC + SPORIC + SSATIC + SPERIC + SDEPIC + STEMIC + SFORIC + STHIIC) / (
				float(wf_api6.get()) + float(wf_vis6.get()) + float(wf_por6.get()) + float(wf_sat6.get()) + float(
			wf_for6.get()) + float(wf_per6.get()) + float(wf_thi6.get()) + float(wf_dep6.get()) + float(wf_tem6.get())) * 100
	TOTALSCOREIH = (SAPIIH + SVISIH + SPORIH + SSATIH + SPERIH + SDEPIH + STEMIH + SFORIH + STHIIH) / (
				float(wf_api7.get()) + float(wf_vis7.get()) + float(wf_por7.get()) + float(wf_sat7.get()) + float(
			wf_for7.get()) + float(wf_per7.get()) + float(wf_thi7.get()) + float(wf_dep7.get()) + float(wf_tem7.get())) * 100
	TOTALSCOREIHW = (SAPIIHW + SVISIHW + SPORIHW + SSATIHW + SPERIHW + SDEPIHW + STEMIHW + SFORIHW + STHIIHW) / (
				float(wf_api8.get()) + float(wf_vis8.get()) + float(wf_por8.get()) + float(wf_sat8.get()) + float(
			wf_for8.get()) + float(wf_per8.get()) + float(wf_thi8.get()) + float(wf_dep8.get()) + float(wf_tem8.get())) * 100
	TOTALSCOREP = (SAPIP + SVISP + SPORP + SSATP + SPERP + SDEPP + STEMP + SFORP + STHIP) / (
				float(wf_api9.get()) + float(wf_vis9.get()) + float(wf_por9.get()) + float(wf_sat9.get()) + float(
			wf_for9.get()) + float(wf_per9.get()) + float(wf_thi9.get()) + float(wf_dep9.get()) + float(wf_tem9.get())) * 100
	TOTALSCOREASP = (SAPIASP + SVISASP + SPORASP + SSATASP + SPERASP + SDEPASP + STEMASP + SFORASP + STHIASP) / (
				float(wf_api10.get()) + float(wf_vis10.get()) + float(wf_por10.get()) + float(wf_sat10.get()) + float(
			wf_for10.get()) + float(wf_per10.get()) + float(wf_thi10.get()) + float(wf_dep10.get()) + float(
			wf_tem10.get())) * 100
	TOTALSCORESPA = (SAPISPA + SVISSPA + SPORSPA + SSATSPA + SPERSPA + SDEPSPA + STEMSPA + SFORSPA + STHISPA) / (
				float(wf_api11.get()) + float(wf_vis11.get()) + float(wf_por11.get()) + float(wf_sat11.get()) + float(
			wf_for11.get()) + float(wf_per11.get()) + float(wf_thi11.get()) + float(wf_dep11.get()) + float(
			wf_tem11.get())) * 100
	TOTALSCOREC = (SAPIC + SVISC + SPORC + SSATC + SPERC + SDEPC + STEMC + SFORC + STHIC) / (
				float(wf_api12.get()) + float(wf_vis12.get()) + float(wf_por12.get()) + float(wf_sat12.get()) + float(
			wf_for12.get()) + float(wf_per12.get()) + float(wf_thi12.get()) + float(wf_dep12.get()) + float(
			wf_tem12.get())) * 100
	TOTALSCOREST = (SAPIST + SVISST + SPORST + SSATST + SPERST + SDEPST + STEMST + SFORST + STHIST) / (
				float(wf_api13.get()) + float(wf_vis13.get()) + float(wf_por13.get()) + float(wf_sat13.get()) + float(
			wf_for13.get()) + float(wf_per13.get()) + float(wf_thi13.get()) + float(wf_dep13.get()) + float(
			wf_tem13.get())) * 100
	TOTALSCOREHOT = (SAPIHOT + SVISHOT + SPORHOT + SSATHOT + SPERHOT + SDEPHOT + STEMHOT + SFORHOT + STHIHOT) / (
				float(wf_api14.get()) + float(wf_vis14.get()) + float(wf_por14.get()) + float(wf_sat14.get()) + float(
			wf_for14.get()) + float(wf_per14.get()) + float(wf_thi14.get()) + float(wf_dep14.get()) + float(
			wf_tem14.get())) * 100
	TOTALSCOREMIC = (SAPIMIC + SVISMIC + SPORMIC + SSATMIC + SPERMIC + SDEPMIC + STEMMIC + SFORMIC + STHIMIC) / (
				float(wf_api15.get()) + float(wf_vis15.get()) + float(wf_por15.get()) + float(wf_sat15.get()) + float(
			wf_for15.get()) + float(wf_per15.get()) + float(wf_thi15.get()) + float(wf_dep15.get()) + float(
			wf_tem15.get())) * 100

	score_MCOO.set(str('%.1f' % (TOTALSCOREMC)))
	score_MHyd.set(str('%.1f' % (TOTALSCOREMH)))
	score_MWAG.set(str('%.1f' % (TOTALSCOREMW)))
	score_MNit.set(str('%.1f' % (TOTALSCOREMN)))
	score_INit.set(str('%.1f' % (TOTALSCOREIN)))
	score_IHyd.set(str('%.1f' % (TOTALSCOREIC)))
	score_ICOO.set(str('%.1f' % (TOTALSCOREIH)))
	score_IHWAG.set(str('%.1f' % (TOTALSCOREIHW)))
	score_Pol.set(str('%.1f' % (TOTALSCOREP)))
	score_ASP.set(str('%.1f' % (TOTALSCOREASP)))
	score_SPA.set(str('%.1f' % (TOTALSCORESPA)))
	score_Com.set(str('%.1f' % (TOTALSCOREC)))
	score_Ste.set(str('%.1f' % (TOTALSCOREST)))
	score_Hot.set(str('%.1f' % (TOTALSCOREHOT)))
	score_Mic.set(str('%.1f' % (TOTALSCOREMIC)))

###CHART
	spiderradar.grid() ##Show radar
	theta = ['Mis. CO2',
			 'Mis. Hydrocarbon',
			 'Mis. WAG',
			 'Mis. Nitrogen',
			 'Imm. Nitrogen',
			 'Imm. CO2',
			 'Imm. Hydrocarbon',
			 'Imm. Hydrocarbon + WAG',
			 'Polymer',
			 'ASP',
			 'ASP + Polymer/Alkaline',
			 'Combustion',
			 'Steam',
			 'Hot Water',
			 'Microbial'
			 ]

	r = [
		TOTALSCOREMC,
		TOTALSCOREMH,
		TOTALSCOREMW,
		TOTALSCOREMN,
		TOTALSCOREIN,
		TOTALSCOREIC,
		TOTALSCOREIH,
		TOTALSCOREIHW,
		TOTALSCOREP,
		TOTALSCOREASP,
		TOTALSCORESPA,
		TOTALSCOREC,
		TOTALSCOREST,
		TOTALSCOREHOT,
		TOTALSCOREMIC,
		TOTALSCOREMC
	]

	label_placement = np.linspace(start=0, stop=2 * np.pi, num=len(r))
	figure1 = plt.figure(figsize=(10,9), dpi=80)
	ax1 = figure1.add_subplot(111, projection="polar")
	radar1 = FigureCanvasTkAgg(figure1, spiderradar)
	radar1.get_tk_widget().grid(row=0, column=0)
	ax1.plot(label_placement, r, marker="o", linewidth=1)
	ax1.fill(label_placement, r, alpha=0.25)
	lines, labels = plt.thetagrids(np.degrees(label_placement), labels=theta)

#========================================RESET=========================================================
#========================================RESET=========================================================
#========================================RESET=========================================================

def reset_values():
	text_Title.set("")
	text_API.set("")
	text_cp.set("")
	text_so.set("")
	text_por.set("")
	text_formation.set("")
	text_thickness.set("")
	text_composition.set("")
	text_md.set("")
	text_ft.set("")
	text_degF.set("")
	score_MNit.set("")
	score_MHyd.set("")
	score_MCOO.set("")
	score_MWAG.set("")
	score_INit.set("")
	score_IHyd.set("")
	score_ICOO.set("")
	score_IHWAG.set("")
	score_Pol.set("")
	score_ASP.set("")
	score_SPA.set("")
	score_Com.set("")
	score_Ste.set("")
	score_Hot.set("")
	score_Mic.set("")
	spiderradar.grid_forget()
	d18.config(bg='white')
	d19.config(bg='white')
	d20.config(bg='white')
	d21.config(bg='white')
	d22.config(bg='white')
	d23.config(bg='white')
	d24.config(bg='white')
	d25.config(bg='white')
	d26.config(bg='white')
	d27.config(bg='white')
	d28.config(bg='white')
	d29.config(bg='white')
	d30.config(bg='white')
	d31.config(bg='white')
	d32.config(bg='white')
	d34.config(bg='white')
	d35.config(bg='white')
	d36.config(bg='white')
	d37.config(bg='white')
	d38.config(bg='white')
	d39.config(bg='white')
	d40.config(bg='white')
	d41.config(bg='white')
	d42.config(bg='white')
	d43.config(bg='white')
	d44.config(bg='white')
	d45.config(bg='white')
	d46.config(bg='white')
	d47.config(bg='white')
	d48.config(bg='white')
	d50.config(bg='white')
	d51.config(bg='white')
	d52.config(bg='white')
	d53.config(bg='white')
	d54.config(bg='white')
	d55.config(bg='white')
	d56.config(bg='white')
	d57.config(bg='white')
	d58.config(bg='white')
	d59.config(bg='white')
	d60.config(bg='white')
	d61.config(bg='white')
	d62.config(bg='white')
	d63.config(bg='white')
	d64.config(bg='white')
	d66.config(bg='white')
	d67.config(bg='white')
	d68.config(bg='white')
	d69.config(bg='white')
	d70.config(bg='white')
	d71.config(bg='white')
	d72.config(bg='white')
	d73.config(bg='white')
	d74.config(bg='white')
	d75.config(bg='white')
	d76.config(bg='white')
	d77.config(bg='white')
	d78.config(bg='white')
	d79.config(bg='white')
	d80.config(bg='white')
	d82.config(bg='white')
	d83.config(bg='white')
	d84.config(bg='white')
	d85.config(bg='white')
	d86.config(bg='white')
	d87.config(bg='white')
	d88.config(bg='white')
	d89.config(bg='white')
	d90.config(bg='white')
	d91.config(bg='white')
	d92.config(bg='white')
	d93.config(bg='white')
	d94.config(bg='white')
	d95.config(bg='white')
	d96.config(bg='white')
	d98.config(bg='white')
	d99.config(bg='white')
	d100.config(bg='white')
	d101.config(bg='white')
	d102.config(bg='white')
	d103.config(bg='white')
	d104.config(bg='white')
	d105.config(bg='white')
	d106.config(bg='white')
	d107.config(bg='white')
	d108.config(bg='white')
	d109.config(bg='white')
	d110.config(bg='white')
	d111.config(bg='white')
	d112.config(bg='white')
	d114.config(bg='white')
	d115.config(bg='white')
	d116.config(bg='white')
	d117.config(bg='white')
	d118.config(bg='white')
	d119.config(bg='white')
	d120.config(bg='white')
	d121.config(bg='white')
	d122.config(bg='white')
	d123.config(bg='white')
	d124.config(bg='white')
	d125.config(bg='white')
	d126.config(bg='white')
	d127.config(bg='white')
	d128.config(bg='white')
	d130.config(bg='white')
	d131.config(bg='white')
	d132.config(bg='white')
	d133.config(bg='white')
	d134.config(bg='white')
	d135.config(bg='white')
	d136.config(bg='white')
	d137.config(bg='white')
	d138.config(bg='white')
	d139.config(bg='white')
	d140.config(bg='white')
	d141.config(bg='white')
	d142.config(bg='white')
	d143.config(bg='white')
	d144.config(bg='white')
	d146.config(bg='white')
	d147.config(bg='white')
	d148.config(bg='white')
	d149.config(bg='white')
	d150.config(bg='white')
	d151.config(bg='white')
	d152.config(bg='white')
	d153.config(bg='white')
	d154.config(bg='white')
	d155.config(bg='white')
	d156.config(bg='white')
	d157.config(bg='white')
	d158.config(bg='white')
	d159.config(bg='white')
	d160.config(bg='white')

btnCalculate = Button(ButtonsFrames, bd=5, fg="black", font=('arial',10,'bold'), command=ref, bg="gainsboro", text="Calculate").grid(row=0,column=0)
btnClose = Button(ButtonsFrames, bd=5, fg="black", font=('arial',10,'bold'), bg="gainsboro", text="Reset", command=reset_values).grid(row=0,column=1)


#=================================USER INPUT + ENTRY===================================================
#=================================USER INPUT + ENTRY===================================================
#=================================USER INPUT + ENTRY===================================================

t1=Label(PropFrame, font=('arial',16,'bold'), bg="aliceblue", text="User Input", pady=5, bd=5).grid(row=0)
t2=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Title", padx=5, pady=5, bd=5).grid(row=1,column=0, sticky=W)
e2 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_Title, insertwidth=4, bg="white", justify='left')
e2.grid(row=1, column=1)
t3=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="API Gravity", padx=5, pady=5, bd=5).grid(row=2,column=0, sticky=W)
e3 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_API, insertwidth=4,bg="white", justify='left')
e3.grid(row=2, column=1)
t4=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Oil Viscosity[cP]", padx=5, pady=5, bd=5).grid(row=3,column=0, sticky=W)
e4 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_cp, insertwidth=4,bg="white", justify='left')
e4.grid(row=3, column=1)
t5=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Oil Saturation, [%]", padx=5, pady=5, bd=5).grid(row=5,column=0, sticky=W)
e5 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_so, insertwidth=4,bg="white", justify='left')
e5.grid(row=5, column=1)
t6=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Porosity, [%]", padx=5, pady=5, bd=5).grid(row=4,column=0, sticky=W)
e6 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_por, insertwidth=4,bg="white", justify='left')
e6.grid(row=4, column=1)
t7=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Formation", padx=5, pady=5, bd=5).grid(row=6,column=0, sticky=W)
entryformation = ttk.Combobox(PropFrame, values=["Sandstone", "Carbonate"],)
entryformation.grid(row=6, column=1, sticky=W)
entryformation.current(0)
t8=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Thickness", padx=5, pady=5, bd=5).grid(row=7,column=0, sticky=W)
entrythickness = ttk.Combobox(PropFrame, values=["< 20 ft", "> 20 ft No Dip", "> 20 ft With Dip"],)
entrythickness.grid(row=7, column=1, sticky=W)
entrythickness.current(0)
t9=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Permeability[mD]", padx=5, pady=5, bd=5).grid(row=8,column=0, sticky=W)
e9 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_md, insertwidth=4,bg="white", justify='left')
e9.grid(row=8, column=1)
t10=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Depth[ft]", padx=5, pady=5, bd=5).grid(row=9,column=0, sticky=W)
e10 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_ft, insertwidth=4,bg="white", justify='left')
e10.grid(row=9, column=1)
t11=Label(PropFrame, font=('arial',10,'bold'), bg="aliceblue", text="Temperature[deg F]", padx=5, pady=5, bd=5).grid(row=10,column=0, sticky=W)
e11 = Entry(PropFrame,font=('arial', 10,'bold'), textvariable=text_degF, insertwidth=4,bg="white", justify='left')
e11.grid(row=10, column=1)

#===================================SYSTEM OUTPUT======================================================
#===================================SYSTEM OUTPUT======================================================
#===================================SYSTEM OUTPUT======================================================

t12 = Label(L11, font=('arial',10,'bold'), bg='aliceblue', text='                  Miscible Gas Injection', pady=5).grid()
t13 = Label(L12, font=('arial',10,'bold'), bg='aliceblue', text='Criteria Fit (%)', padx=4).grid(row=0, column=1)
t14 = Label(L12, font=('arial',10,'bold'), bg='aliceblue', text='Nitrogen', padx=4).grid(row=4,column=0, sticky=W)
t15 = Label(L12, font=('arial',10,'bold'), bg='aliceblue', text='Hydrocarbon', padx=4).grid(row=2,column=0, sticky=W)
t16 = Label(L12, font=('arial',10,'bold'), bg='aliceblue', text='Carbon Dioxide        ', padx=4).grid(row=1,column=0, sticky=W)
t17 = Label(L12, font=('arial',10,'bold'), bg='aliceblue', text='WAG', padx=4).grid(row=3,column=0, sticky=W)

e14 = Entry(L12,font=('arial', 10,'bold'), textvariable=score_MNit, insertwidth=4,bg="white", justify='left')
e14.grid(row=4, column=1)
e15= Entry(L12,font=('arial', 10,'bold'), textvariable=score_MHyd, insertwidth=4,bg="white", justify='left')
e15.grid(row=2, column=1)
e16 = Entry(L12,font=('arial', 10,'bold'), textvariable=score_MCOO, insertwidth=4,bg="white", justify='left')
e16.grid(row=1, column=1)
e17 = Entry(L12,font=('arial', 10,'bold'), textvariable=score_MWAG, insertwidth=4,bg="white", justify='left')
e17.grid(row=3, column=1)

t18 = Label(L21, font=('arial',10,'bold'), bg='aliceblue', text='                Immiscible Gas Injection', pady=5).grid()
t19 = Label(L22, font=('arial',10,'bold'), bg='aliceblue', text='Criteria Fit (%)').grid(row=0,column=1)
t20 = Label(L22, font=('arial',10,'bold'), bg='aliceblue', text='Nitrogen', padx=4).grid(row=1,column=0, sticky=W)
t21 = Label(L22, font=('arial',10,'bold'), bg='aliceblue', text='Hydrocarbon', padx=4).grid(row=2,column=0, sticky=W)
t22 = Label(L22, font=('arial',10,'bold'), bg='aliceblue', text='Carbon Dioxide', padx=4).grid(row=3,column=0, sticky=W)
t23 = Label(L22, font=('arial',10,'bold'), bg='aliceblue', text='Hydrocarbon + WAG', padx=4).grid(row=4,column=0, sticky=W)

e20 = Entry(L22,font=('arial', 10,'bold'), textvariable=score_INit, insertwidth=4,bg="white", justify='left')
e20.grid(row=1, column=1)
e21 = Entry(L22,font=('arial', 10,'bold'), textvariable=score_IHyd, insertwidth=4,bg="white", justify='left')
e21.grid(row=2, column=1)
e22 = Entry(L22,font=('arial', 10,'bold'), textvariable=score_ICOO, insertwidth=4,bg="white", justify='left')
e22.grid(row=3, column=1)
e23 = Entry(L22,font=('arial', 10,'bold'), textvariable=score_IHWAG, insertwidth=4,bg="white", justify='left')
e23.grid(row=4, column=1)

t24 = Label(L31, font=('arial',10,'bold'), bg='aliceblue', text='              (Enhanced) Waterflooding', pady=5).grid()
t25 = Label(L32, font=('arial',10,'bold'), bg='aliceblue', text='Criteria Fit (%)').grid(row=0,column=1)
t26 = Label(L32, font=('arial',10,'bold'), bg='aliceblue', text='Polymer                   ', padx=4).grid(row=1,column=0, sticky=W)
t27 = Label(L32, font=('arial',10,'bold'), bg='aliceblue', text='Alkaline Surfactant' + '\n' + 'Polymer (ASP)', padx=4).grid(row=2,column=0, sticky=W)
t28 = Label(L32, font=('arial',10,'bold'), bg='aliceblue', text='Surfactan' + '\n' + 'Polymer/Alkaline', padx=4).grid(row=3,column=0, sticky=W)

e26 = Entry(L32,font=('arial', 10,'bold'), textvariable=score_Pol, insertwidth=4,bg="white", justify='left')
e26.grid(row=1, column=1)
e27 = Entry(L32,font=('arial', 10,'bold'), textvariable=score_ASP, insertwidth=4,bg="white", justify='left')
e27.grid(row=2, column=1)
e28 = Entry(L32,font=('arial', 10,'bold'), textvariable=score_SPA, insertwidth=4,bg="white", justify='left')
e28.grid(row=3, column=1)

t29 = Label(L41, font=('arial',10,'bold'), bg='aliceblue', text='                   Thermal/Mechanical', pady=5).grid()
t30 = Label(L42, font=('arial',10,'bold'), bg='aliceblue', text='Criteria Fit (%)').grid(row=0,column=1)
t31 = Label(L42, font=('arial',10,'bold'), bg='aliceblue', text='Combustion              ', padx=4).grid(row=1,column=0, sticky=W)
t32 = Label(L42, font=('arial',10,'bold'), bg='aliceblue', text='Steam', padx=4).grid(row=2,column=0, sticky=W)
t33 = Label(L42, font=('arial',10,'bold'), bg='aliceblue', text='Hotwater', padx=4).grid(row=3,column=0, sticky=W)

e31 = Entry(L42,font=('arial', 10,'bold'), textvariable=score_Com, insertwidth=4,bg="white", justify='left')
e31.grid(row=1, column=1)
e32 = Entry(L42,font=('arial', 10,'bold'), textvariable=score_Ste, insertwidth=4,bg="white", justify='left')
e32.grid(row=2, column=1)
e33 = Entry(L42,font=('arial', 10,'bold'), textvariable=score_Hot, insertwidth=4,bg="white", justify='left')
e33.grid(row=3, column=1)

t34 = Label(L51, font=('arial',10,'bold'), bg='aliceblue', text='                           Microbial', pady=5).grid()
t35 = Label(L52, font=('arial',10,'bold'), bg='aliceblue', text='Criteria Fit (%)').grid(row=0,column=1)
t36 = Label(L52, font=('arial',10,'bold'), bg='aliceblue', text='Microbial                  ', padx=4).grid(row=1,column=0, sticky=W)
e36 = Entry(L52,font=('arial', 10,'bold'), textvariable=score_Mic, insertwidth=4,bg="white", justify='left')
e36.grid(row=1, column=1)

#======================================DETAIL==========================================================
#======================================DETAIL==========================================================
#======================================DETAIL==========================================================

d01 = Label(Detail, text="Category",bg="deepskyblue", relief=SOLID, bd=1)
d01.grid(row=0,column=0, rowspan=2, sticky="nsew",padx=1,pady=1)
d01 = Label(Detail, text="Miscible" + "\n" + "Gas" + "\n" "Injection",bg="deepskyblue", relief=SOLID, bd=1)
d01.grid(row=2,column=0, rowspan=4, sticky="nsew",padx=1,pady=1)
d02 = Label(Detail, text="Immiscible" + "\n" + "Gas" + "\n" "Injection",bg="deepskyblue", relief=SOLID, bd=1)
d02.grid(row=6,column=0, rowspan=4, sticky="nsew",padx=1,pady=1)
d03 = Label(Detail, text="Enhanced" + "\n" + "Waterflooding",bg="deepskyblue", relief=SOLID, bd=1)
d03.grid(row=10,column=0, rowspan=3, sticky="nsew",padx=1,pady=1)
d04 = Label(Detail, text="Thermal/" + "\n" + "Mechanical",bg="deepskyblue", relief=SOLID, bd=1)
d04.grid(row=13,column=0, rowspan=3, sticky="nsew",padx=1,pady=1)
d05 = Label(Detail, text="MEOR",bg="deepskyblue", relief=SOLID, bd=1)
d05.grid(row=16,column=0, sticky="nsew",padx=1,pady=1)

d1 = Label(Detail, text="EOR Method",bg="deepskyblue", relief=SOLID, bd=1)
d1.grid(row=0,column=1, rowspan=2, sticky="nsew",padx=1,pady=1)
d2 = Label(Detail, text="CO2", bg="lightskyblue", relief=SOLID, bd=1)
d2.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
d3 = Label(Detail, text="Hydrocarbon", bg="lightskyblue", relief=SOLID, bd=1)
d3.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
d4 = Label(Detail, text="WAG", bg="lightskyblue", relief=SOLID, bd=1)
d4.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)
d5 = Label(Detail, text="Nitrogen", bg="lightskyblue", relief=SOLID, bd=1)
d5.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)
d6 = Label(Detail, text="Nitrogen", bg="lightskyblue", relief=SOLID, bd=1)
d6.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)
d7 = Label(Detail, text="CO2", bg="lightskyblue", relief=SOLID, bd=1)
d7.grid(row=7, column=1, sticky="nsew", padx=1, pady=1)
d8 = Label(Detail, text="Hydrocarbon", bg="lightskyblue", relief=SOLID, bd=1)
d8.grid(row=8, column=1, sticky="nsew", padx=1, pady=1)
d9 = Label(Detail, text="Hydrocarbon + WAG", bg="lightskyblue", relief=SOLID, bd=1)
d9.grid(row=9, column=1, sticky="nsew", padx=1, pady=1)
d10 = Label(Detail, text="Polymer", bg="lightskyblue", relief=SOLID, bd=1)
d10.grid(row=10, column=1, sticky="nsew", padx=1, pady=1)
d11 = Label(Detail, text="Alkaline Surfactant" + "\n" + "Polymer (ASP)", bg="lightskyblue", relief=SOLID, bd=1)
d11.grid(row=11, column=1, sticky="nsew", padx=1, pady=1)
d12 = Label(Detail, text="Surfactant" + "\n" + "+ Polymer/Alkaline", bg="lightskyblue", relief=SOLID, bd=1)
d12.grid(row=12, column=1, sticky="nsew", padx=1, pady=1)
d13 = Label(Detail, text="Combustion", bg="lightskyblue", relief=SOLID, bd=1)
d13.grid(row=13, column=1, sticky="nsew", padx=1, pady=1)
d14 = Label(Detail, text="Steam", bg="lightskyblue", relief=SOLID, bd=1)
d14.grid(row=14, column=1, sticky="nsew", padx=1, pady=1)
d15 = Label(Detail, text="Hot Water", bg="lightskyblue", relief=SOLID, bd=1)
d15.grid(row=15, column=1, sticky="nsew", padx=1, pady=1)
d16 = Label(Detail, text="Microbial", bg="lightskyblue", relief=SOLID, bd=1)
d16.grid(row=16, column=1, sticky="nsew", padx=1, pady=1)

d17 = Label(Detail, text="  Oil API Gravity  ",bg="deepskyblue", relief=SOLID, bd=1)
d17.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=1, pady=1)
d18 = Label(Detail, text="22 - 45" + "\n" + "Avg. 37", bg="azure", relief=SOLID, bd=1)
d18.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
d19 = Label(Detail, text="25 - 57" + "\n" + "Avg. 38.3", bg="azure", relief=SOLID, bd=1)
d19.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)
d20 = Label(Detail, text="33 - 39" + "\n" + "Avg. 35.6", bg="azure", relief=SOLID, bd=1)
d20.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)
d21 = Label(Detail, text="35 - 54" + "\n" + "Avg. 47.6", bg="azure", relief=SOLID, bd=1)
d21.grid(row=5, column=2, sticky="nsew", padx=1, pady=1)
d22 = Label(Detail, text="16 - 54" + "\n" + "34.6", bg="azure", relief=SOLID, bd=1)
d22.grid(row=6, column=2, sticky="nsew", padx=1, pady=1)
d23 = Label(Detail, text="11 - 35" + "\n" + "22.6", bg="azure", relief=SOLID, bd=1)
d23.grid(row=7, column=2, sticky="nsew", padx=1, pady=1)
d24 = Label(Detail, text="22 - 48" + "\n" + "35", bg="azure", relief=SOLID, bd=1)
d24.grid(row=8, column=2, sticky="nsew", padx=1, pady=1)
d25 = Label(Detail, text="9.3 - 41" + "\n" + "31", bg="azure", relief=SOLID, bd=1)
d25.grid(row=9, column=2, sticky="nsew", padx=1, pady=1)
d26 = Label(Detail, text="13 - 42.5 " + "\n" + "26.5", bg="azure", relief=SOLID, bd=1)
d26.grid(row=10, column=2, sticky="nsew", padx=1, pady=1)
d27 = Label(Detail, text="20 - 35" + "\n" + "32.6", bg="azure", relief=SOLID, bd=1)
d27.grid(row=11, column=2, sticky="nsew", padx=1, pady=1)
d28 = Label(Detail, text="22 - 39" + "\n" + "31", bg="azure", relief=SOLID, bd=1)
d28.grid(row=12, column=2, sticky="nsew", padx=1, pady=1)
d29 = Label(Detail, text="10 - 38" + "\n" + "23.6", bg="azure", relief=SOLID, bd=1)
d29.grid(row=13, column=2, sticky="nsew", padx=1, pady=1)
d30 = Label(Detail, text="8 - 30" + "\n" + "14.5", bg="azure", relief=SOLID, bd=1)
d30.grid(row=14, column=2, sticky="nsew", padx=1, pady=1)
d31 = Label(Detail, text="12 - 25" + "\n" + "18.6", bg="azure", relief=SOLID, bd=1)
d31.grid(row=15, column=2, sticky="nsew", padx=1, pady=1)
d32 = Label(Detail, text="12 - 33" + "\n" + "26.6", bg="azure", relief=SOLID, bd=1)
d32.grid(row=16, column=2, sticky="nsew", padx=1, pady=1)

d33 = Label(Detail, text="  Oil Viscosity  " + "\n" + "(cP)",bg="deepskyblue", relief=SOLID, bd=1)
d33.grid(row=0, rowspan=2, column=3, sticky="nsew", padx=1, pady=1)
d34 = Label(Detail, text="0 - 35" + "\n" + "2.1", bg="azure", relief=SOLID, bd=1)
d34.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)
d35 = Label(Detail, text="0 - 18000" + "\n" + "286.1", bg="azure", relief=SOLID, bd=1)
d35.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)
d36 = Label(Detail, text="0.07 - 04 " + "\n" + "0.175", bg="azure", relief=SOLID, bd=1)
d36.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)
d37 = Label(Detail, text="0 - 0.2 " + "\n" + "0.07", bg="azure", relief=SOLID, bd=1)
d37.grid(row=5, column=3, sticky="nsew", padx=1, pady=1)
d38 = Label(Detail, text="0 - 18000 " + "\n" + "2256.8", bg="azure", relief=SOLID, bd=1)
d38.grid(row=6, column=3, sticky="nsew", padx=1, pady=1)
d39 = Label(Detail, text="0.6 - 592 " + "\n" + "65.5", bg="azure", relief=SOLID, bd=1)
d39.grid(row=7, column=3, sticky="nsew", padx=1, pady=1)
d40 = Label(Detail, text="0.25 - 4 " + "\n" + "2.1", bg="azure", relief=SOLID, bd=1)
d40.grid(row=8, column=3, sticky="nsew", padx=1, pady=1)
d41 = Label(Detail, text="0.17 - 16000 " + "\n" + "3948.2", bg="azure", relief=SOLID, bd=1)
d41.grid(row=9, column=3, sticky="nsew", padx=1, pady=1)
d42 = Label(Detail, text="0.4 - 4000 " + "\n" + "123.2", bg="azure", relief=SOLID, bd=1)
d42.grid(row=10, column=3, sticky="nsew", padx=1, pady=1)
d43 = Label(Detail, text="11 - 6500 " + "\n" + "875.8", bg="azure", relief=SOLID, bd=1)
d43.grid(row=11, column=3, sticky="nsew", padx=1, pady=1)
d44 = Label(Detail, text="3 - 15.6 " + "\n" + "9.3", bg="azure", relief=SOLID, bd=1)
d44.grid(row=12, column=3, sticky="nsew", padx=1, pady=1)
d45 = Label(Detail, text="1000 - 5000 " + "\n" + "1200", bg="azure", relief=SOLID, bd=1)
d45.grid(row=13, column=3, sticky="nsew", padx=1, pady=1)
d46 = Label(Detail, text="10 - 5E6 " + "\n" + "32971.3", bg="azure", relief=SOLID, bd=1)
d46.grid(row=14, column=3, sticky="nsew", padx=1, pady=1)
d47 = Label(Detail, text="170 - 8000 " + "\n" + "2002", bg="azure", relief=SOLID, bd=1)
d47.grid(row=15, column=3, sticky="nsew", padx=1, pady=1)
d48 = Label(Detail, text="1.7 - 8900 " + "\n" + "2977.5", bg="azure", relief=SOLID, bd=1)
d48.grid(row=16, column=3, sticky="nsew", padx=1, pady=1)

d49 = Label(Detail, text="     Porosity     " + "\n" + "(%)",bg="deepskyblue", relief=SOLID, bd=1)
d49.grid(row=0,rowspan=2,column=4,sticky="nsew",padx=1,pady=1)
d50 = Label(Detail, text="3 - 7 " + "\n" + "14.8", bg="azure", relief=SOLID, bd=1)
d50.grid(row=2, column=4, sticky="nsew", padx=1, pady=1)
d51 = Label(Detail, text="4.25 - 45 " + "\n" + "14.5", bg="azure", relief=SOLID, bd=1)
d51.grid(row=3, column=4, sticky="nsew", padx=1, pady=1)
d52 = Label(Detail, text="11 - 24 " + "\n" + "18.3", bg="azure", relief=SOLID, bd=1)
d52.grid(row=4, column=4, sticky="nsew", padx=1, pady=1)
d53 = Label(Detail, text="7.5 - 14 " + "\n" + "11.2", bg="azure", relief=SOLID, bd=1)
d53.grid(row=5, column=4, sticky="nsew", padx=1, pady=1)
d54 = Label(Detail, text="11 - 28 " + "\n" + "19.46", bg="azure", relief=SOLID, bd=1)
d54.grid(row=6, column=4, sticky="nsew", padx=1, pady=1)
d55 = Label(Detail, text="17 - 32 " + "\n" + "26.3", bg="azure", relief=SOLID, bd=1)
d55.grid(row=7, column=4, sticky="nsew", padx=1, pady=1)
d56 = Label(Detail, text="5 - 22 " + "\n" + "13.5", bg="azure", relief=SOLID, bd=1)
d56.grid(row=8, column=4, sticky="nsew", padx=1, pady=1)
d57 = Label(Detail, text="18 - 31.9 " + "\n" + "25.09", bg="azure", relief=SOLID, bd=1)
d57.grid(row=9, column=4, sticky="nsew", padx=1, pady=1)
d58 = Label(Detail, text="10.4 - 33 " + "\n" + "22.5", bg="azure", relief=SOLID, bd=1)
d58.grid(row=10, column=4, sticky="nsew", padx=1, pady=1)
d59 = Label(Detail, text="26 - 32 " + "\n" + "26.6", bg="azure", relief=SOLID, bd=1)
d59.grid(row=11, column=4, sticky="nsew", padx=1, pady=1)
d60 = Label(Detail, text="16 - 16.8 " + "\n" + "16.4", bg="azure", relief=SOLID, bd=1)
d60.grid(row=12, column=4, sticky="nsew", padx=1, pady=1)
d61 = Label(Detail, text="14 - 35 " + "\n" + "23.3", bg="azure", relief=SOLID, bd=1)
d61.grid(row=13, column=4, sticky="nsew", padx=1, pady=1)
d62 = Label(Detail, text="12 - 65 " + "\n" + "32.2", bg="azure", relief=SOLID, bd=1)
d62.grid(row=14, column=4, sticky="nsew", padx=1, pady=1)
d63 = Label(Detail, text="25 - 37 " + "\n" + "31.2", bg="azure", relief=SOLID, bd=1)
d63.grid(row=15, column=4, sticky="nsew", padx=1, pady=1)
d64 = Label(Detail, text="12 - 26 " + "\n" + "19", bg="azure", relief=SOLID, bd=1)
d64.grid(row=16, column=4, sticky="nsew", padx=1, pady=1)

d65 = Label(Detail, text="   Oil Saturation   " + "\n" + "(% PV)",bg="deepskyblue", relief=SOLID, bd=1)
d65.grid(row=0,rowspan=2,column=5, sticky="nsew",padx=1,pady=1)
d66 = Label(Detail, text="15 - 89 " + "\n" + "46", bg="azure", relief=SOLID, bd=1)
d66.grid(row=2, column=5, sticky="nsew", padx=1, pady=1)
d67 = Label(Detail, text="30 - 98 " + "\n" + "71", bg="azure", relief=SOLID, bd=1)
d67.grid(row=3, column=5, sticky="nsew", padx=1, pady=1)
d68 = Label(Detail, text="40 - 80 " + "\n" + "75", bg="azure", relief=SOLID, bd=1)
d68.grid(row=4, column=5, sticky="nsew", padx=1, pady=1)
d69 = Label(Detail, text="40 - 80" + "\n" + "78", bg="azure", relief=SOLID, bd=1)
d69.grid(row=5, column=5, sticky="nsew", padx=1, pady=1)
d70 = Label(Detail, text="47 - 98.5 " + "\n" + "71", bg="azure", relief=SOLID, bd=1)
d70.grid(row=6, column=5, sticky="nsew", padx=1, pady=1)
d71 = Label(Detail, text="42 - 78 " + "\n" + "56", bg="azure", relief=SOLID, bd=1)
d71.grid(row=7, column=5, sticky="nsew", padx=1, pady=1)
d72 = Label(Detail, text="75 - 83 " + "\n" + "79", bg="azure", relief=SOLID, bd=1)
d72.grid(row=8, column=5, sticky="nsew", padx=1, pady=1)
d73 = Label(Detail, text="35 - 83 " + "\n" + "88", bg="azure", relief=SOLID, bd=1)
d73.grid(row=9, column=5, sticky="nsew", padx=1, pady=1)
d74 = Label(Detail, text="34 - 82 " + "\n" + "64", bg="azure", relief=SOLID, bd=1)
d74.grid(row=10, column=5, sticky="nsew", padx=1, pady=1)
d75 = Label(Detail, text="35 - 74.8 " + "\n" + "73.7", bg="azure", relief=SOLID, bd=1)
d75.grid(row=11, column=5, sticky="nsew", padx=1, pady=1)
d76 = Label(Detail, text="43.5 - 53 " + "\n" + "48", bg="azure", relief=SOLID, bd=1)
d76.grid(row=12, column=5, sticky="nsew", padx=1, pady=1)
d77 = Label(Detail, text="50 - 94 " + "\n" + "67", bg="azure", relief=SOLID, bd=1)
d77.grid(row=13, column=5, sticky="nsew", padx=1, pady=1)
d78 = Label(Detail, text="35 - 90 " + "\n" + "66", bg="azure", relief=SOLID, bd=1)
d78.grid(row=14, column=5, sticky="nsew", padx=1, pady=1)
d79 = Label(Detail, text="15 - 85 " + "\n" + "58.5", bg="azure", relief=SOLID, bd=1)
d79.grid(row=15, column=5, sticky="nsew", padx=1, pady=1)
d80 = Label(Detail, text="55 - 65 " + "\n" + "60", bg="azure", relief=SOLID, bd=1)
d80.grid(row=16, column=5, sticky="nsew", padx=1, pady=1)

d81 = Label(Detail, text="   Formation Type   ",bg="deepskyblue", relief=SOLID, bd=1)
d81.grid(row=0,rowspan=2,column=6,sticky="nsew",padx=1,pady=1)
d82 = Label(Detail, text="Sandstone or" + "\n" + "Carbonate", bg="azure", relief=SOLID, bd=1)
d82.grid(row=2, column=6, sticky="nsew", padx=1, pady=1)
d83 = Label(Detail, text="Sandstone or" + "\n" + "Carbonate", bg="azure", relief=SOLID, bd=1)
d83.grid(row=3, column=6, sticky="nsew", padx=1, pady=1)
d84 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d84.grid(row=4, column=6, sticky="nsew", padx=1, pady=1)
d85 = Label(Detail, text="Sandstone or" + "\n" + "Carbonaten", bg="azure", relief=SOLID, bd=1)
d85.grid(row=5, column=6, sticky="nsew", padx=1, pady=1)
d86 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d86.grid(row=6, column=6, sticky="nsew", padx=1, pady=1)
d87 = Label(Detail, text="Sandstone or" + "\n" + "Carbonate", bg="azure", relief=SOLID, bd=1)
d87.grid(row=7, column=6, sticky="nsew", padx=1, pady=1)
d88 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d88.grid(row=8, column=6, sticky="nsew", padx=1, pady=1)
d89 = Label(Detail, text="Sandstone or" + "\n" + "Carbonate", bg="azure", relief=SOLID, bd=1)
d89.grid(row=9, column=6, sticky="nsew", padx=1, pady=1)
d90 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d90.grid(row=10, column=6, sticky="nsew", padx=1, pady=1)
d91 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d91.grid(row=11, column=6, sticky="nsew", padx=1, pady=1)
d92 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d92.grid(row=12, column=6, sticky="nsew", padx=1, pady=1)
d93 = Label(Detail, text="Sandstone or" + "\n" + "Carbonate", bg="azure", relief=SOLID, bd=1)
d93.grid(row=13, column=6, sticky="nsew", padx=1, pady=1)
d94 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d94.grid(row=14, column=6, sticky="nsew", padx=1, pady=1)
d95 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d95.grid(row=15, column=6, sticky="nsew", padx=1, pady=1)
d96 = Label(Detail, text="Sandstone", bg="azure", relief=SOLID, bd=1)
d96.grid(row=16, column=6, sticky="nsew", padx=1, pady=1)

d97 = Label(Detail, text="  Permeability  " + "\n" + "(mD)",bg="deepskyblue", relief=SOLID, bd=1)
d97.grid(row=0,rowspan=2,column=7,sticky="nsew",padx=1,pady=1)
d98 = Label(Detail, text="1.5 - 4500 " + "\n" + "201.1", bg="azure", relief=SOLID, bd=1)
d98.grid(row=2, column=7, sticky="nsew", padx=1, pady=1)
d99 = Label(Detail, text="0.1 - 5000 " + "\n" + "726.2", bg="azure", relief=SOLID, bd=1)
d99.grid(row=3, column=7, sticky="nsew", padx=1, pady=1)
d100 = Label(Detail, text="130 - 1000 " + "\n" + "143.3", bg="azure", relief=SOLID, bd=1)
d100.grid(row=4, column=7, sticky="nsew", padx=1, pady=1)
d101 = Label(Detail, text="0.2 - 35 " + "\n" + "15.0", bg="azure", relief=SOLID, bd=1)
d101.grid(row=5, column=7, sticky="nsew", padx=1, pady=1)
d102 = Label(Detail, text="3 - 2800 " + "\n" + "1041.7", bg="azure", relief=SOLID, bd=1)
d102.grid(row=6, column=7, sticky="nsew", padx=1, pady=1)
d103 = Label(Detail, text="30 - 1000 " + "\n" + "217", bg="azure", relief=SOLID, bd=1)
d103.grid(row=7, column=7, sticky="nsew", padx=1, pady=1)
d104 = Label(Detail, text="40 - 1000 " + "\n" + "520", bg="azure", relief=SOLID, bd=1)
d104.grid(row=8, column=7, sticky="nsew", padx=1, pady=1)
d105 = Label(Detail, text="100 - 6600 " + "\n" + "2392", bg="azure", relief=SOLID, bd=1)
d105.grid(row=9, column=7, sticky="nsew", padx=1, pady=1)
d106 = Label(Detail, text="1.8 - 5500 " + "\n" + "834.1", bg="azure", relief=SOLID, bd=1)
d106.grid(row=10, column=7, sticky="nsew", padx=1, pady=1)
d107 = Label(Detail, text="10 - 1520 " + "\n" + "486,5", bg="azure", relief=SOLID, bd=1)
d107.grid(row=11, column=7, sticky="nsew", padx=1, pady=1)
d108 = Label(Detail, text="50 - 60 " + "\n" + "55", bg="azure", relief=SOLID, bd=1)
d108.grid(row=12, column=7, sticky="nsew", padx=1, pady=1)
d109 = Label(Detail, text="10 - 15000 " + "\n" + "1981.5", bg="azure", relief=SOLID, bd=1)
d109.grid(row=13, column=7, sticky="nsew", padx=1, pady=1)
d110 = Label(Detail, text="1 - 15000 " + "\n" + "2605.7", bg="azure", relief=SOLID, bd=1)
d110.grid(row=14, column=7, sticky="nsew", padx=1, pady=1)
d111 = Label(Detail, text="900 - 6000 " + "\n" + "3346", bg="azure", relief=SOLID, bd=1)
d111.grid(row=15, column=7, sticky="nsew", padx=1, pady=1)
d112 = Label(Detail, text="180 - 200 " + "\n" + "190", bg="azure", relief=SOLID, bd=1)
d112.grid(row=16, column=7, sticky="nsew", padx=1, pady=1)

d113 = Label(Detail, text="  Net Thickness  " + "\n" + "(ft)",bg="deepskyblue", relief=SOLID, bd=1)
d113.grid(row=0, rowspan=2, column=8,sticky="nsew",padx=1,pady=1)
d114 = Label(Detail, text="[Wide Range]", bg="azure", relief=SOLID, bd=1)
d114.grid(row=2, column=8, sticky="nsew", padx=1, pady=1)
d115 = Label(Detail, text="[Thin unless" + "\n" + "dipping]", bg="azure", relief=SOLID, bd=1)
d115.grid(row=3, column=8, sticky="nsew", padx=1, pady=1)
d116 = Label(Detail, text="NC", bg="azure", relief=SOLID, bd=1)
d116.grid(row=4, column=8, sticky="nsew", padx=1, pady=1)
d117 = Label(Detail, text="[Thin unless" + "\n" + "dipping]", bg="azure", relief=SOLID, bd=1)
d117.grid(row=5, column=8, sticky="nsew", padx=1, pady=1)
d118 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d118.grid(row=6, column=8, sticky="nsew", padx=1, pady=1)
d119 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d119.grid(row=7, column=8, sticky="nsew", padx=1, pady=1)
d120 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d120.grid(row=8, column=8, sticky="nsew", padx=1, pady=1)
d121 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d121.grid(row=9, column=8, sticky="nsew", padx=1, pady=1)
d122 = Label(Detail, text="[NC]", bg="azure", relief=SOLID, bd=1)
d122.grid(row=10, column=8, sticky="nsew", padx=1, pady=1)
d123 = Label(Detail, text="[NC]", bg="azure", relief=SOLID, bd=1)
d123.grid(row=11, column=8, sticky="nsew", padx=1, pady=1)
d124 = Label(Detail, text="[NC]", bg="azure", relief=SOLID, bd=1)
d124.grid(row=12, column=8, sticky="nsew", padx=1, pady=1)
d125 = Label(Detail, text="[>10]]", bg="azure", relief=SOLID, bd=1)
d125.grid(row=13, column=8, sticky="nsew", padx=1, pady=1)
d126 = Label(Detail, text="[>20]]", bg="azure", relief=SOLID, bd=1)
d126.grid(row=14, column=8, sticky="nsew", padx=1, pady=1)
d127 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d127.grid(row=15, column=8, sticky="nsew", padx=1, pady=1)
d128 = Label(Detail, text="-", bg="azure", relief=SOLID, bd=1)
d128.grid(row=16, column=8, sticky="nsew", padx=1, pady=1)

d129 = Label(Detail, text="      Depth (ft)       ",bg="deepskyblue", relief=SOLID, bd=1)
d129.grid(row=0,rowspan=2,column=9,sticky="nsew",padx=1,pady=1)
d130 = Label(Detail, text="1500 - 13365 " + "\n" + "6171.2", bg="azure", relief=SOLID, bd=1)
d130.grid(row=2, column=9, sticky="nsew", padx=1, pady=1)
d131 = Label(Detail, text="4000 - 15900 " + "\n" + "8343.6", bg="azure", relief=SOLID, bd=1)
d131.grid(row=3, column=9, sticky="nsew", padx=1, pady=1)
d132 = Label(Detail, text="7545 - 8887 " + "\n" + "8216.8", bg="azure", relief=SOLID, bd=1)
d132.grid(row=4, column=9, sticky="nsew", padx=1, pady=1)
d133 = Label(Detail, text="6000 - 18500 " + "\n" + "14633.3", bg="azure", relief=SOLID, bd=1)
d133.grid(row=5, column=9, sticky="nsew", padx=1, pady=1)
d134 = Label(Detail, text="1700 - 18500" + "\n" + "7914.2", bg="azure", relief=SOLID, bd=1)
d134.grid(row=6, column=9, sticky="nsew", padx=1, pady=1)
d135 = Label(Detail, text="1150 - 8500 " + "\n" + "3385", bg="azure", relief=SOLID, bd=1)
d135.grid(row=7, column=9, sticky="nsew", padx=1, pady=1)
d136 = Label(Detail, text="6000 - 7000" + "\n" + "6500", bg="azure", relief=SOLID, bd=1)
d136.grid(row=8, column=9, sticky="nsew", padx=1, pady=1)
d137 = Label(Detail, text="2650 - 9199 " + "\n" + "7218.71", bg="azure", relief=SOLID, bd=1)
d137.grid(row=9, column=9, sticky="nsew", padx=1, pady=1)
d138 = Label(Detail, text="700 - 9460 " + "\n" + "4221.9", bg="azure", relief=SOLID, bd=1)
d138.grid(row=10, column=9, sticky="nsew", padx=1, pady=1)
d139 = Label(Detail, text="2723 - 9000 " + "\n" + "2984.5", bg="azure", relief=SOLID, bd=1)
d139.grid(row=11, column=9, sticky="nsew", padx=1, pady=1)
d140 = Label(Detail, text="625 - 5300 " + "\n" + "2941.6", bg="azure", relief=SOLID, bd=1)
d140.grid(row=12, column=9, sticky="nsew", padx=1, pady=1)
d141 = Label(Detail, text="400 - 11300 " + "\n" + "5569.6", bg="azure", relief=SOLID, bd=1)
d141.grid(row=13, column=9, sticky="nsew", padx=1, pady=1)
d142 = Label(Detail, text="200 - 9000 " + "\n" + "1643.6", bg="azure", relief=SOLID, bd=1)
d142.grid(row=14, column=9, sticky="nsew", padx=1, pady=1)
d143 = Label(Detail, text="500 - 2950 " + "\n" + "1942", bg="azure", relief=SOLID, bd=1)
d143.grid(row=15, column=9, sticky="nsew", padx=1, pady=1)
d144 = Label(Detail, text="1572 - 3464 " + "\n" + "2445.3", bg="azure", relief=SOLID, bd=1)
d144.grid(row=16, column=9, sticky="nsew", padx=1, pady=1)

d145 = Label(Detail, text="    Temperature    " + "\n" + "(deg F)",bg="deepskyblue", relief=SOLID, bd=1)
d145.grid(row=0,rowspan=2,column=10,sticky="nsew",padx=1,pady=1)
d146 = Label(Detail, text="82 - 250 " + "\n" + "136.3", bg="azure", relief=SOLID, bd=1)
d146.grid(row=2, column=10, sticky="nsew", padx=1, pady=1)
d147 = Label(Detail, text="85 - 329 " + "\n" + "202.2", bg="azure", relief=SOLID, bd=1)
d147.grid(row=3, column=10, sticky="nsew", padx=1, pady=1)
d148 = Label(Detail, text="194 - 253 " + "\n" + "229.4", bg="azure", relief=SOLID, bd=1)
d148.grid(row=4, column=10, sticky="nsew", padx=1, pady=1)
d149 = Label(Detail, text="190 - 325 " + "\n" + "266.6", bg="azure", relief=SOLID, bd=1)
d149.grid(row=5, column=10, sticky="nsew", padx=1, pady=1)
d150 = Label(Detail, text="82 - 325 " + "\n" + "173.1", bg="azure", relief=SOLID, bd=1)
d150.grid(row=6, column=10, sticky="nsew", padx=1, pady=1)
d151 = Label(Detail, text="82 - 198 " + "\n" + "124", bg="azure", relief=SOLID, bd=1)
d151.grid(row=7, column=10, sticky="nsew", padx=1, pady=1)
d152 = Label(Detail, text="170 - 180 " + "\n" + "175", bg="azure", relief=SOLID, bd=1)
d152.grid(row=8, column=10, sticky="nsew", padx=1, pady=1)
d153 = Label(Detail, text="131 - 267 " + "\n" + "198.7", bg="azure", relief=SOLID, bd=1)
d153.grid(row=9, column=10, sticky="nsew", padx=1, pady=1)
d154 = Label(Detail, text="74 – 237.2 " + "\n" + "167", bg="azure", relief=SOLID, bd=1)
d154.grid(row=10, column=10, sticky="nsew", padx=1, pady=1)
d155 = Label(Detail, text="80 - 200 " + "\n" + "121.6", bg="azure", relief=SOLID, bd=1)
d155.grid(row=11, column=10, sticky="nsew", padx=1, pady=1)
d156 = Label(Detail, text="122 - 155 " + "\n" + "138.5", bg="azure", relief=SOLID, bd=1)
d156.grid(row=12, column=10, sticky="nsew", padx=1, pady=1)
d157 = Label(Detail, text="64.4 - 230 " + "\n" + "175.5", bg="azure", relief=SOLID, bd=1)
d157.grid(row=13, column=10, sticky="nsew", padx=1, pady=1)
d158 = Label(Detail, text="10 - 350 " + "\n" + "105.8", bg="azure", relief=SOLID, bd=1)
d158.grid(row=14, column=10, sticky="nsew", padx=1, pady=1)
d159 = Label(Detail, text="75 - 135 " + "\n" + "98.5", bg="azure", relief=SOLID, bd=1)
d159.grid(row=15, column=10, sticky="nsew", padx=1, pady=1)
d160 = Label(Detail, text="86 - 90 " + "\n" + "88", bg="azure", relief=SOLID, bd=1)
d160.grid(row=16, column=10, sticky="nsew", padx=1, pady=1)

d161 = Label(Detail, text=" " + "\n" + " " + "\n" + " ", bg="aliceblue")
d161.grid(row=17, rowspan=5, column=0, sticky="nsew", padx=1, pady=1)
d162 = Label(Detail, text=" ", bg="green4", relief=SOLID, bd=1)
d162.grid(row=22, column=0, sticky="nsew", padx=1, pady=1)
d1621 = Label(Detail, text="Well Match", bg="aliceblue")
d1621.grid(row=22, column=1, sticky="w", padx=1, pady=1)
d163 = Label(Detail, text=" ", bg="green2", relief=SOLID, bd=1)
d163.grid(row=23, column=0, sticky="nsew", padx=1, pady=1)
d1631 = Label(Detail, text="Average Match", bg="aliceblue")
d1631.grid(row=23, column=1, sticky="w", padx=1, pady=1)
d164 = Label(Detail, text=" ", bg="green yellow", relief=SOLID, bd=1)
d164.grid(row=24, column=0, sticky="nsew", padx=1, pady=1)
d1641 = Label(Detail, text="Just Match", bg="aliceblue")
d1641.grid(row=24, column=1, sticky="w", padx=1, pady=1)
d165 = Label(Detail, text=" ", bg="firebrick1", relief=SOLID, bd=1)
d165.grid(row=25, column=0, sticky="nsew", padx=1, pady=1)
d1651 = Label(Detail, text="Not Match", bg="aliceblue")
d1651.grid(row=25, column=1, sticky="w", padx=1, pady=1)

#=====================================WEIGHT FACTOR====================================================
#=====================================WEIGHT FACTOR====================================================
#=====================================WEIGHT FACTOR====================================================

f1 = Label(WF, text="EOR Method",bg="deepskyblue", relief=SOLID, bd=1)
f1.grid(row=0,column=1,sticky="nsew",padx=1,pady=1)
f2 = Label(WF, text="Miscible Gas Inj.: CO2", bg="deepskyblue", relief=SOLID, bd=1)
f2.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
f3 = Label(WF, text="Miscible Gas Inj.: Hydrocarbon", bg="deepskyblue", relief=SOLID, bd=1)
f3.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
f4 = Label(WF, text="Miscible Gas Inj.: WAG", bg="deepskyblue", relief=SOLID, bd=1)
f4.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
f5 = Label(WF, text="Miscible Gas Inj.: Nitrogen", bg="deepskyblue", relief=SOLID, bd=1)
f5.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)
f6 = Label(WF, text="Immiscible Gas Inj.: Nitrogen", bg="deepskyblue", relief=SOLID, bd=1)
f6.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)
f7 = Label(WF, text="Immiscible Gas Inj.: CO2", bg="deepskyblue", relief=SOLID, bd=1)
f7.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)
f8 = Label(WF, text="Immiscible Gas Inj.: Hydrocarbon", bg="deepskyblue", relief=SOLID, bd=1)
f8.grid(row=7, column=1, sticky="nsew", padx=1, pady=1)
f9 = Label(WF, text="Immiscible Gas Inj.: Hydrocarbon + WAG", bg="deepskyblue", relief=SOLID, bd=1)
f9.grid(row=8, column=1, sticky="nsew", padx=1, pady=1)
f10 = Label(WF, text="Enh. Waterflooding: Polymer", bg="deepskyblue", relief=SOLID, bd=1)
f10.grid(row=9, column=1, sticky="nsew", padx=1, pady=1)
f11 = Label(WF, text="Enh. Waterflooding: Alkaline Surfactant" + "\n" + "Polymer (ASP)", bg="deepskyblue", relief=SOLID, bd=1)
f11.grid(row=10, column=1, sticky="nsew", padx=1, pady=1)
f12 = Label(WF, text="Enh. Waterflooding: Surfactant" + "\n" + "+ Polymer/Alkaline", bg="deepskyblue", relief=SOLID, bd=1)
f12.grid(row=11, column=1, sticky="nsew", padx=1, pady=1)
f13 = Label(WF, text="Thermal/Mech: Combustion", bg="deepskyblue", relief=SOLID, bd=1)
f13.grid(row=12, column=1, sticky="nsew", padx=1, pady=1)
f14 = Label(WF, text="Thermal/Mech: Steam", bg="deepskyblue", relief=SOLID, bd=1)
f14.grid(row=13, column=1, sticky="nsew", padx=1, pady=1)
f15 = Label(WF, text="Thermal/Mech: Hot Water", bg="deepskyblue", relief=SOLID, bd=1)
f15.grid(row=14, column=1, sticky="nsew", padx=1, pady=1)
f16 = Label(WF, text="Microbial", bg="deepskyblue", relief=SOLID, bd=1)
f16.grid(row=15, column=1, sticky="nsew", padx=1, pady=1)

f17 = Label(WF, text="  Oil API Gravity  ",bg="deepskyblue", relief=SOLID, bd=1)
f17.grid(row=0,column=2,sticky="nsew",padx=1,pady=1)
s1 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api1, width=13, bg="azure", justify='center')
s1.insert(0, "3")
s1.grid(row=1, column=2)
s2 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api2, width=13, bg="azure", justify='center')
s2.insert(0, "1")
s2.grid(row=2, column=2)
s3 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api3, width=13, bg="azure", justify='center')
s3.insert(0, "1")
s3.grid(row=3, column=2)
s4 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api4, width=13, bg="azure", justify='center')
s4.insert(0, "1")
s4.grid(row=4, column=2)
s5 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api5, width=13, bg="azure", justify='center')
s5.insert(0, "1")
s5.grid(row=5, column=2)
s6 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api6, width=13, bg="azure", justify='center')
s6.insert(0, "3")
s6.grid(row=6, column=2)
s7 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api7, width=13, bg="azure", justify='center')
s7.insert(0, "2")
s7.grid(row=7, column=2)
s8 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api8, width=13, bg="azure", justify='center')
s8.insert(0, "1")
s8.grid(row=8, column=2)
s9 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api9, width=13, bg="azure", justify='center')
s9.insert(0, "1")
s9.grid(row=9, column=2)
s10 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api10, width=13, bg="azure", justify='center')
s10.insert(0, "1")
s10.grid(row=10, column=2)
s11 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api11, width=13, bg="azure", justify='center')
s11.insert(0, "1")
s11.grid(row=11, column=2)
s12 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api12, width=13, bg="azure", justify='center')
s12.insert(0, "3")
s12.grid(row=12, column=2)
s13 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api13, width=13, bg="azure", justify='center')
s13.insert(0, "3")
s13.grid(row=13, column=2)
s14 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api14, width=13, bg="azure", justify='center')
s14.insert(0, "3")
s14.grid(row=14, column=2)
s15 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_api15, width=13, bg="azure", justify='center')
s15.insert(0, "1")
s15.grid(row=15, column=2)


f33 = Label(WF, text="  Oil Viscosity (cP)  ",bg="deepskyblue", relief=SOLID, bd=1)
f33.grid(row=0,column=3,sticky="nsew",padx=1,pady=1)
s16 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis1, width=15, bg="azure", justify='center')
s16.insert(0, "1")
s16.grid(row=1, column=3)
s17 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis2, width=15, bg="azure", justify='center')
s17.insert(0, "1")
s17.grid(row=2, column=3)
s18 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis3, width=15, bg="azure", justify='center')
s18.insert(0, "1")
s18.grid(row=3, column=3)
s19 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis4, width=15, bg="azure", justify='center')
s19.insert(0, "1")
s19.grid(row=4, column=3)
s20 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis5, width=15, bg="azure", justify='center')
s20.insert(0, "1")
s20.grid(row=5, column=3)
s21 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis6, width=15, bg="azure", justify='center')
s21.insert(0, "1")
s21.grid(row=6, column=3)
s22 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis7, width=15, bg="azure", justify='center')
s22.insert(0, "1")
s22.grid(row=7, column=3)
s23 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis8, width=15, bg="azure", justify='center')
s23.insert(0, "1")
s23.grid(row=8, column=3)
s24 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis9, width=15, bg="azure", justify='center')
s24.insert(0, "1")
s24.grid(row=9, column=3)
s25 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis10, width=15, bg="azure", justify='center')
s25.insert(0, "1")
s25.grid(row=10, column=3)
s26 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis11, width=15, bg="azure", justify='center')
s26.insert(0, "1")
s26.grid(row=11, column=3)
s27 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis12, width=15, bg="azure", justify='center')
s27.insert(0, "3")
s27.grid(row=12, column=3)
s28 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis13, width=15, bg="azure", justify='center')
s28.insert(0, "3")
s28.grid(row=13, column=3)
s29 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis14, width=15, bg="azure", justify='center')
s29.insert(0, "2")
s29.grid(row=14, column=3)
s30 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_vis15, width=15, bg="azure", justify='center')
s30.insert(0, "1")
s30.grid(row=15, column=3)

f31 = Label(WF, text=" Porosity (%) ",bg="deepskyblue", relief=SOLID, bd=1)
f31.grid(row=0,column=4,sticky="nsew",padx=1,pady=1)
s31 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por1, width=13, bg="azure", justify='center')
s31.insert(0, "1")
s31.grid(row=1, column=4)
s32 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por2, width=13, bg="azure", justify='center')
s32.insert(0, "1")
s32.grid(row=2, column=4)
s33 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por3, width=13, bg="azure", justify='center')
s33.insert(0, "1")
s33.grid(row=3, column=4)
s34 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por4, width=13, bg="azure", justify='center')
s34.insert(0, "1")
s34.grid(row=4, column=4)
s35 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por5, width=13, bg="azure", justify='center')
s35.insert(0, "1")
s35.grid(row=5, column=4)
s36 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por6, width=13, bg="azure", justify='center')
s36.insert(0, "1")
s36.grid(row=6, column=4)
s37 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por7, width=13, bg="azure", justify='center')
s37.insert(0, "1")
s37.grid(row=7, column=4)
s38 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por8, width=13, bg="azure", justify='center')
s38.insert(0, "1")
s38.grid(row=8, column=4)
s39 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por9, width=13, bg="azure", justify='center')
s39.insert(0, "1")
s39.grid(row=9, column=4)
s40 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por10, width=13, bg="azure", justify='center')
s40.insert(0, "1")
s40.grid(row=10, column=4)
s41 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por11, width=13, bg="azure", justify='center')
s41.insert(0, "1")
s41.grid(row=11, column=4)
s42 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por12, width=13, bg="azure", justify='center')
s42.insert(0, "1")
s42.grid(row=12, column=4)
s43 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por13, width=13, bg="azure", justify='center')
s43.insert(0, "1")
s43.grid(row=13, column=4)
s44 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por14, width=13, bg="azure", justify='center')
s44.insert(0, "1")
s44.grid(row=14, column=4)
s45 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_por15, width=13, bg="azure", justify='center')
s45.insert(0, "1")
s45.grid(row=15, column=4)

f65 = Label(WF, text=" Oil Saturation " + "\n" + "(% PV)",bg="deepskyblue", relief=SOLID, bd=1)
f65.grid(row=0,column=5,sticky="nsew",padx=1,pady=1)
s46 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat1, width=13, bg="azure", justify='center')
s46.insert(0, "1")
s46.grid(row=1, column=5)
s47 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat2, width=13, bg="azure", justify='center')
s47.insert(0, "1")
s47.grid(row=2, column=5)
s48 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat3, width=13, bg="azure", justify='center')
s48.insert(0, "1")
s48.grid(row=3, column=5)
s49 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat4, width=13, bg="azure", justify='center')
s49.insert(0, "1")
s49.grid(row=4, column=5)
s50 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat5, width=13, bg="azure", justify='center')
s50.insert(0, "1")
s50.grid(row=5, column=5)
s51 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat6, width=13, bg="azure", justify='center')
s51.insert(0, "1")
s51.grid(row=6, column=5)
s52 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat7, width=13, bg="azure", justify='center')
s52.insert(0, "1")
s52.grid(row=7, column=5)
s53 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat8, width=13, bg="azure", justify='center')
s53.insert(0, "1")
s53.grid(row=8, column=5)
s54 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat9, width=13, bg="azure", justify='center')
s54.insert(0, "1")
s54.grid(row=9, column=5)
s55 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat10, width=13, bg="azure", justify='center')
s55.insert(0, "1")
s55.grid(row=10, column=5)
s56 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat11, width=13, bg="azure", justify='center')
s56.insert(0, "1")
s56.grid(row=11, column=5)
s57 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat12, width=13, bg="azure", justify='center')
s57.insert(0, "1")
s57.grid(row=12, column=5)
s58 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat13, width=13, bg="azure", justify='center')
s58.insert(0, "1")
s58.grid(row=13, column=5)
s59 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat14, width=13, bg="azure", justify='center')
s59.insert(0, "1")
s59.grid(row=14, column=5)
s60 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_sat15, width=13, bg="azure", justify='center')
s60.insert(0, "1")
s60.grid(row=15, column=5)

f81 = Label(WF, text=" Formation Type ",bg="deepskyblue", relief=SOLID, bd=1)
f81.grid(row=0,column=6,sticky="nsew",padx=1,pady=1)
s61 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for1, width=13, bg="azure", justify='center')
s61.insert(0, "1")
s61.grid(row=1, column=6)
s62 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for2, width=13, bg="azure", justify='center')
s62.insert(0, "1")
s62.grid(row=2, column=6)
s63 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for3, width=13, bg="azure", justify='center')
s63.insert(0, "1")
s63.grid(row=3, column=6)
s64 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for4, width=13, bg="azure", justify='center')
s64.insert(0, "1")
s64.grid(row=4, column=6)
s65 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for5, width=13, bg="azure", justify='center')
s65.insert(0, "1")
s65.grid(row=5, column=6)
s66 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for6, width=13, bg="azure", justify='center')
s66.insert(0, "1")
s66.grid(row=6, column=6)
s67 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for7, width=13, bg="azure", justify='center')
s67.insert(0, "1")
s67.grid(row=7, column=6)
s68 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for8, width=13, bg="azure", justify='center')
s68.insert(0, "1")
s68.grid(row=8, column=6)
s69 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for9, width=13, bg="azure", justify='center')
s69.insert(0, "1")
s69.grid(row=9, column=6)
s70 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for10, width=13, bg="azure", justify='center')
s70.insert(0, "1")
s70.grid(row=10, column=6)
s71 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for11, width=13, bg="azure", justify='center')
s71.insert(0, "1")
s71.grid(row=11, column=6)
s72 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for12, width=13, bg="azure", justify='center')
s72.insert(0, "1")
s72.grid(row=12, column=6)
s73 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for13, width=13, bg="azure", justify='center')
s73.insert(0, "1")
s73.grid(row=13, column=6)
s74 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for14, width=13, bg="azure", justify='center')
s74.insert(0, "1")
s74.grid(row=14, column=6)
s75 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_for15, width=13, bg="azure", justify='center')
s75.insert(0, "1")
s75.grid(row=15, column=6)

f97 = Label(WF, text="Permeability (mD) ",bg="deepskyblue", relief=SOLID, bd=1)
f97.grid(row=0,column=7,sticky="nsew",padx=1,pady=1)
s76 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per1, width=15, bg="azure", justify='center')
s76.insert(0, "1")
s76.grid(row=1, column=7)
s77 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per2, width=15, bg="azure", justify='center')
s77.insert(0, "1")
s77.grid(row=2, column=7)
s78 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per3, width=15, bg="azure", justify='center')
s78.insert(0, "1")
s78.grid(row=3, column=7)
s79 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per4, width=15, bg="azure", justify='center')
s79.insert(0, "1")
s79.grid(row=4, column=7)
s80 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per5, width=15, bg="azure", justify='center')
s80.insert(0, "1")
s80.grid(row=5, column=7)
s81 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per6, width=15, bg="azure", justify='center')
s81.insert(0, "1")
s81.grid(row=6, column=7)
s82 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per7, width=15, bg="azure", justify='center')
s82.insert(0, "1")
s82.grid(row=7, column=7)
s83 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per8, width=15, bg="azure", justify='center')
s83.insert(0, "1")
s83.grid(row=8, column=7)
s84 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per9, width=15, bg="azure", justify='center')
s84.insert(0, "1")
s84.grid(row=9, column=7)
s85 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per10, width=15, bg="azure", justify='center')
s85.insert(0, "1")
s85.grid(row=10, column=7)
s86 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per11, width=15, bg="azure", justify='center')
s86.insert(0, "1")
s86.grid(row=11, column=7)
s87 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per12, width=15, bg="azure", justify='center')
s87.insert(0, "1")
s87.grid(row=12, column=7)
s88 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per13, width=15, bg="azure", justify='center')
s88.insert(0, "1")
s88.grid(row=13, column=7)
s89 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per14, width=15, bg="azure", justify='center')
s89.insert(0, "1")
s89.grid(row=14, column=7)
s90 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_per15, width=15, bg="azure", justify='center')
s90.insert(0, "1")
s90.grid(row=15, column=7)

f113 = Label(WF, text="  Net Thickness (ft)  ",bg="deepskyblue", relief=SOLID, bd=1)
f113.grid(row=0,column=8,sticky="nsew",padx=1,pady=1)
s91 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi1, width=15, bg="azure", justify='center')
s91.insert(0, "0")
s91.grid(row=1, column=8)
s92 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi2, width=15, bg="azure", justify='center')
s92.insert(0, "1")
s92.grid(row=2, column=8)
s93 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi3, width=15, bg="azure", justify='center')
s93.insert(0, "0")
s93.grid(row=3, column=8)
s94 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi4, width=15, bg="azure", justify='center')
s94.insert(0, "1")
s94.grid(row=4, column=8)
s95 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi5, width=15, bg="azure", justify='center')
s95.insert(0, "0")
s95.grid(row=5, column=8)
s96 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi6, width=15, bg="azure", justify='center')
s96.insert(0, "0")
s96.grid(row=6, column=8)
s97 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi7, width=15, bg="azure", justify='center')
s97.insert(0, "0")
s97.grid(row=7, column=8)
s98 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi8, width=15, bg="azure", justify='center')
s98.insert(0, "0")
s98.grid(row=8, column=8)
s99 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi9, width=15, bg="azure", justify='center')
s99.insert(0, "0")
s99.grid(row=9, column=8)
s100 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi10, width=15, bg="azure", justify='center')
s100.insert(0, "0")
s100.grid(row=10, column=8)
s101 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi11, width=15, bg="azure", justify='center')
s101.insert(0, "0")
s101.grid(row=11, column=8)
s102 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi12, width=15, bg="azure", justify='center')
s102.insert(0, "1")
s102.grid(row=12, column=8)
s103 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi13, width=15, bg="azure", justify='center')
s103.insert(0, "1")
s103.grid(row=13, column=8)
s104 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi14, width=15, bg="azure", justify='center')
s104.insert(0, "0")
s104.grid(row=14, column=8)
s105 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_thi15, width=15, bg="azure", justify='center')
s105.insert(0, "0")
s105.grid(row=15, column=8)

f129 = Label(WF, text="  Depth (ft) ",bg="deepskyblue", relief=SOLID, bd=1)
f129.grid(row=0,column=9,sticky="nsew",padx=1,pady=1)
s106 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep1, width=13, bg="azure", justify='center')
s106.insert(0, "1")
s106.grid(row=1, column=9)
s107 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep2, width=13, bg="azure", justify='center')
s107.insert(0, "1")
s107.grid(row=2, column=9)
s108 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep3, width=13, bg="azure", justify='center')
s108.insert(0, "1")
s108.grid(row=3, column=9)
s109 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep4, width=13, bg="azure", justify='center')
s109.insert(0, "1")
s109.grid(row=4, column=9)
s110 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep5, width=13, bg="azure", justify='center')
s110.insert(0, "1")
s110.grid(row=5, column=9)
s111 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep6, width=13, bg="azure", justify='center')
s111.insert(0, "1")
s111.grid(row=6, column=9)
s112 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep7, width=13, bg="azure", justify='center')
s112.insert(0, "1")
s112.grid(row=7, column=9)
s113 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep8, width=13, bg="azure", justify='center')
s113.insert(0, "1")
s113.grid(row=8, column=9)
s114 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep9, width=13, bg="azure", justify='center')
s114.insert(0, "3")
s114.grid(row=9, column=9)
s115 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep10, width=13, bg="azure", justify='center')
s115.insert(0, "3")
s115.grid(row=10, column=9)
s116 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep11, width=13, bg="azure", justify='center')
s116.insert(0, "3")
s116.grid(row=11, column=9)
s117 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep12, width=13, bg="azure", justify='center')
s117.insert(0, "3")
s117.grid(row=12, column=9)
s118 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep13, width=13, bg="azure", justify='center')
s118.insert(0, "3")
s118.grid(row=13, column=9)
s119 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep14, width=13, bg="azure", justify='center')
s119.insert(0, "3")
s119.grid(row=14, column=9)
s120 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_dep15, width=13, bg="azure", justify='center')
s120.insert(0, "1")
s120.grid(row=15, column=9)

f145 = Label(WF, text=" Temperature " + "\n" + "(deg F)",bg="deepskyblue", relief=SOLID, bd=1)
f145.grid(row=0,column=10,sticky="nsew",padx=1,pady=1)
s121 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem1, width=15, bg="azure", justify='center')
s121.insert(0, "1")
s121.grid(row=1, column=10)
s122 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem2, width=15, bg="azure", justify='center')
s122.insert(0, "1")
s122.grid(row=2, column=10)
s123 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem3, width=15, bg="azure", justify='center')
s123.insert(0, "1")
s123.grid(row=3, column=10)
s124 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem4, width=15, bg="azure", justify='center')
s124.insert(0, "1")
s124.grid(row=4, column=10)
s125 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem5, width=15, bg="azure", justify='center')
s125.insert(0, "1")
s125.grid(row=5, column=10)
s126 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem6, width=15, bg="azure", justify='center')
s126.insert(0, "1")
s126.grid(row=6, column=10)
s127 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem7, width=15, bg="azure", justify='center')
s127.insert(0, "1")
s127.grid(row=7, column=10)
s128 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem8, width=15, bg="azure", justify='center')
s128.insert(0, "1")
s128.grid(row=8, column=10)
s129 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem9, width=15, bg="azure", justify='center')
s129.insert(0, "3")
s129.grid(row=9, column=10)
s130 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem10, width=15, bg="azure", justify='center')
s130.insert(0, "3")
s130.grid(row=10, column=10)
s131 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem11, width=15, bg="azure", justify='center')
s131.insert(0, "3")
s131.grid(row=11, column=10)
s132 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem12, width=15, bg="azure", justify='center')
s132.insert(0, "1")
s132.grid(row=12, column=10)
s133 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem13, width=15, bg="azure", justify='center')
s133.insert(0, "1")
s133.grid(row=13, column=10)
s134 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem14, width=15, bg="azure", justify='center')
s134.insert(0, "1")
s134.grid(row=14, column=10)
s135 = Entry(WF,font=('arial', 10,'bold'), textvariable=wf_tem15, width=15, bg="azure", justify='center')
s135.insert(0, "3")
s135.grid(row=15, column=10)








root.mainloop()