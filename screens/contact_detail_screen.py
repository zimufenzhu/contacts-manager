from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.contact_manager import ContactManager
from utils.field_manager import FieldManager


class ContactDetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contact_manager = ContactManager()
        self.field_manager = FieldManager()


# 加载KV文件
Builder.load_string('''
<ContactDetailScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "联系人详情"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.root.current = 'contact_list']]
            right_action_items: [["pencil", lambda x: app.root.current = 'contact_edit'], ["delete", lambda x: None]]
            
        ScrollView:
            MDGridLayout:
                cols: 1
                padding: "10dp"
                spacing: "5dp"
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: contact_info_box.height + 30
                    
                    MDBoxLayout:
                        id: contact_info_box
                        orientation: 'vertical'
                        spacing: "10dp"
                        
                        MDLabel:
                            text: "张三"
                            font_style: "H5"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "电话: 13800138000"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "邮箱: zhangsan@example.com"
                            size_hint_y: None
                            height: self.texture_size[1]
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: company_info_box.height + 30
                    
                    MDBoxLayout:
                        id: company_info_box
                        orientation: 'vertical'
                        spacing: "10dp"
                        
                        MDLabel:
                            text: "公司信息"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "公司: ABC公司"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "职位: 工程师"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "地址: 北京市朝阳区xxx街道"
                            size_hint_y: None
                            height: self.texture_size[1]
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: custom_fields_box.height + 30
                    
                    MDBoxLayout:
                        id: custom_fields_box
                        orientation: 'vertical'
                        spacing: "10dp"
                        
                        MDLabel:
                            text: "自定义字段"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "暂无自定义字段"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: notes_box.height + 30
                    
                    MDBoxLayout:
                        id: notes_box
                        orientation: 'vertical'
                        spacing: "10dp"
                        
                        MDLabel:
                            text: "备注"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "这是一个示例联系人"
                            size_hint_y: None
                            height: self.texture_size[1]
''')