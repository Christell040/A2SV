class ListStatistics:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        maximum = max(self.data)
        minimum = min(self.data)

        total_sum = 0
        count = 0

        for value in self.data:
            if value != maximum and value != minimum:
                total_sum += value
                count += 1

        if count == 0:
            return 0
        else:
            average = total_sum / count
            return average


listz = [100, 200, 300, 400]
stats = ListStatistics(listz)
average = stats.calculate_average()
print(average)
