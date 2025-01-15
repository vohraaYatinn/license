from .models import LicenseKey


class WalletManager:
    @staticmethod
    def manage_licensing(request, data):
        license = data.get("licence_key", False)
        device = data.get("uuid", False)
        try:
            license_key = LicenseKey.objects.filter(license=license)
            if license_key[0].registered and license_key[0].device == device and license_key[0].is_active :
                return True
            elif not license_key[0].registered and not license_key[0].device:
                license_key[0].device = device
                license_key[0].registered = True
                license_key[0].save()
                return True
            return False
        except:
            return False





