from django.urls import path

import users.views

urlpatterns = [
    path('login/', users.views.login_user, name='login'),
    path('signup/', users.views.sign_up(), name='signup'),
]