import subprocess

def check_service_status(service_name):
    try:
        # Use systemctl command to check if the service is active
        result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True)
        if result.returncode == 0:
            return True  # Service is running
        else:
            return False  # Service is not running
    except Exception as e:
        print(f"Error occurred while checking service status: {e}")
        return False  # Unable to determine service status

if __name__ == "__main__":
    services_to_check = ['mysql', 'httpd','vsftpd']

    for service in services_to_check:
        if check_service_status(service):
            print(f"{service} service is running.")
        else:
            print(f"{service} service is not running.")