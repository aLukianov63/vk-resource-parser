import argparse


def main():
    parser = argparse.ArgumentParser(description="VK resourse parser")
    parser.add_argument("action", choices=["user", "group"], help="")
    parser.add_argument("id", type=int, help="")
    parser.add_argument("--type", choices=["voice", "photo", "video", "message", "document", "all"],
                        default="all", help="")
    parser.add_argument("--path", type=str, default="/data/", help="")

    args = parser.parse_args()

    print(f"\n{args.action} | {args.id} | {args.type} | {args.path}\n")


if __name__ == '__main__':
    main()
