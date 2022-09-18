import json
import pytz
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import FIREBASE_CERT
from model import ToDoItem



class ORM:
    def __init__(self, timezone:str='Asia/Taipei') -> None:
        # 引用私密金鑰
        # path/to/serviceAccount.json 請用自己存放的路徑
        cert = json.loads(FIREBASE_CERT)
        self.cred = credentials.Certificate(cert)

        # 初始化firebase，注意不能重複初始化
        firebase_admin.initialize_app(self.cred)

        # 初始化firestore
        self.db = firestore.client()

        # set timezone
        self.timezone =  pytz.timezone(timezone)


    
    def get_todolist(self, user_id:str):
        user_ref = self.db.collection("user").document(user_id)

        if not user_ref.get().exists: user_ref.set({})

        return user_ref.collection("todo_list")
