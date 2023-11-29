import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate

def test(name, perceptron: Perceptron, expect: list[int]) -> None:
    print("---------------------------------------")
    print(f"Teste para {name}")
    POSSIBILITIES = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    for possibility, e in zip(POSSIBILITIES, expect):
        print(f"in ({possibility[0]}, {possibility[1]}), Expect: {e} , out: {perceptron.predict(possibility)}")
      
    print("---------------------------------------")

# Exemplo de uso
if __name__ == "__main__":
    '''
    ------- AND -------
    '''
    X_AND = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Entradas
    y_and = np.array([0, 0, 0, 1]) # Saídas esperadas

    perceptron_and = Perceptron()
    perceptron_and.train(X_AND, y_and)
    test("AND", perceptron_and, y_and)

    '''
    ------- OR -------
    '''
    X_OR = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Entradas
    y_or = np.array([0, 1, 1, 1]) # Saídas esperadas

    perceptron_or = Perceptron()
    perceptron_or.train(X_OR, y_or)
    test("OR", perceptron_or, y_or)

    '''
    ------- NAND -------
    '''
    X_NAND = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Entradas
    y_nand = np.array([1, 1, 1, 0]) # Saídas esperadas

    perceptron_nand = Perceptron()
    perceptron_nand.train(X_NAND, y_nand)
    test("NAND", perceptron_nand, y_nand)

    '''
    ------- XOR -------
    '''
    X_XOR = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Entradas
    y_xor = np.array([0, 1, 1, 0]) # Saídas esperadas

    perceptron_xor = Perceptron()
    perceptron_xor.train(X_XOR, y_xor)
    test("XOR", perceptron_xor, y_xor)