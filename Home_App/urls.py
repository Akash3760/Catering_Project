from django.urls import path

from Home_App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book_now/', views.book_now, name='book_now'),
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/search/', views.menu_search, name='menu_search'),
    path('menus/chicken/', views.chicken_items, name='chicken_items'),
    path('menus/mutton/', views.mutton_items, name='mutton_items'),
    path('menus/fish/', views.fish_items, name='fish_items'),
    path('menus/dal/', views.dal, name='dal'),
    path('menus/rice/', views.rice, name='rice'),
    path('menus/flourbased/', views.flourbased, name='flourbased'),
    path('menus/veg/', views.veg, name='veg'),
    path('menus/snacks/', views.snacks, name='snacks'),
    path('menus/sweets/', views.sweets, name='sweets'),
    path('menus/drinks/', views.drinks, name='drinks'),
    path('menus/salads/', views.salads, name='salads'),
    path('menus/papad/', views.papad, name='papad'),
    path('menus/chutney/', views.chutney, name='chutney'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('success_page/', views.success_page, name='success_page'),
    path('blog/', views.blog, name='blog'),
    path('submit-comment/', views.comment_views, name='comment_views'),
]
