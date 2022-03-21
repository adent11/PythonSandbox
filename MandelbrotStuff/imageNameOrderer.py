import shutil

WIDTH, HEIGHT = 1080, 720

for i in range(2000, 2135, 1):
    pwr = i/1000
    curPath = f"Ndelbrot/{pwr}.jpg"
    newPath = f"OrderedNdelbrot/{i}.jpg"
    command = f"copy {curPath} {newPath}"
    shutil.copyfile(curPath, newPath)
