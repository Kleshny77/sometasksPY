'''
class Serializer:
    def beginArray(self):
        raise NotImplementedError("BeginArray is not implemented")

    def addArrayItem(self, item):
        raise NotImplementedError("addArrayItem is not implemented")

    def endArray(self):
        raise NotImplementedError("endArray is not implemented")
 class JsonSerializer(Serializer):
 '''
def main():
    print('HI')