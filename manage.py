# 导入flask_migrate扩展和script扩展
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
# 从info目录下导入db，app
from person import create_app,db,models
# from person.models import User
app = create_app('development')

# 实例化管理对象
manage = Manager(app)
# 数据库迁移
Migrate(app,db)
# 添加迁移命令
manage.add_command("db",MigrateCommand)

"""
迁移步骤：
1、创建迁移仓库
python manage.py db init 
2、创建迁移脚本
python manage.py db migrate -m 'init_tables'
3、执行迁移脚本
python manage.py db upgrade 

迁移脚本不成功：在manage.py文件中导入models

"""

if __name__ == '__main__':
    # app.run(debug=True)
    print(app.url_map)
    manage.run()
