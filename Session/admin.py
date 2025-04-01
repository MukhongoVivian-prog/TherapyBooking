from django.contrib import admin
from .models import User, Patient, Therapist, Availability, Appointment, Payment, Notification, SessionRoom

# Custom User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_verified')
    search_fields = ('email', 'role')
    list_filter = ('role', 'is_verified')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'date_of_birth')
    search_fields = ('user__email',)

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'years_of_experience', 'availability_status')
    search_fields = ('user__email', 'specialization')
    list_filter = ('availability_status',)

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'date', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'therapist', 'date', 'start_time', 'status', 'payment_status')
    list_filter = ('status', 'payment_status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'payment_method', 'payment_status', 'payment_date')
    list_filter = ('payment_status',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read')

@admin.register(SessionRoom)
class SessionRoomAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'room_link', 'session_status', 'created_at')
    list_filter = ('session_status',)
