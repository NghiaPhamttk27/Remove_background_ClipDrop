import requests
import os

def remove_bg(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"): 
            with open(os.path.join(input_dir, filename), 'rb') as f:
                image_file_object = f.read()

            r = requests.post('https://clipdrop-api.co/remove-background/v1',
            files = {
                'image_file': (filename, image_file_object, 'image/jpeg'),
                },
            headers = { 'x-api-key': 'c8eed1accfbdd427833a70fa63f0315a34e4ea319e382c78a49d9d8f965ad9c6b3bc4bf8d67d0e1fdc397ddc45331fb8'}
            )
            if (r.ok):
                # r.content contains the bytes of the returned image
                output_filename = 'remove_' + os.path.splitext(filename)[0] + '.png'
                with open(os.path.join(output_dir, output_filename), 'wb') as f:
                    f.write(r.content)
            else:
                r.raise_for_status()


input_folder = "./sample_images"
output_folder = "./Remove_bg_images_sample"
remove_bg(input_folder, output_folder)
