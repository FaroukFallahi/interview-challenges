from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import docker
from api.serializers import ContainerSerializer

d = docker.from_env()


@api_view(['GET','POST'])
def endpoint(request):
    if request.method == 'GET':
        containers = d.containers.list(all=True)
        containers_attrs = [container.attrs for container in containers]
        serializer = ContainerSerializer(containers_attrs , many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        try:
            container=d.containers.run(
                request.data.get('image'),
                name=request.data.get('name'),
                environment=request.data.get('env'),
                command=request.data.get('command'),
                detach=True,
                )
        except docker.errors.APIError as e:
            return Response({'detail': e.explanation}, status=e.status_code)
        serializer = ContainerSerializer(container.attrs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def endpoint_id(request,id_or_name):
    if request.method == 'GET':
        try:
            container = d.containers.get(id_or_name)
        except docker.errors.APIError as e:
            return Response({'detail': e.explanation}, status=e.status_code)
        serializer = ContainerSerializer(container.attrs)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        try:
            container = d.containers.get(id_or_name)
        except docker.errors.APIError as e:
            return Response({'detail': e.explanation}, status=e.status_code)
        container.stop()
        container.remove()
        return Response( status=status.HTTP_204_NO_CONTENT)
