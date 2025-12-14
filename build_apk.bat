name: Build APK

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y build-essential libgl1-mesa-dev libgles2-mesa-dev
        python -m pip install --upgrade pip
        pip install --upgrade cython
        pip install -r requirements.txt

    - name: Setup buildozer
      run: |
        pip install buildozer
        sudo apt install -y git zip unzip openjdk-13-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

    - name: Build APK
      run: |
        buildozer init
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: contactsmanager-apk
        path: bin/*.apk@echo off
setlocal enabledelayedexpansion

echo ================================================
echo 联系人管理系统 APK 构建脚本
echo ================================================
echo.
echo 当前目录: %cd%
echo.
timeout /t 2 /nobreak >nul

echo 正在启动Docker容器进行APK构建...
echo 命令: docker run --rm -v %cd%:/home/user/hostcwd kivy/buildozer android debug
echo.
docker run --rm -v %cd%:/home/user/hostcwd kivy/buildozer android debug

if !errorlevel! equ 0 (
    echo.
    echo ================================================
    echo APK构建成功完成！
    echo ================================================
    echo 请在bin目录中查找生成的APK文件
) else (
    echo.
    echo ================================================
    echo 错误: APK构建失败，退出代码: !errorlevel!
    echo ================================================
    echo 请检查以上输出以诊断问题
)

echo.
echo 按任意键退出...
pause >nul