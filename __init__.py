from optimal import *
from defaults import *


class Optimal:
    def __init__(self, data, data_format=FORMAT):
        self.format = data_format
        self.data = data

    def __optimal__(self, data):
        pass

    def get_optimal(self):
        for i in self.data:
            if len(i) == len(self.format):
                converted_data = list()

                for f, j, n in zip(self.format, i, data_types_names):
                    try:
                        converted_data.append(data_types[f](j))

                    except ValueError as e:
                        raise ValueError("the format is incorrect; cannot convert `%s` into %s" % (str(e), n))

                return self.__optimal__(converted_data)

            else:
                raise ValueError("format and data aren't compatible")
