import sys

def simple_interest(principle, interest, time):
    return (principle * interest * time) / 100

if __name__ == "__main__":
    p = int(sys.argv[1])
    i = float(sys.argv[2])
    t = int(sys.argv[3])

    print("SI:", simple_interest(p, i, t))