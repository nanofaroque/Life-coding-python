import unittest


def clockwise_distance(distance, start, destination):
    dist = 0
    for counter in range(start, destination):
        dist += distance[counter]
    return dist


def anti_clockwise_distance(distance, start, destination):
    if start == destination:
        return 0
    dist = 0
    # zero to point
    for counter in range(0, start):
        dist += distance[counter]
    # point to end
    for counter in range(destination, len(distance) - 1):
        dist += distance[counter]
    # end to point
    dist += distance[len(distance) - 1]
    return dist


class TestDistanceBetweenBusStop(unittest.TestCase):

    def distance_between_bus_stops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start < destination:
            clock_distance = clockwise_distance(distance, start, destination)
        else:
            clock_distance = clockwise_distance(distance, destination, start)

        # clock_distance = clockwise_distance(distance, start, destination)
        print('clockwise distance' + str(clock_distance))

        if start < destination:
            anti_clock_distance = anti_clockwise_distance(distance, start, destination)
        else:
            anti_clock_distance = anti_clockwise_distance(distance, destination, start)
        return min(clock_distance, anti_clock_distance)

    def test_first_distance_between_bus_stops(self):
        distance = [7, 10, 1, 12, 11, 14, 5, 0]
        start = 7
        destination = 2
        result = self.distance_between_bus_stops(distance, start, destination)
        self.assertEqual(result, 17, "distance should be 4")


if __name__ == '__main__':
    unittest.main()
