import sqlite3
import os
from datetime import datetime
from models import Contact, CustomField


class DatabaseManager:
    def __init__(self, db_name='contacts.db'):
        self.db_name = db_name
        self.init_database()

    def get_connection(self):
        """获取数据库连接"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # 使得查询结果可以通过列名访问
        return conn

    def init_database(self):
        """初始化数据库表结构"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 创建联系人表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                company TEXT,
                position TEXT,
                address TEXT,
                notes TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 创建自定义字段表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS custom_fields (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_id INTEGER NOT NULL,
                field_name TEXT NOT NULL,
                field_value TEXT,
                field_type TEXT DEFAULT 'text',
                FOREIGN KEY (contact_id) REFERENCES contacts (id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
        conn.close()

    def add_contact(self, contact):
        """添加联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO contacts (name, phone, email, company, position, address, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            contact.name, contact.phone, contact.email, contact.company,
            contact.position, contact.address, contact.notes,
            contact.created_at, contact.updated_at
        ))

        contact_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return contact_id

    def update_contact(self, contact):
        """更新联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE contacts SET name=?, phone=?, email=?, company=?, position=?, address=?, notes=?, updated_at=?
            WHERE id=?
        ''', (
            contact.name, contact.phone, contact.email, contact.company,
            contact.position, contact.address, contact.notes,
            datetime.now(), contact.id
        ))

        conn.commit()
        conn.close()

    def delete_contact(self, contact_id):
        """删除联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
        conn.commit()
        conn.close()

    def get_contact(self, contact_id):
        """获取单个联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM contacts WHERE id=?', (contact_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Contact(
                id=row['id'],
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                company=row['company'],
                position=row['position'],
                address=row['address'],
                notes=row['notes']
            )
        return None

    def get_all_contacts(self):
        """获取所有联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM contacts ORDER BY name')
        rows = cursor.fetchall()
        conn.close()

        contacts = []
        for row in rows:
            contacts.append(Contact(
                id=row['id'],
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                company=row['company'],
                position=row['position'],
                address=row['address'],
                notes=row['notes']
            ))
        return contacts

    def search_contacts(self, keyword):
        """搜索联系人"""
        conn = self.get_connection()
        cursor = conn.cursor()

        query = '''
            SELECT * FROM contacts 
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR company LIKE ? OR position LIKE ? OR notes LIKE ?
            ORDER BY name
        '''
        search_term = f'%{keyword}%'
        cursor.execute(query, (search_term, search_term, search_term, search_term, search_term, search_term))
        rows = cursor.fetchall()
        conn.close()

        contacts = []
        for row in rows:
            contacts.append(Contact(
                id=row['id'],
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
                company=row['company'],
                position=row['position'],
                address=row['address'],
                notes=row['notes']
            ))
        return contacts

    def add_custom_field(self, custom_field):
        """添加自定义字段"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO custom_fields (contact_id, field_name, field_value, field_type)
            VALUES (?, ?, ?, ?)
        ''', (
            custom_field.contact_id, custom_field.field_name,
            custom_field.field_value, custom_field.field_type
        ))

        field_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return field_id

    def update_custom_field(self, custom_field):
        """更新自定义字段"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE custom_fields SET field_name=?, field_value=?, field_type=?
            WHERE id=?
        ''', (
            custom_field.field_name, custom_field.field_value,
            custom_field.field_type, custom_field.id
        ))

        conn.commit()
        conn.close()

    def delete_custom_field(self, field_id):
        """删除自定义字段"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM custom_fields WHERE id=?', (field_id,))
        conn.commit()
        conn.close()

    def get_custom_fields(self, contact_id):
        """获取联系人的所有自定义字段"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM custom_fields WHERE contact_id=?', (contact_id,))
        rows = cursor.fetchall()
        conn.close()

        custom_fields = []
        for row in rows:
            custom_fields.append(CustomField(
                id=row['id'],
                contact_id=row['contact_id'],
                field_name=row['field_name'],
                field_value=row['field_value'],
                field_type=row['field_type']
            ))
        return custom_fields