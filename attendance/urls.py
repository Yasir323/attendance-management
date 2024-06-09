from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, ShiftViewSet, RosterViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'rosters', RosterViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
