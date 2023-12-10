import argparse

from setup import ACCESS_TOKEN
from src.utils import resource_download, resource_type, save_messages_to_file
from src.vk_downloader import VKParser


def main():
    parser = argparse.ArgumentParser(description="VK resourse parser")
    parser.add_argument("action", choices=["user", "group"], help="")
    parser.add_argument("id", type=int, help="")
    parser.add_argument("--type", choices=["voice", "photo", "video", "message", "document", "all"],
                        default="all", help="")
    parser.add_argument("--path", type=str, default="/data/", help="")

    args = parser.parse_args()
    vk = VKParser(token=ACCESS_TOKEN)

    if args.action == "user":
        match args.type:
            case "photo":
                resource = vk.get_chat_photo_links(args.id)
                resource_download(resource, args.path, resource_type.ResourceType.PHOTO)
            case "voice":
                resource = vk.get_chat_voice_links(args.id)
                resource_download(resource, args.path, resource_type.ResourceType.VOICE)
            case "message":
                resource = vk.get_chat_messages(args.id)
                save_messages_to_file(resource, args.path)


if __name__ == '__main__':
    main()
