from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    cfn_inventory = serializers.FileField(use_url=True)
    inventory_listing = serializers.FileField(use_url=True)
    reserved_inventory = serializers.FileField(use_url=True)

    def create(self, validated_data):


        return
