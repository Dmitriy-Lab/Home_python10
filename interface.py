from tkinter import *
from Bot import send_answer

global answer
global count
count = -1
answer = ''

def NextQ():
    global count
    count += 1
    data = open('messageText.txt', 'r', encoding='utf-8')
    text = data.readlines()
    data.close()
    if count == len(text):
        return '               Больше сообщений нет                '
    else:
        return ''.join(text[count])

def PrintNextQ():
    Label(root, text=f'{NextQ()}').grid(column=0, row=2)
    


def SendAnsver():
    Label.destroy
    global answer
    global count
    answer = entryAnswer.get(1.0, END)
    Label(root, text='Сообщение отправлено').grid(column=2, row=3)
    send_answer(answer, count)
    entryAnswer.delete(1.0, END)
    return 'Сообщение отправлено'



root = Tk()
root.title('Служба поддержки')
root.geometry('600x400')


ButtonNext = Button(root, text="Следующий вопрос", command=PrintNextQ)
ButtonNext.grid(column=0, row=6)
ButtonSend = Button(root, text="Отправить ответ", command=SendAnsver)
ButtonSend.grid(column=2, row=6)
ButtonExit = Button(root, text="Выход", command=root.destroy)
ButtonExit.grid(column=1, row=8)

LabelAnswer = Label(root, text="Поле для ответа")
LabelAnswer.grid(column=2, row=1)
entryAnswer = Text(root, width=30, height=10)
entryAnswer.grid(column=2, row=2)


root.mainloop()