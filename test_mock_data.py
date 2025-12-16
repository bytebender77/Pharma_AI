import sys
import os

# Add the project root to the python path
sys.path.append(os.getcwd())

try:
    from app.services.mock_data import SCENARIOS
    print("Successfully imported SCENARIOS.")
    
    for key, data in SCENARIOS.items():
        print(f"Scenario: {key}")
        print(f"  Trials: {len(data['trials'])}")
        print(f"  Patents: {len(data['patents'])}")
        print(f"  Web: {len(data['web'])}")
        
except Exception as e:
    print(f"Error importing mock_data: {e}")
