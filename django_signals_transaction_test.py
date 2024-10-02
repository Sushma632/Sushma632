from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Sample model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal triggered")

# A function to test transaction behavior
def transaction_test():
    # Begin a transaction
    with transaction.atomic():
        # Create a new instance of MyModel
        obj = MyModel.objects.create(name="Test Object")
        
        # Signal is triggered here after save
        print("Object saved but transaction not committed yet")

        # Rollback the transaction to cancel the save
        raise Exception("Rolling back transaction!")

try:
    transaction_test()
except Exception as e:
    print(e)
