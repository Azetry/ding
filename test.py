import json
import pytz
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import FIREBASE_CERT




# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cert = json.loads(FIREBASE_CERT)
cred = credentials.Certificate(cert)

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()


taipei = pytz.timezone('Asia/Taipei')
doc = {
    'todo': "test ding -2",
    'created_at': datetime.now(taipei),
    'date': datetime.now(taipei) + timedelta(days=1),
    'done': False
}

collection_ref = db.collection("user").document("92kdNMozzVcm4eWj8ah6").collection("todo_list")

_time, _doc = collection_ref.add(doc)
docs = collection_ref.stream()

for doc in docs:
    print(doc.id)

exit("Done.")