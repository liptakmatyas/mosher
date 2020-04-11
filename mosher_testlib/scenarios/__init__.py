def alternatives(expected_result, indices):
    return { idx: expected_result for idx in indices }

class ExpectedResult:
    def __init__(self, segment_list, non_empty):
        self.segment_list = segment_list
        self.non_empty = {}

        for index_type in ['a', 'ab', 'abc', 'tuple']:
            if index_type in non_empty:
                self.non_empty[index_type] = alternatives(
                    self.segment_list, non_empty[index_type])

