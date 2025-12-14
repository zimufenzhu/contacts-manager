from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.contact_manager import ContactManager
from utils.field_manager import FieldManager


class ContactEditScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contact_manager = ContactManager()
        self.field_manager = FieldManager()


# 加载KV文件
Builder.load_string('''
<ContactEditScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "编辑联系人"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.root.current = 'contact_list']]
            right_action_items: [["content-save", lambda x: None]]
            
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "10dp"
                spacing: "15dp"
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: basic_info_box.height + 30
                    
                    MDBoxLayout:
                        id: basic_info_box
                        orientation: 'vertical'
                        spacing: "10dp"
                        
                        MDLabel:
                            text: "基本信息"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDTextField:
                            hint_text: "姓名 *"
                            helper_text: "请输入联系人姓名"
                            helper_text_mode: "on_focus"
                            
                        MDTextField:
                            hint_text: "电话"
                            helper_text: "请输入联系电话"
                            helper_text_mode: "on_focus"
                            
                        MDTextField:
                            hint_text: "邮箱"
                            helper_text: "请输入电子邮箱"
                            helper_text_mode: "on_focus"
                
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
                            
                        MDTextField:
                            hint_text: "公司"
                            helper_text: "请输入公司名称"
                            helper_text_mode: "on_focus"
                            
                        MDTextField:
                            hint_text: "职位"
                            helper_text: "请输入职位"
                            helper_text_mode: "on_focus"
                            
                        MDTextField:
                            hint_text: "地址"
                            helper_text: "请输入地址"
                            helper_text_mode: "on_focus"
                
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
                            
                        MDRaisedButton:
                            text: "添加字段"
                            size_hint: None, None
                            size: "120dp", "35dp"
                            pos_hint: {"center_x": .5}
                            on_press: None  # 添加自定义字段
                
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
                            
                        MDTextField:
                            hint_text: "备注"
                            helper_text: "请输入备注信息"
                            helper_text_mode: "on_focus"
                            
        MDFloatingActionButton:
            icon: 'content-save'
            pos_hint: {'center_x': 0.9, 'center_y': 0.1}
            on_press: None
''')