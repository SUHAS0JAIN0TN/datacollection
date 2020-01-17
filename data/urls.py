from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('signup/',views.signup,name='signup'),
    path('query1/',views.query1,name='query1'),
    path('query2/',views.query2,name='query2'),
    path('query3/',views.query3,name='query3'),
    # path('query4/',views.query4,name='query4'),
    # path('query5/',views.query5,name='query5'),
    path('query1-table/',views.query1_table,name='query1_table'),
    path('query2-table/',views.query2_table,name='query2_table'),
    path('query3-table/',views.query3_table,name='query3_table'),

    path('all-query/',views.all_query,name='all_query'),
    path('all-query-csv/',views.all_query_csv,name='all_query_csv'),

    # path('thanks/', views.thanks, name='thanks'),
    # path('up/<str:typ>',views.up ,name='up'),
    # path('search',views.search, name='search')
    path('logout/',views.logout,name='logout'),
]