import os
import logging
import re
import csv
from collections import defaultdict, Counter
from query_rag import query_rag  # Import the chatbot functionality
from dotenv import load_dotenv

# Constants
LOG_FILE = "sample.log"
OUTPUT_CSV = "log_analysis_results.csv"
FAILED_LOGIN_THRESHOLD = 10

# Load environment variables
load_dotenv()

def parse_log_file(file_path):
    """Parses the log file and extracts relevant data."""
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = defaultdict(int)
    
    with open(file_path, "r") as file:
        for line in file:
            # Extract IP, endpoint, and status code
            match = re.match(r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] ".* (/\S*) HTTP/.*" (\d+)', line)
            if match:
                ip, endpoint, status_code = match.groups()
                ip_requests[ip] += 1
                endpoint_requests[endpoint] += 1
                if status_code == "401":
                    failed_logins[ip] += 1
            else:
                print(f"Warning: Could not parse line: {line.strip()}")  # Debug for unmatched lines
                
    return ip_requests, endpoint_requests, failed_logins

def analyze_requests(ip_requests):
    """Analyzes request counts per IP address."""
    sorted_requests = sorted(ip_requests.items(), key=lambda x: x[1], reverse=True)
    return sorted_requests

def analyze_endpoints(endpoint_requests):
    """Finds the most frequently accessed endpoint."""
    if endpoint_requests:
        most_accessed = max(endpoint_requests.items(), key=lambda x: x[1])
        return most_accessed
    return None, 0

def detect_suspicious_activity(failed_logins, threshold):
    """Detects suspicious activity based on failed login attempts."""
    suspicious_ips = {ip: count for ip, count in failed_logins.items() if count > threshold}
    return suspicious_ips

def save_to_csv(ip_requests, endpoint, failed_logins, output_file):
    """Saves analysis results to a CSV file."""
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Write Requests per IP
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_requests)
        
        # Write Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow(endpoint)
        
        # Write All Failed Logins
        writer.writerow([])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(failed_logins.items())

def main():
    # Parse the log file
    ip_requests, endpoint_requests, failed_logins = parse_log_file(LOG_FILE)
    
    # Analyze requests per IP
    sorted_requests = analyze_requests(ip_requests)
    
    # Identify the most frequently accessed endpoint
    most_accessed_endpoint = analyze_endpoints(endpoint_requests)
    
    # Detect suspicious activity based on threshold
    suspicious_ips = detect_suspicious_activity(failed_logins, FAILED_LOGIN_THRESHOLD)
    
    # Display results
    print("Requests per IP Address:")
    for ip, count in sorted_requests:
        print(f"{ip:20} {count}")
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")
    
    print("\nSuspicious Activity Detected:")
    if suspicious_ips:
        print(f"{'IP Address':<20}{'Failed Login Attempts':<25}")
        print("-" * 45)  # Adds a line separator for better readability
        for ip, count in suspicious_ips.items():
            print(f"{ip:<20}{count:<25}")
    else:
        print("None")
    
    # Save all results to CSV
    save_to_csv(sorted_requests, most_accessed_endpoint, failed_logins, OUTPUT_CSV)
    print(f"\nResults saved to {OUTPUT_CSV}")
    
    # Allow user to query the log data
    print("\nNow, you can ask questions related to the log analysis.")
    while True:
        # Get user input dynamically for the query
        question = input("Enter your query (or type 'exit' to quit): ").strip()

        if question.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        
        # Get the response from the RAG model based on user input
        response = query_rag(question=question)
        print(f"Response: {response}")
        
        # Optionally, allow the user to continue asking questions
        continue_query = input("Would you like to ask another question? (yes/no): ").strip().lower()
        
        if continue_query == "no":
            print("Exiting the chat. Goodbye!")
            break
        elif continue_query != "yes":
            print("Invalid option. Exiting the chat.")
            break

if __name__ == "__main__":
    main()
