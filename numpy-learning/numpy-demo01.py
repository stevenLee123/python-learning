import numpy as np
# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#激活函数的导数
def sigmoid_derivative(x):
    return x * (1 - x)

# 输入层、隐藏层、输出层的节点数
input_size = 3
hidden_size = 4
output_size = 2

# 随机初始化权重
np.random.seed(0)
# 输入层到隐藏层的权重和输出层到隐藏层的权重
weights_input_hidden = np.random.randn(input_size, hidden_size)
print(weights_input_hidden)
weights_hidden_output = np.random.randn(hidden_size, output_size)
print(weights_hidden_output)

# 随机初始化偏置
bias_hidden = np.random.randn(1, hidden_size)
bias_output = np.random.randn(1, output_size)

# 前向传播
def forward_propagation(X):
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)
    
    return predicted_output, hidden_layer_output

# 计算损失
def compute_loss(y_true, y_pred):
    return 0.5 * np.sum((y_true - y_pred) ** 2)

# 反向传播
def backward_propagation(X, y_true, y_pred, hidden_layer_output):
    # 计算输出层误差
    output_error = y_true - y_pred
    output_delta = output_error * sigmoid_derivative(y_pred)
    
    # 计算隐藏层误差
    hidden_error = output_delta.dot(weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)
    
    # 更新权重和偏置
    weights_hidden_output += hidden_layer_output.T.dot(output_delta)
    bias_output += np.sum(output_delta, axis=0, keepdims=True)
    
    weights_input_hidden += X.T.dot(hidden_delta)
    bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True)

    
# 示例数据
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0, 1], [1, 0], [1, 0], [0, 1]])

epochs = 10000
# 学习率
learning_rate = 0.1

for epoch in range(epochs):
    y_pred, hidden_layer_output = forward_propagation(X)
    loss = compute_loss(y, y_pred)
    
    if epoch % 1000 == 0:
        print(f'Epoch {epoch}, Loss: {loss}')
    
    backward_propagation(X, y, y_pred, hidden_layer_output)    

# 测试
test_input = np.array([[1, 0, 0]])
predicted_output, _ = forward_propagation(test_input)
print("预测输出:", predicted_output)    