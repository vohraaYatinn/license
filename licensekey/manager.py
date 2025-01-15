from .models import LicenseKey


class WalletManager:
    @staticmethod
    def manage_licensing(request, data):
        license = data.get("licence_key", False)
        device = data.get("uuid", False)
        try:
            license_key = LicenseKey.objects.get(license=license)
            if license_key.registered and license_key.device == device and license_key.is_active :
                return True
            elif not license_key.registered and not license_key.device:
                license_key.device = device
                license_key.registered = True
                license_key.save()
                return True
            return False
        except:
            return False





