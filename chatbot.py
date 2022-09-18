#
import pytz
from datetime import datetime, timedelta
from db import ORM
from model import ToDoItem



class ChatBot:
    def __init__(self) -> None:
        self.cmd_list = [
            'list',
        ]

        self.orm = ORM()
        self.timezone = pytz.timezone('Asia/Taipei')


    # main
    def response(self, user_id, msg):
        # check is command
        if self.is_cmd(msg): return self.exec_cmd(user_id, msg)
        else: return self.add_item(user_id, msg)


    # add todo item
    def add_item(self, user_id, msg):
        item = ToDoItem(
            message=msg,
            created_at=datetime.now(self.timezone),
            done=False
        )
        
        # add
        ref = self.orm.get_todolist(user_id)
        _time, _doc = ref.add(item.dict())

        return "Added."
    
    # command
    @staticmethod
    def is_cmd(msg:str):
        ''' If the first char of message is "!", the message is a command. 
        '''
        return msg[0] == "!"


    def exec_cmd(self, uer_id, msg:str):
        if msg[1:].strip() in self.cmd_list: cmd = msg[1:].strip() 
        else: raise ValueError("Not supported command.")

        if cmd == "list": return self.item_list()
        # ...

        return None


    def item_list(self) -> str:
        ''' List all unfinish todo items'''
        return "Listed."