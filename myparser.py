from object import Item



class Parser:

    def parse_object(self, content):

        return Item(
            property_1=self.get_property_1(content),
            property_2=self.get_property_2(content),
            property_3=self.get_property_3(content),
            property_4=self.get_property_4(content),
        )

    def get_property_1(self, content):
        return content['date']

    def get_property_2(self, content):
        return content['lie']

    def get_property_3(self, content):
        return content['explanation']

    def get_property_4(self, content):
        return content['url']