import itchat
from itchat.content import TEXT


@itchat.msg_register(TEXT)
def print_content(msg):
    print(msg['Text'])


itchat.auto_login()
itchat.run()
