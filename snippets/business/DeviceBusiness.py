from snippets.models import Device
from django.db.models import Q


class DeviceBusiness:
    def __init__(self):
        pass

    @staticmethod
    def getByCode(code):
        device = Device.objects.filter(code=code)

        if device:
            return device[0]

        return False

    @staticmethod
    def countActiveByUserId(userId):
        return Device.objects.filter(user=userId, status=1).__len__()

    @staticmethod
    def isActiveByCode(code):
        device = DeviceBusiness().getByCode(code)

        if device:
            return bool(device.status)

        return True

    @staticmethod
    def inactivateAllExceptCode(code):
        device = DeviceBusiness().getByCode(code)

        if device and device.user:
            device_record = Device.objects.filter(Q(user=device.user) & Q(status=1) & ~Q(id=device.id))

            if device_record:
                device_record[0].status = 0
                device_record[0].save()
