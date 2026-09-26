import yaml
# 定义函数 默认读dev的环境
def get_config(env="dev"):
    # 打开yaml
    with open("config/config.yaml","r",encoding="utf-8") as f:
        # 把yaml读成python字典
        config=yaml.safe_load(f)
    return config[env]
