from rest_framework.views import APIView
from rest_framework.response import Response
from .manager import WalletManager


class  WalletGet(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            notifications_data = WalletManager.manage_licensing(request, data)
            return Response({"result" : "success", "data":notifications_data}, 200)

        except Exception as err:
            return Response(str(err), 500)
