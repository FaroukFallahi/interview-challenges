from typing import overload, Dict
from rest_framework import serializers

class ContainerSerializer(serializers.Serializer):
    short_id = serializers.CharField()
    name = serializers.CharField( )
    image = serializers.CharField(required=True, allow_blank=False,)
    env = serializers.JSONField( )
    command = serializers.JSONField(required=False)
    status = serializers.CharField( )
    created = serializers.DateTimeField()


    def to_representation(self, data: Dict):
        if data:
            transformed_data = {
                'short_id': data['Id'][:10],
                'image': data['Config']['Image'],
                'name': data['Name'][1:],
                'env': data['Config']['Env'][:-1],
                'command': ' '.join(data['Config']['Cmd']) if data['Config']['Cmd'] != None else None,
                'status': data['State']['Status']  ,
                'created': data['Created']
            }
        else: 
            transformed_data = {}
        return super().to_representation(transformed_data)
     
