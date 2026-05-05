from django.core.management.base import BaseCommand
from root.models import Registered
from miclat.views import verify_nin 
from root import data as data_register

from django.conf import settings
from miclat.models import MiclatData



class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        register = Registered.objects.filter(status=data_register.registration.CHECK_NIN)
        
        for reg in register:

            miclat = MiclatData.objects.filter(nin=reg.nin).first()

            if miclat:
                result = True
            else:
                result = verify_nin(reg.nin)

            if result:
                reg.status = data_register.registration.VERIFIED
                reg.miclat = True
            else:
            
                reg.status = data_register.registration.FAILED 
                reg.miclat = False



            reg.save()

            print(f"NIN {reg.nin} traité")