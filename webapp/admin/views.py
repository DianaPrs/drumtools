from flask_login import current_user
from flask import redirect, url_for, flash
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from webapp.admin.decorators import admin_required


class MyView(BaseView):
    @expose('/')
    @admin_required
    def index(self):
        return 'Hello Admin!! You can have users sessions info here. Maybe. '

class UserView(ModelView):
    can_create = False
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', ]
    def is_accessible(self):
        return current_user.is_admin
     
    def inaccessible_callback(self, name, *kwargs):
        flash('You have to be Tutor to access this page.')
        return redirect(url_for('profile.account'))

class TutorView(ModelView):
    def is_accessible(self):
        return current_user.is_admin or current_user.is_tutor
     
    def inaccessible_callback(self, name, *kwargs):
        flash('You have to be Tutor to access this page.')
        return redirect(url_for('profile.account'))    

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_admin

    def inaccessible_callback(self, name, *kwargs):
        flash('You have to be Admin to access this page.')
        return redirect(url_for('profile.account'))