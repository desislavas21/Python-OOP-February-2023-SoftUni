from Exercise.ex_3_Document_Management.category import Category
from Exercise.ex_3_Document_Management.topic import Topic
from Exercise.ex_3_Document_Management.document import Document
from typing import List


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        try:
            match = [category for category in self.categories if category_id == category.id][0]
            match.name = new_name
        except IndexError:
            pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            match = [topic for topic in self.topics if topic_id == topic.id][0]
            match.storage_folder = new_storage_folder
            match.topic = new_topic
        except IndexError:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            match = [document for document in self.documents if document.id == document_id][0]
            match.file_name = new_file_name
        except IndexError:
            pass

    def delete_category(self, category_id):
        try:
            match = [category for category in self.categories if category.id == category_id][0]
            self.categories.remove(match)
        except IndexError:
            pass

    def delete_topic(self, topic_id):
        try:
            match = [topic for topic in self.topics if topic.id == topic_id][0]
            self.topics.remove(match)
        except IndexError:
            pass

    def delete_document(self, document_id):
        try:
            match = [document for document in self.documents if document.id == document_id][0]
            self.documents.remove(match)
        except IndexError:
            pass

    def get_document(self, document_id):
        try:
            match = [document for document in self.documents if document.id == document_id][0]
            return match
        except IndexError:
            pass

    def __repr__(self):
        final = []
        for document in self.documents:
            final.append(document.__repr__())
        return '\n'.join(final)
