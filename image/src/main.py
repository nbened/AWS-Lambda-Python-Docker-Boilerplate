import numpy as np

# use this file as your main testing if python is locally installed
# the args are what is sent by the client

def main(arg1,arg2):
    arr = np.random.randint(0, 10, (3, 3))

    print("\n\n\nInt args added are:")
    print(f"{arg1+arg2}\n\n\n")

    return arr

if __name__ == "__main__":
    result = main(1,2)
    print("Result when run directly:")
    print(result)