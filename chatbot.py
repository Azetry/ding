#



class ChatBot:
    def __init__(self) -> None:
        self.cmd_list = {
            'list': self.item_list,
            'get': 0,
            'update': 0,
            'delete': 0,
        }


    # main
    def response(self, msg):
        # check is command
        if self.is_cmd(msg): return self.cmd_list[self.get_cmd(msg)]()

        return msg


    # command
    @staticmethod
    def is_cmd(msg:str):
        ''' If the first char of message is "!", the message is a command. 
        '''
        return msg[0] == "!"


    def get_cmd(self, msg:str):
        if msg[1:].strip() in self.cmd_list: return  msg[1:].strip() 
        else: raise ValueError("Not supported command.")


    def item_list(self) -> str:
        ''' List all unfinish todo items'''
        return "Listed."