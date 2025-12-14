from database.db_manager import DatabaseManager
from models import Contact, CustomField


class ContactManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def add_contact(self, contact):
        """添加联系人"""
        return self.db_manager.add_contact(contact)

    def update_contact(self, contact):
        """更新联系人"""
        self.db_manager.update_contact(contact)

    def delete_contact(self, contact_id):
        """删除联系人"""
        self.db_manager.delete_contact(contact_id)

    def get_contact(self, contact_id):
        """获取联系人"""
        return self.db_manager.get_contact(contact_id)

    def get_all_contacts(self):
        """获取所有联系人"""
        return self.db_manager.get_all_contacts()

    def search_contacts(self, keyword):
        """搜索联系人"""
        return self.db_manager.search_contacts(keyword)