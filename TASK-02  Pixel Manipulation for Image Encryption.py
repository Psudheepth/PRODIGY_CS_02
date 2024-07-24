from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    try:

        img = Image.open(image_path)
        
      
        img_array = np.array(img)

        key = np.resize(key, img_array.shape)

        encrypted_array = np.bitwise_xor(img_array, key)
 
        encrypted_img = Image.fromarray(encrypted_array)
   
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(encrypted_image_path, key):
    try:
        encrypted_img = Image.open(encrypted_image_path)
        
      
        encrypted_array = np.array(encrypted_img)

       
        key = np.resize(key, encrypted_array.shape)

     
        decrypted_array = np.bitwise_xor(encrypted_array, key)
        
    
        decrypted_img = Image.fromarray(decrypted_array)
        

        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except FileNotFoundError:
        print(f"Error: The file {encrypted_image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

   
    image_path = input("Enter the path to the image file: ").strip()

   
    if not os.path.isfile(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return

   
    choice = input("Do you want to encrypt or decrypt the image? (Enter 'e' for encrypt or 'd' for decrypt): ").strip().lower()

 
    key_input = input("Enter the key for encryption/decryption (a sequence of integers separated by spaces): ").strip()
    key = np.array([int(k) for k in key_input.split()], dtype=np.uint8)

    if choice == 'e':

        encrypt_image(image_path, key)
    elif choice == 'd':
       
        encrypted_image_path = "encrypted_image.png"
        if not os.path.isfile(encrypted_image_path):
            print(f"Error: The file {encrypted_image_path} does not exist. Please encrypt an image first.")
            return
        
    
        decrypt_image(encrypted_image_path, key)
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
