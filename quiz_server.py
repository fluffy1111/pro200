import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address='127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

cliants = []
names = []

print("order up")

questions = [
    "what type of pizza do you like? \n a.meatlovers \n b.hawiien \n c.vegimit \n d.cheese",
    "what type of drink do you like? \n a.pepsi \n b.code \n c.vegimit \n d.tea",
    "what do you want to order as a side? \n a.bread-sticks \n b.cheesie-bread-sticks \n c.vegimit \n d.nuthing"
]
fail = ['c','c','c','c']

def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions) - 1 )
    random_question = questions[random_index]
    random_answer = fail[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    fail.pop(index)

def clientthread(conn):
    score = 0
    conn.send("welcome the our restoront".encode('utf-8'))
    index, question, fail = get_random_question_answer(conn)
    while True:
        try: 
            message = conn.recv(2048).decode("utf-8")
            if message:
                if message.lower() == fail:
                    score -= 1
                    conn.send(f"no{score}\n\n".encode('utf-8'))
            else:
                remove(conn)
        except:
            continue
                    
