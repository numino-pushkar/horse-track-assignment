
```markdown
# 🐎 Horse Track Betting Machine

This is a command-line simulation of a Horse Track Betting Machine. It supports placing bets on horses, dispensing winnings using available cash denominations, setting race winners, restocking inventory, and handling invalid commands gracefully.

---

## 📦 Project Structure

.
├── app/
│   ├── commands/          # Command implementations
│   ├── model/             # Horse and inventory models
│   ├── constants/         # Constants (command strings, etc.)
│   ├── exceptions/        # Custom exceptions
│   ├── config.py          # Config for horses and cash inventory
│   └── main.py            # Entry point of the app
├── tests/                 # Unit tests for all modules
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── pytest.ini             # Pytest config (optional)

````

---

## 🚀 Features

- Manage horse race data and odds
- Accept and process betting commands
- Dispense payouts using available inventory
- Refill cash inventory
- Display inventory and race results
- Follows the Command Design Pattern
- Modular and testable architecture

---

## 🛠️ Setup

1. **Clone the Repository**
    ```bash
   git clone https://github.com/...../horse-track-machine.git
   cd horse-track-machine
    ````

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app/main.py
   ```

---

## 🧾 Valid Commands

| Command          | Description                  |
|------------------| ---------------------------- |
| `R` or `r`       | Restock the cash inventory   |
| `Q` or `q`       | Quit the application         |
| `w <horse#>`     | Set the winning horse        |
| `<horse#> <bet>` | Place a bet on a horse (1-7) |

---

## 🧪 Running Tests

To run **all tests** in the `/tests` folder:

```bash
pytest tests/
```


---

## 📁 Configuration

Horse and inventory data is stored in `app/config.py`:

```python
HORSES = [
    {"number": 1, "name": "That Darn Gray Cat", "odds": 5},
    ...
]

INVENTORY = {
    100: 10,
    20: 10,
    10: 10,
    5: 10,
    1: 10
}
```

---

## ✅ Sample Usage

```text
> 1 50
Payout: That Darn Gray Cat, $250
$100,2
$20,2
$10,1

> W 2
Winner: Fort Utopia

> r
Inventory restocked
```

---

## 📚 Design Highlights

* Follows Command Design Pattern for extensibility
* Separation of concerns: model, command, config, and utility modules
* Easily testable with Pytest + mocks
* Uses configuration files for data initialization

---

