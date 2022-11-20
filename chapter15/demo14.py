with open('logo.jpg','rb') as src_file:
    with open('copy2logo.jpg','wb') as target_file:
        target_file.write(src_file.read())