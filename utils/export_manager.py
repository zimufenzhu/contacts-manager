import csv
import json
from database.db_manager import DatabaseManager


class ExportManager:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def export_to_csv(self, filename):
        """导出联系人到CSV文件"""
        contacts = self.db_manager.get_all_contacts()
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'name', 'phone', 'email', 'company', 'position', 'address', 'notes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for contact in contacts:
                writer.writerow({
                    'id': contact.id,
                    'name': contact.name,
                    'phone': contact.phone,
                    'email': contact.email,
                    'company': contact.company,
                    'position': contact.position,
                    'address': contact.address,
                    'notes': contact.notes
                })
        
        return filename

    def export_to_json(self, filename):
        """导出联系人到JSON文件"""
        contacts = self.db_manager.get_all_contacts()
        
        contact_data = []
        for contact in contacts:
            contact_data.append({
                'id': contact.id,
                'name': contact.name,
                'phone': contact.phone,
                'email': contact.email,
                'company': contact.company,
                'position': contact.position,
                'address': contact.address,
                'notes': contact.notes
            })
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(contact_data, jsonfile, ensure_ascii=False, indent=2)
        
        return filename