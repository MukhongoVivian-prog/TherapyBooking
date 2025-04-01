# THERAPY BOOKING SYSTEM
## SCOPE AND PROJECT DEFINITION

### 1. Users & Roles
    • Patients:
        ◦ View available therapists and their specializations.
        ◦ Book, reschedule, or cancel therapy sessions (cancellation allowed up to 24 hours before).
        ◦ Pay for sessions before confirmation.
        ◦ Receive notifications (booking confirmation, therapist approval, payment updates, and reminders).
        ◦ Access a virtual session room after confirmation.
    • Therapists:
        ◦ Set their availability (time slots for booking).
        ◦ View and manage appointments.
        ◦ Confirm or decline patient bookings.
    • Admin:
        ◦ Monitor all bookings and session activities.
        ◦ Manage therapists (approve, deactivate, or modify details).
### 2. Core Features
    • Appointments & Scheduling:
        ◦ Patients book available time slots set by therapists.
        ◦ Therapists confirm or reject bookings.
        ◦ Patients can cancel or reschedule within a 24-hour window.
    • Therapist Management:
        ◦ List of therapists with their specializations.
        ◦ Patients assigned to therapists based on availability or preference.
    • Payments:
        ◦ Patients must pay before the session is confirmed.
        ◦ Payment records stored for tracking.
    • Virtual Session Room:
        ◦ Patients access a virtual session link after confirmation.
    • Notifications:
        ◦ Automatic emails/SMS for booking confirmations, payment updates, and session reminders.
### 3. Tech Stack
    • Backend: Django & Django REST Framework (DRF)
    • Database: PostgreSQL
    
