import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now

# Signal handler
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, created, **kwargs):
    print(f"Signal started: {now()}")
    time.sleep(5)  # Simulate a delay in handling the signal
    print(f"Signal completed: {now()}")

# Code to trigger the signal
def test_signal():
    print(f"Before saving: {now()}")
    user = User.objects.create(username="testuser")
    print(f"After saving: {now()}")

# Explanation:
# - The print statement "Before saving" happens before the signal.
# - The print statement "After saving" will not appear until after the 5-second delay in the signal handler.
