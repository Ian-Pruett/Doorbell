from fbchat import Client, log
from fbchat.models import Message, ThreadType
import getpass

class Bot(Client):

    def onMessage(self, author_id=None, message_object=None, 
        thread_id=None, thread_type=ThreadType.USER, **kwargs):
        
        self.markAsRead(author_id)

        log.info('message {} from {} in {}'.format(
                message_object, thread_id, thread_type))

        msg = message_object.text

        reply = 'DUDE! It worked'

        self.send(Message(text=reply), thread_id=thread_id, 
            thread_type=thread_type)

        if author_id != self.uid:
            self.markAsDelivered(author_id, thread_id)

if __name__ == '__main__':
    username = input('What is your fb username: ')
    password = getpass.getpass('What is your fb password: ')
    bot = Bot(username, password)
    bot.listen()