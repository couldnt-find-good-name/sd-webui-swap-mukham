import os

## _____________________ GALLERY ____________________

root_sd = os.getcwd()
txt2img_dir = os.path.join(root_sd, "Outputs", "txt2img-images")
img2img_dir = os.path.join(root_sd, "Outputs", "img2img-images")
swap_dir = os.path.join(root_sd, "Outputs", "swap-mukham")
others_dir = os.path.join(root_sd, "Outputs")
txt2img_img_list = [] 
img2img_img_list = [] 
swap_img_list = [] 
others_img_list = [] 



def gallery_txt2img():
    txt2img_img_list = []  # Lista vacía para guardar las imágenes
    for root, dirs, files in os.walk(txt2img_dir):  # Recorrer la carpeta y subcarpetas
        for file in files:  # Recorrer los archivos
            if file.endswith((".jpg", ".png", ".jpeg")): 
                img_path = os.path.join(root, file) 
                txt2img_img_list.append(img_path)
    yield gr.Gallery.update(value=txt2img_img_list)  # Devolver el nuevo valor de la galería
def gallery_img2img():
    img2img_img_list = []  # Lista vacía para guardar las imágenes
    for root, dirs, files in os.walk(img2img_dir):  # Recorrer la carpeta y subcarpetas
        for file in files:  # Recorrer los archivos
            if file.endswith((".jpg", ".png", ".jpeg")): 
                img_path = os.path.join(root, file) 
                img2img_img_list.append(img_path)
    yield gr.Gallery.update(value=img2img_img_list)  # Devolver el nuevo valor de la galería

def gallery_swap():
    swap_img_list = []  # Lista vacía para guardar las imágenes
    for root, dirs, files in os.walk(swap_dir):  # Recorrer la carpeta y subcarpetas
        for file in files:  # Recorrer los archivos
            if file.endswith((".jpg", ".png", ".jpeg")): 
                img_path = os.path.join(root, file) 
                swap_img_list.append(img_path)
    yield gr.Gallery.update(value=swap_img_list)  # Devolver el nuevo valor de la galería

def gallery_others():
    global txt2img_img_list, img2img_img_list, swap_img_list
    others_img_list = []  # Lista vacía para guardar las imágenes
    
    # Recorrer la carpeta y subcarpetas de 'others_dir'
    for root, dirs, files in os.walk(others_dir):
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                img_path = os.path.join(root, file)
                
                # Verificar si el archivo ya está en alguna de las listas generadas previamente
                if img_path not in txt2img_img_list and img_path not in img2img_img_list and img_path not in swap_img_list:
                    others_img_list.append(img_path)
    
    yield gr.Gallery.update(value=others_img_list)  # Devolver el nuevo valor de la galería



    #############################  VIDEO GALLERY ###################################################
#
videogallery = """current_dir = outputs_dir
            video_list = []     # Lista para guardar los videos

            def video_gallery(current_dir):
                video_list = []
                for root, dirs, files in os.walk(current_dir):
                    for file in files:
                        if file.endswith(".mp4"):
                            video_path = os.path.join(root, file)
                            video_list.append(video_path)
                return video_list

            def update_video_gallery(sender, data):
                all_videos = video_gallery(current_dir)
                print(all_videos)
                # Usamos un bucle for para actualizar cada componente gr.Video con el valor correspondiente de la lista de videos
                for i in range(3):
                    video_gal[i].update(value=all_videos[i])

            def get_num_rows(video_list, videos_per_row):
                # Esta función calcula el número de filas necesarias para mostrar los videos
                num_videos = len(video_list)
                num_rows = num_videos // videos_per_row
                if num_videos % videos_per_row != 0:
                    num_rows += 1
                return num_rows

            with gr.Tab("Videos", elem_id="videos_tab"):
                update_button = gr.Button(value="Update Gallery", variant="primary")
                all_videos = video_gallery(current_dir)
                videos_per_row = 4
                num_rows = get_num_rows(all_videos, videos_per_row)

                for i in range(num_rows):
                    with gr.Row():
                        # Usamos una lista por comprensión para crear los objetos gr.Video a partir de la lista de videos
                        video_gal = [gr.Video(all_videos[i * videos_per_row + j]) for j in range(videos_per_row) if i * videos_per_row + j < len(all_videos)]

                update_button.click(fn=update_video_gallery, outputs=video_gal)
                preview_video.change(fn=update_video_gallery, outputs=video_gal)
"""
#############################  VIDEO GALLERY ###################################################  



def update_galleries():
    # Crear tres variables vacías para guardar las imágenes de cada tab
    txt2img_img_list = []
    img2img_img_list = []
    swap_img_list = []
    others_img_list = [] 
    # Escanear las imágenes de cada tab_dir y guardarlas en la variable correspondiente
    for root, dirs, files in os.walk(txt2img_dir):
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                img_path = os.path.join(root, file)
                txt2img_img_list.append(img_path)
    for root, dirs, files in os.walk(img2img_dir):
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                img_path = os.path.join(root, file)
                img2img_img_list.append(img_path)
    for root, dirs, files in os.walk(swap_dir):
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                img_path = os.path.join(root, file)
                swap_img_list.append(img_path)
    for root, dirs, files in os.walk(others_dir):
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                img_path = os.path.join(root, file)
                if img_path not in txt2img_img_list and img_path not in img2img_img_list and img_path not in swap_img_list:
                    others_img_list.append(img_path)
                    
    return txt2img_img_list, img2img_img_list, swap_img_list, others_img_list

if __name__ == "__main__":
    txt2img_img_list, img2img_img_list, swap_img_list, others_img_list = update_galleries()
