def save_history (entry):
    with open("history.txt", "a") as f:
        f.write(entry + "\n")
        
def load_history():
    try:
        with open("history.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []