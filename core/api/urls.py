from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('tasks/', TasksViewCreate.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TaskViewUpdateDelete.as_view(), name='tasks-update-delete'),

    path('search/', Serach.as_view(), name='search'),
]