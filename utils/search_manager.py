from database.db_manager import DatabaseManager


class SearchManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def search_contacts(self, keyword):
        """搜索联系人"""
        return self.db_manager.search_contacts(keyword)

    def filter_contacts_by_field(self, field_name, field_value):
        """按字段筛选联系人"""
        # 这个功能需要在数据库层面实现更复杂的查询
        # 目前先返回所有联系人作为占位符
        return self.db_manager.get_all_contacts()