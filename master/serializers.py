import re

from rest_framework import serializers

from .models import Pattern

PATTERN1 = r'(\${\w+})'
PATTERN2 = r'(\${(\w+)})'


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ['pk', 'string', 'lst_variable']
        read_only_fields = ['lst_variable']

    def get_data(self, string):
        prepared = re.split(PATTERN1, string)
        count_variable = 0
        lst_variable = []
        for i in prepared:
            match = re.fullmatch(PATTERN2, i)
            if match and match[2] not in lst_variable:
                count_variable += 1
                lst_variable.append(match[2])
        return string, prepared, count_variable, lst_variable

    def create(self, validated_data):
        string, prepared, count_variable, lst_variable = self.get_data(validated_data['string'])
        return Pattern.objects.create(string=string,
                                      prepared=prepared,
                                      count_variable=count_variable,
                                      lst_variable=lst_variable)

    def update(self, instance, validated_data):
        if instance.string != validated_data.get('string'):
            string, prepared, count_variable, lst_variable = self.get_data(validated_data['string'])
            instance.string = string
            instance.prepared = prepared
            instance.count_variable = count_variable
            instance.lst_variable = lst_variable
            instance.save()
        return instance


class GenerateSerializer(serializers.Serializer):
    data = serializers.HStoreField(child=serializers.CharField())
