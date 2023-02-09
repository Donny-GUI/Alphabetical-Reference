
class AlphabeticalReference:
    def __init__(self, list_of: list[dict[str:dict]] | list[str], key):

        self.key = key
        self.list = list_of
        self.reference = {}
        self.tags = []
        self.key_string = True if isinstance(self.key, str) else False


class SortedBy(AlphabeticalReference):
    def __init__(self, list_of: list[dict[str:dict]], key: str):
        super().__init__(list_of, key)

        for item in self.list:
            item_attribute = item[self.key]
            tag = item_attribute[0]
            self.tags.append(tag)
            self.reference[tag] = []
        for item in self.list:
            item_attribute = item[self.key]
            tag = item_attribute[0]
            self.reference[tag].append(item)
            
    def options(self):
        alpha_dict = {}
        for tag in tags:
            alpha_dict[tag] = []
            for item in self.reference[tag]:
                alpha_dict[tag].append(item[self.key])
        return alpha_dict
            
    
    def get_key(self):
        return self.key

    def find(self, item: any) -> bool | dict:

        tag = item[0]
        for ref in self.reference[tag]:
            if ref[self.key] == item:
                return ref


class Sorted(AlphabeticalReference):
    def __init__(self, list_of: list[dict[str:dict]] | list[str], key: str | None = None):
        super().__init__(list_of, key)
        self.key_string = False
        for item in self.list:
            tag = item[0]
            self.tags.append(tag)
            self.reference[tag] = []
        for item in self.list:
            tag = item[0]
            self.reference[tag].append(item)
    
    def find(self, item: str):
        tag = item[0]
        for ref in self.reference[tag]:
            if ref == item:
                return True
        return False
