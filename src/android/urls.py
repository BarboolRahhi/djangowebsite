from django.urls import path

from android.views import (
	android_screen_view,
	detail_blog_view,

)

app_name = 'android'

urlpatterns = [
    path('', android_screen_view, name="android"),
    path('<slug>/', detail_blog_view, name="detail"),
 ]