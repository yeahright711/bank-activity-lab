
import statistics as stats
from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
             valid_prices = []
             for num in row[1:]:
                 num = num.strip()
            
                 if num and num.replace('.', '', 1).isdigit():
                     price = float(num)
                     valid_prices.append(price)
             print(valid_prices)

             sum_averages = sum(valid_prices)/len(valid_prices)
             averages.append(round(sum_averages, 3))
             print(averages)
               
        return averages

    def median02(self):
        """pt2
        """
        median = []
        for row in self.data:
             valid_prices = []
             for num in row[1:]:
                 num = num.strip()
            
                 if num and num.replace('.', '', 1).isdigit():
                     price = float(num)
                     valid_prices.append(price)
             print(valid_prices)

             sum_median = stats.median(valid_prices)
             median.append(sum_median)
             print(median)
        return median

    def stddev03(self):
        """pt3
        """
        stddev = []
        for row in self.data:
             valid_prices = []
             for num in row[1:]:
                 num = num.strip()
            
                 if num and num.replace('.', '', 1).isdigit():
                     price = float(num)
                     valid_prices.append(price)
             print(valid_prices)

             new_stddev = stats.stdev(valid_prices)
             stddev.append(round(new_stddev, 3))
             print(stddev)

        return stddev
