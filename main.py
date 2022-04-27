from parsetop import Parser


if __name__ == '__main__':
    csv_file_path = 'data/top_linux.csv'
    json_file_path = 'data/json_output_csv.json'
    parser = Parser(csv_file_path, json_file_path)
    parser.create_json_file()
    parser.print_topic('USER')
    parser.print_topic('PID')
    parser.print_topic('COMMAND')
    parser.print_commands_for_specific_pid_topic("2921")
    parser.print_top_five_mem_usage()