from typing import List
from scipy.spatial import KDTree
import numpy as np


class Element1D:
    """
    This class represents the 1D elements
    """

    id: int
    property_id: int
    node1: int
    node2: int
    all_elements = []

    def __init__(self, element_id: int, property_id: int, node1: int, node2: int):
        self.id = element_id
        self.property_id = property_id
        self.node1 = node1
        self.node2 = node2
        Element1D.all_elements.append(self)


class Element:
    """
    This class is used to store the 2D/3D elements
    """

    id: int
    property_id: int
    nodes: list = []
    all_elements = []
    centroid: list = []

    def __init__(self, element_id: int, property_id: int, nodes: list):
        self.id = element_id
        self.property_id = property_id
        self.nodes = nodes
        for node in nodes:
            node.add_element(self)
        self.centroid = self.__calculate_centroid()
        self.neighbors = []
        Element.all_elements.append(self)

    def __calculate_centroid(self):
        """
        This method calculates the centroid of the element
        """
        centroid = [0, 0, 0]
        for node in self.nodes:
            for i in range(3):
                centroid[i] += node.coords[i]
        for i in range(3):
            centroid[i] /= len(self.nodes)
        return centroid

    @staticmethod
    def get_neighbors():
        """
        Calculate the neigbours by making use of a KDTree, 3 dimensions, using the centroid
        Get the 30 closest potential neighbors and check if they are really neighbors by
        checking if they share nodes
        """

        coords = [element.centroid for element in Element.all_elements]
        tree = KDTree(np.array(coords))
        for element in Element.all_elements:
            neighbors = tree.query(element.centroid, k=30)

            for potential_neighbor_index in neighbors[1]:
                potential_neighbor = Element.all_elements[potential_neighbor_index]

                # contition to avoid self as neighbor
                if element.id == potential_neighbor.id:
                    continue

                # check if the element and the potential neighbor share nodes
                if set(element.nodes).intersection(potential_neighbor.nodes):
                    # check if the neighbor alredy has the element in its neighbors
                    if element not in potential_neighbor.neighbors:
                        potential_neighbor.neighbors.append(element)
                    # check if the element alredy has the potential neighbor in its neighbors
                    if potential_neighbor not in element.neighbors:
                        element.neighbors.append(potential_neighbor)

    def get_all_connected_elements(self, connected_elements: List) -> List:
        """
        This method returns all connected elements to the given element
        """
        if len(connected_elements) == 0:
            connected_elements.append(self)

        len_before = len(connected_elements)

        # loop through all connected elements and add all  the neighbors to the connected_elements
        for element in connected_elements:
            for neighbor in element.neighbors:
                if neighbor not in connected_elements:
                    connected_elements.append(neighbor)

        len_after = len(connected_elements)

        if len_before == len_after:
            return connected_elements
        return self.get_all_connected_elements(connected_elements)

    def get_all_connected_nodes(self) -> List:
        """
        This method returns all connected nodes to the given element
        """
        connected_elementes = self.get_all_connected_elements([self])
        connected_nodes = []
        for element in connected_elementes:
            for node in element.nodes:
                if node not in connected_nodes:
                    connected_nodes.append(node)

        return connected_nodes


class Node:
    """
    This class is used to store the nodes
    """

    id: int
    coords: List = []
    all_nodes: List = []
    connected_elements: List = []

    def __init__(self, node_id: int, coords: List):
        self.id = node_id
        self.coords = coords
        Node.all_nodes.append(self)
        self.connected_elements = []

    def add_element(self, element):
        """
        This method adds the element to the connected elements
        """
        if element not in self.connected_elements:
            self.connected_elements.append(element)
