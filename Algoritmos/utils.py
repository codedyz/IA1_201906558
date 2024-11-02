def printscs(texto):
    VERDE = "\033[32m"
    RESET = "\033[0m"
    print(f"{VERDE}{texto}{RESET}")



def graph_dot(data):
    lines = []
    lines.append("""graph G {
    node [shape=circle];
    rankdir=TB;
    """)
    lines.append(data)
    lines.append("}")
