import math
def main():
    d = 8
    h = 20
    if h >= d:
        magnitude = h//d
        limit = (magnitude+1)*d
        print("limit is ",limit)
        preresult = math.pow(1/d,magnitude)
        print("fraction is", (1-(h%d-1)/d))
        result = preresult * (1-(h%d-1)/d)
        print(result)
    else:
        result = 1-(h-1)/d
        print(result)
    
    


if __name__ == "__main__":
    main()