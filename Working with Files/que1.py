
# Configure logging
import logging
from pdb import main


logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s - %(message)s') 
def read_numbers(file_name):
    logging.info('File opened: %s', file_name)
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    logging.info('Data loaded: %d values', len(numbers))
    return numbers  
def compute_statistics(numbers):
    total_values = len(numbers)
    sum_values = sum(numbers)
    average_value = sum_values / total_values if total_values > 0 else 0
    logging.info('Computation completed: Total=%d, Sum=%d, Average=%.2f', total_values, sum_values, average_value)
    return total_values, sum_values, average_value

def write_results(total, sum_values, average):
    with open('results.log', 'a') as log_file:
        log_file.write(f'Total number of values: {total}\n')
        log_file.write(f'Sum of values: {sum_values}\n')
        log_file.write(f'Average value: {average:.2f}\n')
    logging.info('Results written to results.log')

    def main():
    numbers = read_numbers('numbers.txt')
    total, sum_values, average = compute_statistics(numbers)
    write_results(total, sum_values, average)
    logging.info('File closed: results.log')
if __name__ == '__main__':
    main()






