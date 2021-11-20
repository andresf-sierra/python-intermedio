def run():
    
    challenge = [i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(challenge)

if __name__ == "__main__":
    run()
