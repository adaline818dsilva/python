def tower(disk, source, auxi, dest):
    if disk == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    tower(disk - 1, source, dest, auxi)
    print(f"Move disk {disk} from {source} to {dest}")
    tower(disk - 1, auxi, source, dest)

disk = int(input("Enter the number of disks: "))
print("Steps involved are:")
tower(disk, 'A', 'B', 'C')

