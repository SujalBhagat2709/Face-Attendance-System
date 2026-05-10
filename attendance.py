from datetime import datetime

attendance_log = []

def mark_attendance(name):
    
    entry = {
        "name": name,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    
    attendance_log.append(entry)
    
    return entry


if __name__ == "__main__":
    
    result = mark_attendance("Sujal")
    
    print(result)