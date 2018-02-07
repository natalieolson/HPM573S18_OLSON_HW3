class Node:
    """ base class """
    def __init__(self, name, cost, utility):
        """
        :param name: name
        :param cost: cost
        :param utility: HUI score
        """
        self.name = name
        self.cost = cost
        self.utility = utility
    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")
    def get_expected_utility(self):
        raise NotImplementedError ("This is an abstract method, will be implemented in derived class")

class ChanceNode(Node):

    def __init__(self, name, cost, utility, future_nodes, probs):

        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        """
        :return: expected cost of this chance node
        """
        exp_utility = self.utility  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i += 1
        return exp_utility

class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_utility(self):
        return self.utility

class DecisionNode(Node):

    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        costoutcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            costoutcomes[node.name] = node.get_expected_cost()

        return costoutcomes

    def get_expected_utility(self):
        """ returns the expected costs of future nodes"""
        utilityoutcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            utilityoutcomes[node.name] = node.get_expected_utility()

        return utilityoutcomes

#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2
C2 = ChanceNode('C2', 35, 0, [T1, T2], [0.7, 0.3])
# create C1
C1 = ChanceNode('C1', 25,0, [C2, T3], [0.2, 0.8])
# create C3
C3 = ChanceNode('C3', 45, 0, [T4, T5], [0.1, 0.9])

# create D1
D1 = DecisionNode('D1', 0, 0, [C1, C3])

# print the expect cost of C1
print(C1.get_expected_cost())
print(C3.get_expected_cost())
print(C1.get_expected_utility())
print(C3.get_expected_utility())
