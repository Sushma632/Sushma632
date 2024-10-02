# signals_thread_check.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import logging

# Set up logging to check thread IDs
logging.basicConfig(level=logging.INFO)

# Receiver function for post_save signal
@receiver(post_save, sender=User)
def post_save_user_handler(sender, instance, **kwargs):
    logging.info(f"Signal Handler Thread ID: {threading.get_ident()}")

# Simulate a user save operation and log the main thread ID
def create_user():
    logging.info(f"Main Thread ID: {threading.get_ident()}")
    user = User.objects.create_user(username='testuser', password='testpass')

if __name__ == "__main__":
    create_user()
