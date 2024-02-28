from django.urls import path, include
from acounts.views import (
    LoginView,
    LogOutView,
    SignUpView,
    ChangePasswordView,
    ChangePasswordDoneView, 
    PasswordResetView,
    ResetPasswordDoneView,
    PasswordResetConfirmView,
    ResetDoneView
)

app_name = "acounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("api/V1/", include("acounts.api.V1.urls")),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path(
        "change-password/done/",
        ChangePasswordDoneView.as_view(),
        name="change_password_done",
    ),
    path(
         "resetPassword/",  PasswordResetView.as_view(), name="reset_password"
    ),
    path(
         "resetPassword/done/",
         ResetPasswordDoneView.as_view(),
        name="reset_password_done",
    ),
    path("reset/<str:token>", PasswordResetConfirmView.as_view(), name="reset"),
    path("reset/done/", ResetDoneView.as_view(), name="reset_done"),
]
