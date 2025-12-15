import requests
import time
import subprocess
import sys

def verify_backend():
    # Start backend in background
    process = subprocess.Popen([sys.executable, "run.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Backend started with PID:", process.pid)
    
    try:
        # Wait for startup (increased to 10s)
        time.sleep(10)
        
        # Test Analysis Endpoint
        print("Testing /api/analyze...")
        response = requests.post("http://localhost:8000/api/analyze", json={"query": "test"})
        if response.status_code == 200:
            print("Analyze Endpoint: SUCCESS")
            print(response.json()['summary']['thesis'][:50] + "...")
        else:
            print("Analyze Endpoint: FAILED", response.text)
            
        # Test Report Endpoint
        print("Testing /api/report...")
        response = requests.post("http://localhost:8000/api/report", json={"query": "test"})
        if response.status_code == 200 and response.headers['content-type'] == 'application/pdf':
            print("Report Endpoint: SUCCESS")
        else:
            print("Report Endpoint: FAILED", response.status_code)

    except Exception as e:
        print("Verification Failed:", e)
        # Print backend output for debugging
        outs, errs = process.communicate(timeout=5)
        print("Backend STDOUT:", outs.decode())
        print("Backend STDERR:", errs.decode())
    finally:
        process.terminate()
        print("Backend stopped")

if __name__ == "__main__":
    verify_backend()
