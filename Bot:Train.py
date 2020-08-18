from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle, gzip

bot = ChatBot('YouTubeChatBot')
trainer = ListTrainer(bot)


#Loading pickle commments
with gzip.open('./InstagramComments_.p', 'rb') as f:
    comments = pickle.load(f)
    f.close()


#Training Bot with existing comments
for convo in comments[:10000]:
    trainer.train(convo)

#Testing bot
while True:
    request = input("You: ")
    response = bot.get_response(request)
    print('Bot:', response)