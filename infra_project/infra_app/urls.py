from django import urls

from infra_project.infra_app import views

app_name = 'infra_app'

urlpatterns = [
    urls.path('', views.index, name='index'),
    urls.path('second/', views.second_page, name='second_page'),
]
