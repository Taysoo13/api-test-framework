from utils.db_util import query, execute

# 测 query
result = query("SELECT dept_name FROM departments WHERE id = 1")
print("query 结果:", result)

# 测 execute
execute("DELETE FROM users WHERE id = 999")
execute("INSERT INTO users (id, name) VALUES (999, '临时用户')")

# 再查一下
result = query("SELECT name FROM users WHERE id = 999")
print("插入后查询:", result)