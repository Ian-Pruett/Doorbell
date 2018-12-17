from fbchat import Client, log
from fbchat.models import *


class NotifyBot(Client):
    def ring(self):
        users = self.fetchAllUsers()
        for user in users:
            self.sendMessage(Message('someone is at the door'), 
                thread_id=user.uid, thread_type=ThreadType.USER)
        self.logout()