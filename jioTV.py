
from jioTV import JioTV

def main():
    jtv = JioTV("jtv_config.json")
    playlist = jtv.getChannels()
    print(playlist)

if __name__ == "__main__":
    main()
