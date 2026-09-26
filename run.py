import os

def run():
    # 第一步：跑测试，生成 Allure 数据
    os.system("pytest -v --alluredir=./allure-results --clean-alluredir")

    # 第二步：打开 Allure 报告
    os.system("allure serve ./allure-results")
# 如果这个文件是被直接执行的，就执行下面的代码
if __name__ == "__main__":
    run()
