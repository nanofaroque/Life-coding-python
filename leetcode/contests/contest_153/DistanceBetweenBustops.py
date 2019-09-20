import unittest


class TestDistanceBetweenBusStop(unittest.TestCase):

    def distance_between_bus_stops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        return 100

    def test_first_distance_between_bus_stops(self):
        distance = [1, 2, 3, 4]
        start = 0
        destination = 1
        result = self.distance_between_bus_stops(distance, start, destination)
        print(result)


if __name__ == '__main__':
    unittest.main()
