from samsung.miner import Samsung
if __name__ == '__main__':
    f = Samsung.read_file()
    #print(f)

    Samsung.extract_hangeul(f)