import glob

label_files = (
    glob.glob("/Users/jo-eunjin/Downloads/SISO/crosswalk.v1i.yolov11/train/labels/*.txt")
    + glob.glob("/Users/jo-eunjin/Downloads/SISO/crosswalk.v1i.yolov11/valid/labels/*.txt")
    + glob.glob("/Users/jo-eunjin/Downloads/SISO/crosswalk.v1i.yolov11/test/labels/*.txt")
)

for path in label_files:
    with open(path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        parts[0] = "2"   
        new_lines.append(" ".join(parts) + "\n")

    with open(path, "w") as f:
        f.writelines(new_lines)

print("모든 횡단보도 라벨을 class 2로 변경 완료!!")