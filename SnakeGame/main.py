def main():
    # Logic to start the game
    running = True
    iterations = 0
    max_iterations = 10
    print("Starting game...")


    while running:
        print(f"""Iteration {iterations}""")
        iterations += 1
        
        # Determine if we should stop the game
        if (iterations > max_iterations):
            running = False


    # Logic to end the game 
    print("Ending game...")


if __name__ == '__main__':
    main()
