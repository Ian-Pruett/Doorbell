from fbchat import Client, log
from fbchat.models import *

class NotifyBot(Client):

    def ring(self):
        users = self.fetchAllUsers()
        for user in users:
            print(user.first_name)
        self.logout()