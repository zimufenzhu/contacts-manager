#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
核心功能测试脚本
用于验证联系人管理系统的核心功能是否正常工作
"""

import sys
import os

# 将项目根目录添加到Python路径中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 简化测试，只测试最基本的数据库和联系人管理功能
def test_basic_functionality():
    """测试基本功能"""
    print("测试基本功能...")
    try:
        # 动态导入模块
        from models import Contact
        from database.db_manager import DatabaseManager
        from utils.contact_manager import ContactManager
        
        print("✓ 模块导入成功")
        
        # 测试数据库连接
        db_manager = DatabaseManager()
        db_manager.create_tables()
        print("✓ 数据库连接和表创建成功")
        
        # 测试联系人管理
        contact_manager = ContactManager()
        
        # 创建测试联系人
        contact = Contact(
            name="测试联系人",
            phone="13800138000",
            email="test@example.com"
        )
        
        # 添加联系人
        contact_id = contact_manager.add_contact(contact)
        print(f"✓ 成功添加联系人，ID: {contact_id}")
        
        # 获取联系人
        retrieved_contact = contact_manager.get_contact_by_id(contact_id)
        if retrieved_contact and retrieved_contact.name == "测试联系人":
            print("✓ 成功获取联系人")
        else:
            print("✗ 获取联系人失败")
            return False
            
        # 更新联系人
        retrieved_contact.phone = "13900139000"
        if contact_manager.update_contact(retrieved_contact):
            print("✓ 成功更新联系人")
        else:
            print("✗ 更新联系人失败")
            return False
            
        # 删除联系人
        if contact_manager.delete_contact(contact_id):
            print("✓ 成功删除联系人")
        else:
            print("✗ 删除联系人失败")
            return False
            
        print("✓ 基本功能测试全部通过")
        return True
    except Exception as e:
        print(f"✗ 基本功能测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主测试函数"""
    print("=" * 50)
    print("联系人管理系统基本功能测试")
    print("=" * 50)
    
    # 运行基本功能测试
    if test_basic_functionality():
        print("\n" + "=" * 50)
        print("测试结果: 所有基本功能测试通过！")
        print("核心功能正常工作。")
        return True
    else:
        print("\n" + "=" * 50)
        print("测试结果: 基本功能测试失败！")
        print("请检查相关功能实现。")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)