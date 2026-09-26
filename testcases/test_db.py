# from utils.db_util import query
# def test_db():
#     result =query("select dept_name from departments where id =1")
#     assert result[0][0]=="技术部"


# from utils.db_util import query
# def test_department_count():
#     result =query("select count(*) from departments")
#     assert result[0][0]>0
# def test_department_name():
#     result =query("select dept_name from departments where id =2")
#     assert result[0][0]=="产品部"
# def test_manager():
#     result =query("select manager from departments where id =3")
#     assert result[0][0]=="张总监"
# from utils.db_util import query
# def test_user_exists():
#     result =query("select name from users where id =1")
#     assert result [0][0]=="张三"