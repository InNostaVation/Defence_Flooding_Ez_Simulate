import sys
import subprocess

def capture_container_logs(container_id):
    try:
        # Run the docker logs command and capture the output
        logs_output = subprocess.check_output(['docker', 'logs', container_id])
        # Write the output to a file
        found_start = False
        relevant_lines = []
        min_line = 0
        count1 = 0
        count2 = 0
        with open('logs.txt', 'w') as f:
            for line in logs_output.decode().split('\n'):
                if 'start worker process' in line:
                    min_line = count1
                count1 =count1+1
            for line in logs_output.decode().split('\n'):
                count2 =count2+1
                if(count2==min_line+2):
                    found_start = True
                if(found_start):
                    relevant_lines.append(line)

            f.write('\n'.join(relevant_lines))
        print("Logs captured successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing logs: {e}")

if __name__ == "__main__":
    # Check if a container ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 logs.py <CONTAINER_ID>")
        sys.exit(1)

    container_id = sys.argv[1]
    capture_container_logs(container_id)
