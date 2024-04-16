import dataclasses

@dataclasses.dataclass
class Method:
    code: int
    type: str

    def __eq__(self, other):
        return self.code==other.code

    def __hash__(self):
        return hash(self.code)