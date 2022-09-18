# import json
import pytz
from datetime import datetime, timedelta
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# from config import FIREBASE_CERT

from db import ORM

from model import ToDoItem




# # 引用私密金鑰
# # path/to/serviceAccount.json 請用自己存放的路徑
# cert = json.loads(FIREBASE_CERT)
# cred = credentials.Certificate(cert)

# # 初始化firebase，注意不能重複初始化
# firebase_admin.initialize_app(cred)

# # 初始化firestore
# db = firestore.client()


taipei = pytz.timezone('Asia/Taipei')
item = ToDoItem(
    message="test test gogogo!",
    created_at=datetime.now(taipei),
    done=False
)


orm = ORM()

collection_ref = orm.get_todolist("92kdNMozzVc2221322")

_time, _doc = collection_ref.add(item.dict())
docs = collection_ref.stream()

for doc in docs:
    print(doc.id)

exit("Done.")