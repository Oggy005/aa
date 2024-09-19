def Tower_of_Hanoi(disk , src, dest, auxiliary):
    if disk==1:
        print("Transfer disk 1 from source",src,"to destination",dest)
        return
    Tower_of_Hanoi(disk-1, src, auxiliary, dest)
    print("Transfer disk",disk, "from source",src,"to destination",dest)
    Tower_of_Hanoi(disk-1, auxiliary, dest, src)

disk = int(input("For how many rings you want to search.?"))
Tower_of_Hanoi(disk,'A','B','C')
