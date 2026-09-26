from utils.db_util import query, execute
from utils.request_util import get
from config.settings import get_config

config = get_config("dev")
BASE_URL = config.get("base_url")


def test_api_data_to_db():
    # 1. 调接口，拿数据
    res = get(f"{BASE_URL}/users/1")
    user_id = res.json()["id"]
    username = res.json()["username"]

    # 2. 存进数据库（先删旧的，再插新的）
    execute(f"DELETE FROM users WHERE id = {user_id}")
    execute(f"INSERT INTO users (id, name) VALUES ({user_id}, '{username}')")

    # 3. 从数据库查出来
    result = query(f"SELECT name FROM users WHERE id = {user_id}")

    # 4. 断言：数据库里的，和接口返回的一致
    assert result[0][0] == username