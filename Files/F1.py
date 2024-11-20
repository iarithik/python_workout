def get_final_line(Filename):
    try:
        final_line = ''

        with open(Filename,'r') as f:
            for current_line in f:
                final_line = current_line
        return final_line.strip()
    except FileNotFoundError:
        return f" File {Filename} not found please enter correct filename"
    except Exception as e:
        return f"an error occured {e}"


if __name__ == '__main__':
    op = get_final_line('Files/random.txt')
    print(op)