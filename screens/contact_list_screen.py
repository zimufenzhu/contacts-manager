from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.contact_manager import ContactManager


class ContactListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contact_manager = ContactManager()
        self.load_contacts()
    
    def load_contacts(self):
        """加载联系人列表"""
        contacts = self.contact_manager.get_all_contacts()
        # 这里应该更新UI显示联系人列表
        print(f"Loaded {len(contacts)} contacts")


# 加载KV文件
Builder.load_string('''
<ContactListScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "联系人列表"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.root.current = 'main']]
            right_action_items: [["magnify", lambda x: None]]
            
        MDBoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            
            MDTextField:
                id: search_field
                hint_text: "搜索联系人..."
                icon_right: "magnify"
                icon_right_color: app.theme_cls.primary_color
                
        ScrollView:
            MDList:
                id: contact_list
                
                # 示例联系人项
                TwoLineListItem:
                    text: "张三"
                    secondary_text: "13800138000"
                    on_press: 
                        app.root.current = 'contact_detail'
                        
                TwoLineListItem:
                    text: "李四"
                    secondary_text: "lisi@example.com"
                    on_press: 
                        app.root.current = 'contact_detail'
                        
                TwoLineListItem:
                    text: "王五"
                    secondary_text: "北京市朝阳区"
                    on_press: 
                        app.root.current = 'contact_detail'
                        
        MDFloatingActionButton:
            icon: 'plus'
            pos_hint: {'center_x': 0.9, 'center_y': 0.1}
            on_press: app.root.current = 'contact_edit'
''')