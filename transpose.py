class Solution(object):
    def transpose(self, matrix):
        zipped_list = list(map(list, zip(*matrix)))
        return zipped_list

        