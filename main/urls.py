from django.contrib import admin
from django.urls import path
from . import views 

app_name = "main"  # pour plus tard

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.homepage, name="Home"),
	path('Contact/', views.contact, name="Contact"),
	path('Register/', views.register, name="Register"),
	path('content_spect/page/<int:num>', views.content, name="Content"),
	path('Login/', views.login_a, name="Login"),
	path('add/', views.addi, name="Add"),
	path('homepage_li/', views.login_a, name="Welcome"),
	path('logout/', views.logout_a, name="Logout")
	]
