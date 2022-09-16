import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore




# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('./ding-b2817-firebase-adminsdk-mnrt2-de0637d349.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()


doc = {
    'todo': "test ding -2",
    'done': False
}

collection_ref = db.collection("todo_list")

# _time, _doc = collection_ref.add(doc)
docs = collection_ref.stream()

for doc in docs:
    print(doc.id)