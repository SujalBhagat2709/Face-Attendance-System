import os
import cv2

def load_images(folder):
    
    images = []
    labels = []
    
    for person in os.listdir(folder):
        
        person_path = os.path.join(folder, person)
        
        for file in os.listdir(person_path):
            
            img_path = os.path.join(person_path, file)
            
            img = cv2.imread(img_path)
            
            if img is not None:
                images.append(img)
                labels.append(person)
    
    return images, labels


if __name__ == "__main__":
    
    images, labels = load_images("faces")
    
    print("Loaded:", len(images))