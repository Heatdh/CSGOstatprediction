import argparse

if __name__ == '__main__':
    argparse=argparse.ArgumentParser()
    argparse.add_argument('--team',type=str,default='NIP')
    argparse.add_argument('--since',type=int,default=0)
    args=argparse.parse_args()
    print(args.team)
    print(args.since)


    