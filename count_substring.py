def count_substring(string, sub_string):
    total_count = 0
    sub_length = len(sub_string)
    for i in range(len(string) - sub_length + 1):
        if string[i:i+sub_length] == sub_string:
            total_count += 1
    return total_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
