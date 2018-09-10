from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Friend') #create the bot

bot.set_trainer(ListTrainer) # Teacher

#bot.train(conv) # teacher train the bot

for knowledeg in os.listdir('base'):
	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	bot.train(BotMemory)



app = Flask(__name__)

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']

	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	print("Friend: "+bot_response)
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)


if __name__=='__main__':
	app.run(debug=True,port=5002)