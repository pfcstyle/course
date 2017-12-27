from django.apps import AppConfig

# 配置app名称  xadmin的右侧菜单会显示
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户"
