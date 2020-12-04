import unittest
import ports

class port_test(unittest.TestCase):
    def test_ex1(self):
        include_ports = [[80, 80], [22, 23], [8000, 9000]]
        exclude_ports = [[1024, 1024], [8080, 8080]] 
        output =  [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]
        self.assertEqual(ports.apply_port_exclusions(include_ports, exclude_ports), output)

    def test_ex2(self):
        include_ports = [[8000, 9000], [80, 80], [22, 23]] 
        exclude_ports = [[1024, 1024], [8080, 8080]] 
        output =  [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]
        self.assertEqual(ports.apply_port_exclusions(include_ports, exclude_ports), output)

    def test_ex3(self):
        include_ports = [[1, 65535]] 
        exclude_ports = [[1000, 2000], [500, 2500]] 
        output = [[1, 499], [2501, 65535]] 
        self.assertEqual(ports.apply_port_exclusions(include_ports, exclude_ports), output)

    def test_ex4(self):
        include_ports = [[1,1], [3, 65535], [2, 2]] 
        exclude_ports = [[1000, 2000], [500, 2500]] 
        output =  [[1, 499], [2501, 65535]] 
        self.assertEqual(ports.apply_port_exclusions(include_ports, exclude_ports), output)
    def test_ex5(self):
        include_ports = []
        exclude_ports = [[8080, 8080]] 
        output =  []
        self.assertEqual(ports.apply_port_exclusions(include_ports, exclude_ports), output)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

