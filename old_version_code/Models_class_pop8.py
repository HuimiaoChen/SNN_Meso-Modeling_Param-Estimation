import torch.nn as nn
import torch.nn.functional as F

class MultiTaskNet_T(nn.Module):
    def __init__(self):
        super(MultiTaskNet_T, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=50, num_layers=1, batch_first=True)
        self.fc_J_syn = nn.Linear(50, 8*8)
        self.fc_mu = nn.Linear(50, 8)
        self.fc_tau_m = nn.Linear(50, 8)
        self.fc_V_th = nn.Linear(50, 8)
        self.fc_J_theta = nn.Linear(50, 8)
        self.fc_tau_theta = nn.Linear(50, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta


class MultiTaskNet_S(nn.Module):
    def __init__(self):
        super(MultiTaskNet_S, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=100, num_layers=1, batch_first=True)
        self.fc_J_syn = nn.Linear(100, 8*8)
        self.fc_mu = nn.Linear(100, 8)
        self.fc_tau_m = nn.Linear(100, 8)
        self.fc_V_th = nn.Linear(100, 8)
        self.fc_J_theta = nn.Linear(100, 8)
        self.fc_tau_theta = nn.Linear(100, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta
    
class MultiTaskNet_M(nn.Module):
    def __init__(self):
        super(MultiTaskNet_M, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=200, num_layers=2, batch_first=True, dropout=0.2)
        self.fc1 = nn.Linear(200, 100)
        self.fc_J_syn = nn.Linear(100, 8*8)
        self.fc_mu = nn.Linear(100, 8)
        self.fc_tau_m = nn.Linear(100, 8)
        self.fc_V_th = nn.Linear(100, 8)
        self.fc_J_theta = nn.Linear(100, 8)
        self.fc_tau_theta = nn.Linear(100, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output
        x = F.relu(self.fc1(x))  # Add an extra linear layer with ReLU activation

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta

class MultiTaskNet_L(nn.Module):
    def __init__(self):
        super(MultiTaskNet_L, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=200, num_layers=3, batch_first=True, dropout=0.2)
        self.fc1 = nn.Linear(200, 150)
        self.fc2 = nn.Linear(150, 100)
        self.fc_J_syn = nn.Linear(100, 8*8)
        self.fc_mu = nn.Linear(100, 8)
        self.fc_tau_m = nn.Linear(100, 8)
        self.fc_V_th = nn.Linear(100, 8)
        self.fc_J_theta = nn.Linear(100, 8)
        self.fc_tau_theta = nn.Linear(100, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output
        x = F.relu(self.fc1(x))  # Add an extra linear layer with ReLU activation
        x = F.relu(self.fc2(x))  # Add another extra linear layer with ReLU activation

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta

class MultiTaskNet_LL(nn.Module):
    def __init__(self):
        super(MultiTaskNet_LL, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=300, num_layers=2, batch_first=True, dropout=0.2)
        self.fc1 = nn.Linear(300, 200)
        self.fc2 = nn.Linear(200, 100)
        self.fc_J_syn = nn.Linear(100, 8*8)
        self.fc_mu = nn.Linear(100, 8)
        self.fc_tau_m = nn.Linear(100, 8)
        self.fc_V_th = nn.Linear(100, 8)
        self.fc_J_theta = nn.Linear(100, 8)
        self.fc_tau_theta = nn.Linear(100, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output
        x = F.relu(self.fc1(x))  # Add an extra linear layer with ReLU activation
        x = F.relu(self.fc2(x))  # Add another extra linear layer with ReLU activation

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta

class MultiTaskNet_LLL(nn.Module):
    def __init__(self):
        super(MultiTaskNet_LLL, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=400, num_layers=2, batch_first=True, dropout=0.2)
        self.fc1 = nn.Linear(400, 350)
        self.fc2 = nn.Linear(350, 300)
        self.fc_J_syn = nn.Linear(300, 8*8)
        self.fc_mu = nn.Linear(300, 8)
        self.fc_tau_m = nn.Linear(300, 8)
        self.fc_V_th = nn.Linear(300, 8)
        self.fc_J_theta = nn.Linear(300, 8)
        self.fc_tau_theta = nn.Linear(300, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output
        x = F.relu(self.fc1(x))  # Add an extra linear layer with ReLU activation
        x = F.relu(self.fc2(x))  # Add another extra linear layer with ReLU activation

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta

class MultiTaskNet_X(nn.Module):
    def __init__(self):
        super(MultiTaskNet_X, self).__init__()
        self.gru = nn.GRU(input_size=8, hidden_size=400, num_layers=3, batch_first=True, dropout=0.2)
        self.fc1 = nn.Linear(400, 200)
        self.fc2 = nn.Linear(200, 100)
        self.fc_J_syn = nn.Linear(100, 8*8)
        self.fc_mu = nn.Linear(100, 8)
        self.fc_tau_m = nn.Linear(100, 8)
        self.fc_V_th = nn.Linear(100, 8)
        self.fc_J_theta = nn.Linear(100, 8)
        self.fc_tau_theta = nn.Linear(100, 8)

    def forward(self, x):
        x, _ = self.gru(x)  # Shape of output x: (batch_size, seq_len, hidden_size)
                            # Shape of output x: (batch_size, seq_len, input_size)
        x = x[:, -1, :]  # We only need the last time step's output
        x = F.relu(self.fc1(x))  # Add an extra linear layer with ReLU activation
        x = F.relu(self.fc2(x))  # Add another extra linear layer with ReLU activation

        J_syn = self.fc_J_syn(x).view(-1, 8, 8)
        mu = self.fc_mu(x)
        tau_m = self.fc_tau_m(x)
        V_th = self.fc_V_th(x)
        J_theta = self.fc_J_theta(x).view(-1, 8, 1)
        tau_theta = self.fc_tau_theta(x).view(-1, 8, 1)

        return J_syn, mu, tau_m, V_th, J_theta, tau_theta