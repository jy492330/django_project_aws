from rest_framework.decorators import action
from rest_framework import response
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=["GET"], detail=False, url_path=r"security_group/(?P<group_name>[^/]+)/list")
    def security_group(self, *args, **kwargs):
        group_name = self.kwargs["group_name"]
        users = User.objects.filter(
            groups__name=group_name) 
        serializer_obj = self.serializer_class(users, many=True)
        return response.Response(serializer_obj.data, status=200)
