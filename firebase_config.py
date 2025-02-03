import firebase_admin
from firebase_admin import credentials

# Correct path to your JSON file
json_path = r"C:\Users\CPT\OneDrive\Desktop\xus.ai\xus-ai-2a7a2-firebase-adminsdk-fbsvc-ac87a8cf08.json"

# Initialize Firebase
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

print("🔥 Firebase initialized successfully!")
