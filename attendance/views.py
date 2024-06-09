from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsManager, IsStaff
from .models import Staff, Shift, Roster, Attendance
from .serializers import StaffSerializer, ShiftSerializer, RosterSerializer, AttendanceSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, IsManager]


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated, IsManager]


class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    permission_classes = [IsAuthenticated, IsManager]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsStaff]
