# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from leo_API import Leo 
import sys
import pyarabic.araby as araby



import os
#promt is the text from the user input

 
app = Flask(__name__)
leo = Leo()



def askleo(prompt):
#max_tokens_to_sample is an int : 400 to 2048
    # You can use it as Llama by explicitly leaving System Prompt empty.
    system_prompt = 'you are an ai named No0ne your job is to help devolopers in solving theit problems and and help them .rules : your response should be complete and well explained , if someone asked you somthing that dont have a relation with coding and programming dont answer his question and  say " im a coding ai expert i cannot help you"'
    response = leo.ask(prompt, system_prompt=system_prompt,max_tokens_to_sample=2048)
    response = response.completion
    print(response)
    return response


@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = str(request.args.get('msg'))
    text = askleo(userText)
    print(text)
    return text
 
 
if __name__ == "__main__":
    app.run()




