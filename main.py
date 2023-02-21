import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    
    1111

itchat.auto_login()
itchat.run()
