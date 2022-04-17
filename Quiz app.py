import tkinter
from tkinter import *
import random

root=Tk()
root.title("MY QUIZ APP")
root.geometry("700x600")
root.config(background="#ffffff")

questions=[
	"The Taj Mahal is located in ?",
	"Capital of India ?",
	"Which of the following is not a coastly city of India ?",
	"How many colors are there in rainbow ?",
	"National food of India ?",
]

answerschoice=[
	["Mumbai","Delhi","Agra","Lucknow"],
	["Delhi","Chennai","Mumbai","Kolkata"],
	["Patna","Delhi","BAnaras","Agra"],
	["1","7","5","8"],
	["Dosa","Paratha","Khichdi","Chole Bhature"],

]

user_answer=[]

indexes=[]

def gen():
	global indexes
	while(len(indexes)<5):
		x=random.randint(0,4)
		if x in indexes:
			continue
		else:
			indexes.append(x)

ques=1
def selected():
	global radiovar
	global lblques,r1,r2,r3,r4
	global user_answer, ques
	x= radiovar.get()
	#user_answer.append[x]
	if ques < 5:
		lblques.config(text=questions[indexes[ques]])
		r1['text']=answerschoice[indexes[ques]][0]
		r2['text']=answerschoice[indexes[ques]][1]
		r3['text']=answerschoice[indexes[ques]][2]
		r4['text']=answerschoice[indexes[ques]][3]
		ques+=1

	else:
		pass


def startquiz():
	global radiovar
	global lblques,r1,r2,r3,r4
	lblques=Label(root,
		text=questions[indexes[0]],
		font=("Consolas",16),
		width=500,
		justify="center",
		wraplength=400,
		)
	lblques.pack()
	radiovar=IntVar()
	radiovar.set(-1)

	r1=Radiobutton(root,
		text=answerschoice[indexes[0]][0],
		font=("Times",12),
		value=0,
		variable=radiovar,
		command=selected,

		)
	r1.pack()

	r2=Radiobutton(root,
		text=answerschoice[indexes[0]][1],
		font=("Times",12),
		value=1,
		variable=radiovar,
		command=selected,

		)
	r2.pack()

	r3=Radiobutton(root,
		text=answerschoice[indexes[0]][2],
		font=("Times",12),
		value=2,
		variable=radiovar,
		command=selected,

		)
	r3.pack()

	r4=Radiobutton(root,
		text=answerschoice[indexes[0]][3],
		font=("Times",12),
		value=3,
		variable=radiovar,
		command=selected,

		)
	r4.pack()


def startispressed():
	l1.destroy()
	l2.destroy()
	lblinst.destroy()
	lblrules.destroy()
	btnstart.destroy()
	gen()
	startquiz()


img1 = PhotoImage(file="gradhat.png")
l1=Label(root,image=img1,background="#ffffff")
l1.pack(padx=40,pady=(0,0))

l2=Label(root, text="QUIZ",font=("Comic sans MS",24,"bold"),background="#ffffff")
l2.pack(pady=(0,50))

img2=PhotoImage(file="start.png")
btnstart=Button(root,image=img2,relief=FLAT,border=0,command=startispressed)
btnstart.pack()

lblinst=Label(root,
	text="Read The Rules And\nClick Start Once You Are Ready",
	background="#ffffff",
	font=("Consolas",14),
	justify="center",

	)
lblinst.pack(pady=(10,75))

lblrules=Label(root,
	text="This quiz contains 3 questions\nYou will get 20 seconds to solve the question\nOnce you select a radio button that will be a final choice\nhence think before you select ",
	width=100,
	font=("Times",14),
	background="black",
	foreground="yellow")

lblrules.pack()

root.resizable(0,0)
root.mainloop()