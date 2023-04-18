from Exercise.ex_3_Document_Management.category import Category
from Exercise.ex_3_Document_Management.document import Document
from Exercise.ex_3_Document_Management.storage import Storage
from Exercise.ex_3_Document_Management.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize ex_3_Document_Management")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
