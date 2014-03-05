# test_Dataset.py

import Dataset


def main():
    print("This is a program to compute the min, max, mean and ")
    print('standard deviation for a set of numbers.\n')
    data = Dataset()
    while True:
        xStr = input('Enter a number (<Enter> to quit): ')
        if xStr == "":
            break
        try:
            x = float(xStr)
        except ValueError:
            print("Invalid Entry Ignored: Input was not a number")
            continue
        data.add(x)
    print('Summary of', data.size(), 'scores.')
    print('Min: ', data.min())
    print('Max: ', data.max())
    print('Mean: ', data.mean())
    print('Standard Deviation: ', data.std_deviation())

if __name__ == "__main__":
    main()