import numpy as np

# *********************************************************************************
# Parameters for Figure 1
D0_1 = np.array([
    [-2.11, 0.1, 0.0, 0.0, 0.01],
    [0.1, -2.61, 0.5, 0.0, 0.01],
    [0.1, 0.2, -5.4, 0.0, 0.1],
    [0.1, 0.1, 0.3, -3.5, 0.0],
    [0.1, 0.1, 0.1, 0.1, -100.4]
])

D1_1 = np.array([
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [1, 2, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 100]
])

# *********************************************************************************
# Parameters for Figure 2
D0_2 = np.array([
    [-7, 2, 3, 0],
    [3, -12, 1, 5],
    [1, 2, -12, 6],
    [8, 8, 0, -19]
])
D1_2 = np.array([
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1]
])
# *********************************************************************************
# Parameters for Figure 3
# Top Left
D0_3a = np.array([
    [-2.02, 0.01, 0.01],
    [0.1, -7.2, 0.1],
    [0, 0.01, -16.01]
])
D1_3a = np.array([
    [1, 0, 1],
    [1, 5, 1],
    [0, 1, 15]
])
# *********************************************************************************
# Parameters for Figure 3
# Top Right
D0_3b =np.array([
    [-2.2, 0.1, 0, 0, 0.1],
    [0.1, -2.7, 0.5, 0, 0.1],
    [0.1, 0.2, -5.4, 0, 0.1],
    [0.1, 0.1, 0.3, -3.5, 0],
    [0.1, 0.1, 0.1, 0.1, -15.4]
])
D1_3b = np.array([
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [1, 2, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 15]
])
# *********************************************************************************
# Parameters for Figure 3
# Bottom Left panel
N = 10
D0_3c = np.zeros((N, N))

for i in range(1, 3):
    np.random.seed(42 + i)
    diag = np.random.uniform(low=0, high=2, size=N - i)
    for k in range(N - i):
        D0_3c[k, k + i] = diag[k]

for i in range(1, 4):
    np.random.seed(42 - i)
    diag = np.random.uniform(low=0, high=2, size=N - i)
    for k in range(N - i):
        D0_3c[k + i, k] = diag[k]

D1_3c = np.zeros((N, N))

diag = np.random.uniform(low=0, high=5, size=N)
for k in range(N):
    D1_3c[k, k] = diag[k]

for i in range(1, 4):
    np.random.seed(42 + i)
    diag = np.random.uniform(low=0, high=3, size=N - i)
    for k in range(N - i):
        D1_3c[k, k + i] = diag[k]

for i in range(1, 4):
    np.random.seed(42 - i)
    diag = np.random.uniform(low=0, high=2, size=N - i)
    for k in range(N - i):
        D1_3c[k + i, k] = diag[k]

# Calculate and fill diagonal elements of D0
for i in range(N):
    # Calculate sum of non-diagonal elements in row i of D0
    D0_3c_rowsum = np.sum(D0_3c[i, :])  # Current diagonal element initialized as 0
    # Calculate sum of all elements in row i of D1
    D1_3c_rowsum = np.sum(D1_3c[i, :])
    # Set diagonal element of D0
    D0_3c[i, i] = -(D0_3c_rowsum + D1_3c_rowsum)
# *********************************************************************************
# Parameters for Figure 3
# Bottom Right panel
N = 20
D0_3d = np.zeros((N, N))

for i in range(1, 21):
    np.random.seed(42 + i)
    diag = np.random.uniform(low=0, high=2, size=N - i)
    for k in range(N - i):
        D0_3d[k, k + i] = diag[k]

for i in range(1, 21):
    np.random.seed(42 - i)
    diag = np.random.uniform(low=0, high=2, size=N - i)
    for k in range(N - i):
        D0_3d[k + i, k] = diag[k]

D1_3d = np.zeros((N, N))

diag = np.random.uniform(low=0, high=3, size=N)
for k in range(N):
    D1_3d[k, k] = diag[k]

for i in range(1, 6):
    np.random.seed(42 + i)
    diag = np.random.uniform(low=0, high=1, size=N - i)
    for k in range(N - i):
        D1_3d[k, k + i] = diag[k]

for i in range(1, 21):
    np.random.seed(42 - i)
    diag = np.random.uniform(low=0, high=1, size=N - i)
    for k in range(N - i):
        D1_3d[k + i, k] = diag[k]

# Calculate and fill diagonal elements of D0
for i in range(N):
    # Calculate sum of non-diagonal elements in row i of D0
    D0_3d_rowsum = np.sum(D0_3d[i, :])  # Current diagonal element initialized as 0
    # Calculate sum of all elements in row i of D1
    D1_3d_rowsum = np.sum(D1_3d[i, :])
    # Set diagonal element of D0
    D0_3d[i, i] = -(D0_3d_rowsum + D1_3d_rowsum)
    
# *********************************************************************************
# Parameters for Figure 4 and Figure 5
def generate_D0n(n):
    return np.diag([-i * n for i in range(1, n + 1)])

def generate_D1n(n):
    return np.array([[i] * n for i in range(1, n + 1)])
