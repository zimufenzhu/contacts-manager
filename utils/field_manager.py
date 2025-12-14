from database.db_manager import DatabaseManager
from models import CustomField


class FieldManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def add_custom_field(self, custom_field):
        """添加自定义字段"""
        return self.db_manager.add_custom_field(custom_field)

    def update_custom_field(self, custom_field):
        """更新自定义字段"""
        self.db_manager.update_custom_field(custom_field)

    def delete_custom_field(self, field_id):
        """删除自定义字段"""
        self.db_manager.delete_custom_field(field_id)

    def get_custom_fields(self, contact_id):
        """获取联系人的自定义字段"""
        return self.db_manager.get_custom_fields(contact_id)