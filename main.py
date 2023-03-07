# python3
import array

def parallel_processing(n, m, data):
    laiks = []
    laiks = [0 for i in range(n)]

    output = [[0,0]]
    output.pop([0][0])

    k=0
    while(k<len(data)):
        for i in range(n):
            if(k<len(data)):
                output.append([i, laiks[i]])
                laiks[i] = laiks[i] + data[k]
                k=k+1
            else:
                break

    return output

def main():
    first_line = list(map(int, input().split()))
    n = first_line[0]
    m = first_line[1]

    second_line = list(map(int, input().split()))
    data = second_line

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()