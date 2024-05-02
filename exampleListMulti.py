from src.datadebug import logger, class_decorator, List


class Number:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)
    
    def add_child(self, node):
        self.children.append(node)
        logger.add_edge(self, node, display=True)


if __name__ == "__main__":

    number_10 = Number(10)
    number_20 = Number(20)
    number_30 = Number(30)
    number_40 = Number(40)
    number_50 = Number(50)
    number_60 = Number(60)

    number_40.add_child(number_50)
    number_40.add_child(number_20)
    number_20.add_child(number_30)
    number_20.add_child(number_10)
    number_50.add_child(number_60)

    l = List([number_10, number_20, number_30, number_40, number_50, number_60])

    number_70 = Number(70)
    number_80 = Number(80)
    number_90 = Number(90)
    number_100 = Number(100)
    number_110 = Number(110)

    number_100.add_child(number_110)
    number_100.add_child(number_80)
    number_80.add_child(number_90)
    number_80.add_child(number_70)

    l2 = List([number_70, number_80, number_90, number_100, number_110])

    number_65 = Number(65)
    number_70.add_child(number_65)
    number_60.add_child(number_65)

    for node in l:
        logger.add_pointer(node, "current", display_once=True)
