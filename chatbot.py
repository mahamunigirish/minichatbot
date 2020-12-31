from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine = pp.init()


rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 110)     # setting up new voice rate


voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

#engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# create a new chat bot named charlie

bot = ChatBot('Charlie')

conv = [
    'Hello',
    'Hi There !',
    'What is Your Name ?',
    'My Name is Charliee i am develope by girish',
    'how are you?',
    'I am doing grate these days',
    'thank you',
    'in which city you live ?',
    'I lived in chembur'

]

trainer = ListTrainer(bot)
trainer.train(conv)

'''print("Talk To Bot,")


while True:
    query  = input()
    if (query == exit):
        break
    answer = bot.get_response(query)
    print("BOt :",answer)'''

main = Tk()
main.geometry("500x700")
main.title("MyChatBot")
img = PhotoImage(file='C:\\Users\\HP\\Desktop\\computer science\\chatbot projects\\robo1.png')
photo = Label(main, image=img)
photo.pack(pady=5)


def ask_from_bot():
    query = textfield.get()
    answer = bot.get_response(query)
    msgs.insert(END, "you:" + query)
    msgs.insert(END, "bot : " + str(answer))
    speak(answer)
    textfield.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# creating Text Field

textfield = Entry(main, font=("Comic", 20))
textfield.pack(fill=X, pady=10)
btn = Button(main, text="Ask_From_Bot", font=("Comic", 15), command=ask_from_bot)
btn.pack()


def Enter(event):
    btn.invoke()


main.bind('<Return>', Enter)

main.mainloop()
