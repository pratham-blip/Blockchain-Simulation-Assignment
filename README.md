# ✨ Simple Blockchain Simulation ✨

This project is a **basic 🛠️ blockchain** simulation that demonstrates fundamental concepts like:
- **📊 Block structure** (index, timestamp, transactions, previous hash, current hash)
- **⛏️ Proof-of-Work (PoW)** to add computational difficulty in mining
- **📢 Dynamic transaction handling** (users can add transactions before mining)
- **⚖️ Blockchain validation** (detects tampering attempts)

## ✨ Features ✨
✔️ Implements a **linked list of blocks** forming a blockchain  
✔️ Uses **🤖 SHA-256 hashing** to secure each block  
✔️ **⛏️ Proof-of-Work** makes mining computationally expensive  
✔️ **📢 Transaction pool** allows users to add transactions before mining  
✔️ **⚖️ Tampering detection** ensures blockchain integrity  

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd blockchain_project
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Using Docker (Alternative to Virtual Env)
If you want to use Docker to containerize the project, follow these steps:
1. Build the Docker Image:
```bash
docker build -t blockchain-simulation .
```
2. Run the Docker Container:
 ```bash
 docker run blockchain-simulation

   ```


## ⚡ Running the Blockchain

### 1️⃣ Start the Simulation
Run the main script to test the blockchain:
```bash
python main.py
```

### 2️⃣ Example Output
```bash
  Block 0:
  Timestamp: 2025-01-29 06:37:28
  Transactions: Genesis Block
  Previous Hash: 0
  Current Hash: 0000aac8c51d8d0a6d34f194bb93de64
  Nonce: 41059
----------------------------------------
  Block 1:
  Timestamp: 2025-01-29 06:37:28
  Transactions: [{'from': 'Alice', 'to': 'Bob', 'amount': 50}]
  Previous Hash: 0000aac8c51d8d0a6d34f194bb93de64
  Current Hash: 00005e89abd3ab2ee865ab8404622134
  Nonce: 163731
----------------------------------------
 Is blockchain valid? ✅ True
 Tampering Attempt Detected!
 Is blockchain valid after tampering? ❌ False
```

## ⚖️ Security Mechanisms

### ♻️ Proof-of-Work (PoW)
- ⛏️ The blockchain requires miners to find a valid hash starting with `0000`
- ❌ This prevents spam blocks and makes mining computationally expensive

### 📝 Tampering Detection
- ⚠️ If someone modifies a block’s data, the blockchain **recomputes hashes** and detects inconsistencies

### 🛠️ Transactions & Mining
- 📢 Users can add multiple transactions before mining a block
- ⛏️ Mining confirms transactions and adds them to the blockchain


## 🎉 Conclusion
This project successfully simulates blockchain functionality with **PoW**, **transactions**, and **security mechanisms**. Future improvements can include:
- 🎨 A **frontend** to interact with the blockchain
- 📃 A **database** to persist transactions
- 🛠️ Network support for **multi-node blockchain simulation**

## 📚 Credits
Developed by **Pratham** as part of a **🛠️ Blockchain Simulation Assignment**. 

💪 Thank You!!

