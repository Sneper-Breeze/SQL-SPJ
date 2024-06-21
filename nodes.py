import csv
from sys import getsizeof


class AbstractNode:

    def __init__(self):
        self.__LChild = None
        self.__RChild = None
        self.__internalState = []
        self.size_of_tuple = 70
        self.iter_for_next = None

    def give_LChind(self):
        return self.__LChild

    def give_RChind(self):
        return self.__RChild

    def set_LChild(self, node):
        self.__LChild = node

    def set_RChild(self, node):
        self.__RChild = node

    def get_iter_for_next(self):
        pass

    def open(self):
        self.iter_for_next = self.get_iter_for_next()
        if (self.__RChild is not None):
            self.give_RChind().open()
        if (self.__LChild is not None):
            self.give_LChind().open()

    def close(self):
        self.iter_for_next = None
        if (self.__RChild is not None):
            self.give_RChind().close()
        if (self.__LChild is not None):
            self.give_LChind().close()

    def get_next(self):
        try:
            return next(self.iter_for_next)
        except StopIteration:
            return None

    def reset(self):
        self.__internalState = []
        if (self.__LChild is not None):
            self.__LChild.reset()
        if (self.__RChild is not None):
            self.__RChild.reset()
        self.iter_for_next = self.get_iter_for_next()


class SelectNode(AbstractNode):
    def __init__(self, collumns: list[str]):
        super().__init__()
        self.collumns = collumns

    def get_only_collumns(self, row):
        if ('*' in self.collumns):
            return row

        return {key: row[key] for key in self.collumns}

    def get_iter_for_next(self):
        table = self.give_LChind()

        data_blck = table.get_next()
        while data_blck is not None:
            for row in data_blck:
                self._AbstractNode__internalState.append(self.get_only_collumns(row))

                if getsizeof(self._AbstractNode__internalState) > self.size_of_tuple:
                    yield self._AbstractNode__internalState
                    self._AbstractNode__internalState = []

            data_blck = table.get_next()

        if len(self._AbstractNode__internalState) != 0:
            yield self._AbstractNode__internalState


class JoinNode(AbstractNode):
    def __init__(self, col1: str, col2: str):
        super().__init__()
        self.col1 = col1
        self.col2 = col2

    def get_iter_for_next(self):
        rtable = self.give_RChind()
        ltable = self.give_LChind()

        rdata_blck = rtable.get_next()
        while rdata_blck is not None:
            if (self.col2 not in rdata_blck[0]):
                self.col1, self.col2 = self.col2, self.col1
            for rEl in rdata_blck:
                ldata_blck = ltable.get_next()
                while ldata_blck is not None:
                    for lEl in ldata_blck:
                        if (lEl[self.col1] == rEl[self.col2]):
                            lEl.update(rEl)
                            self._AbstractNode__internalState.append(lEl)

                        if getsizeof(self._AbstractNode__internalState) > self.size_of_tuple:
                            yield self._AbstractNode__internalState
                            self._AbstractNode__internalState = []

                    ldata_blck = ltable.get_next()

                ltable.reset()

            rdata_blck = rtable.get_next()

        if len(self._AbstractNode__internalState) != 0:
            yield self._AbstractNode__internalState


class WhereNode(AbstractNode):
    def __init__(self, a: str, b: str, comps: list[str]):
        super().__init__()
        self.a = a
        self.b = b
        self.comps = comps

    def check_with_var(self, row):
        res = False
        if self.a not in row:
            self.a, self.b = self.b, self.a
            self.comps = ['<' if comp == '>' else '>' if comp == '<' else '=' for comp in self.comps]

        if '<' in self.comps:
            if (self.b.isdigit() and row[self.a].isdigit()):
                res = res or (int(row[self.a]) < int(self.b))
            else:
                res = res or (row[self.a] < self.b)
        if '>' in self.comps:
            if (self.b.isdigit() and row[self.a].isdigit()):
                res = res or (int(row[self.a]) > int(self.b))
            else:
                res = res or (row[self.a] > self.b)
        if '=' in self.comps:
            if (self.b.isdigit() and row[self.a].isdigit()):
                res = res or (int(self.b) == int(row[self.a]))
            else:
                res = res or (self.b == row[self.a])
        return res

    def check_with_atr(self, row):
        res = False
        if '<' in self.comps:
            if (row[self.b].isdigit() and row[self.a].isdigit()):
                res = res or (int(row[self.a]) < int(row[self.b]))
            else:
                res = res or (row[self.a] < row[self.b])
        if '>' in self.comps:
            if (row[self.b].isdigit() and row[self.a].isdigit()):
                res = res or (int(row[self.a]) > int(row[self.b]))
            else:
                res = res or (row[self.a] > int(row[self.b]))
        if '=' in self.comps:
            if (row[self.b].isdigit() and row[self.a].isdigit()):
                res = res or (int(row[self.b]) == int(row[self.a]))
            else:
                res = res or (row[self.b] == row[self.a])

        return res

    def get_iter_for_next(self):
        table = self.give_LChind()

        data_blck = table.get_next()
        while data_blck is not None:
            with_var = (self.a not in data_blck[0] or self.b not in data_blck[0])

            for row in data_blck:
                if with_var is True and self.check_with_var(row):
                    self._AbstractNode__internalState.append(row)
                elif with_var is False and self.check_with_atr(row):
                    self._AbstractNode__internalState.append(row)
                if getsizeof(self._AbstractNode__internalState) > self.size_of_tuple:
                    yield self._AbstractNode__internalState
                    self._AbstractNode__internalState = []

            data_blck = table.get_next()

        if len(self._AbstractNode__internalState) != 0:
            yield self._AbstractNode__internalState


class TableNode(AbstractNode):
    __file_stream = None

    def __init__(self, table_name: str, path: str):
        super().__init__()
        self.table_name = table_name
        self.table_path = f'{path}/{table_name}.csv'

    def open(self):
        self.__file_stream = open(self.table_path, 'r')
        super().open()

    def close(self):
        self.__file_stream.close()
        super().close()

    def get_iter_for_next(self):
        reader = csv.DictReader(self.__file_stream, delimiter=' ', quotechar='|')
        for row in reader:
            self._AbstractNode__internalState.append(row)
            if getsizeof(self._AbstractNode__internalState) > self.size_of_tuple:
                yield [{f'{self.table_name}.{k}': v for k, v in row.items()}
                       for row in self._AbstractNode__internalState]
                self._AbstractNode__internalState = []
        if len(self._AbstractNode__internalState) != 0:
            yield [{f'{self.table_name}.{k}': v for k, v in row.items()} for row in self._AbstractNode__internalState]

    def reset(self):
        super().reset()
        self.close()
        self.open()
