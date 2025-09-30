import subprocess
import sys
import time

def start_customer_server():
    """Start customer portal on port 8000"""
    return subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "customer_app:app", 
        "--host", "0.0.0.0", 
        "--port", "8000", 
        "--reload"
    ])

def start_employee_server():
    """Start employee portal on port 8001"""
    return subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "employee_app:app", 
        "--host", "0.0.0.0", 
        "--port", "8001", 
        "--reload"
    ])

if __name__ == "__main__":
    print("Starting Finance Support System...")
    print("Customer Portal: http://localhost:8000")
    print("Employee Portal: http://localhost:8001")
    print("Press Ctrl+C to stop both servers")
    
    try:
        # Start both servers
        customer_process = start_customer_server()
        time.sleep(2)  # Give first server time to start
        employee_process = start_employee_server()
        
        # Wait for both processes
        customer_process.wait()
        employee_process.wait()
        
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        customer_process.terminate()
        employee_process.terminate()
        customer_process.wait()
        employee_process.wait()
        print("Servers stopped.")