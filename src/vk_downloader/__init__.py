import vk_api
from rich.progress import track


class VKParser:
    def __init__(self, token: str) -> None:
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()

    def get_chat_voice_links(self, user_id: int) -> list[str]:
        voice_links: list[str] = []

        total_messages = self.vk.messages.getHistory(user_id=user_id, count=1)['count']
        message_count_per_request = 200
        num_requests = -(-total_messages // message_count_per_request)

        for i in track(range(num_requests), "[green]Voice messages search..."):
            offset = i * message_count_per_request
            messages = self.vk.messages.getHistory(user_id=user_id, count=message_count_per_request, offset=offset)

            for message in messages['items']:
                if 'attachments' in message and message['attachments']:
                    for attachment in message['attachments']:
                        if attachment['type'] == 'audio_message':
                            audio_message = message['attachments'][0]['audio_message']
                            voice_links.append(audio_message['link_mp3'])

        return voice_links

    def get_chat_photo_links(self, user_id: int) -> list[str]:
        photo_links: list[str] = []

        total_messages = self.vk.messages.getHistory(user_id=user_id, count=1)['count']
        message_count_per_request = 200
        num_requests = -(-total_messages // message_count_per_request)

        for i in track(range(num_requests), "[green]Photo search..."):
            offset = i * message_count_per_request
            messages = self.vk.messages.getHistory(user_id=user_id, count=message_count_per_request, offset=offset)

            for message in messages['items']:
                if 'attachments' in message and message['attachments']:
                    for attachment in message['attachments']:
                        if attachment['type'] == 'photo':
                            photo_message = message['attachments'][0]['photo']['sizes'][5]
                            photo_links.append(photo_message['url'])

        return photo_links

    def get_chat_messages(self, user_id: int) -> list[str]:
        messages_list: list[str] = []

        total_messages = self.vk.messages.getHistory(user_id=user_id, count=1)['count']
        message_count_per_request = 200
        num_requests = -(-total_messages // message_count_per_request)

        for i in track(range(num_requests), "[green]Messages search..."):
            offset = i * message_count_per_request
            messages = self.vk.messages.getHistory(user_id=user_id, count=message_count_per_request, offset=offset)

            for message in messages['items']:
                messages_list.append({"data": message["date"], "from": message["from_id"], "text": message["text"]})

        return messages_list

    def get_chat_doc_links(self, user_id: int) -> list[str]:
        doc_links: list[str] = []

        total_messages = self.vk.messages.getHistory(user_id=user_id, count=1)['count']
        message_count_per_request = 200
        num_requests = -(-total_messages // message_count_per_request)

        for i in track(range(num_requests), "[green]Documents search..."):
            offset = i * message_count_per_request
            messages = self.vk.messages.getHistory(user_id=user_id, count=message_count_per_request, offset=offset)

            for message in messages['items']:
                if 'attachments' in message and message['attachments']:
                    for attachment in message['attachments']:
                        if attachment['type'] == 'doc':
                            doc_message = message['attachments'][0]["doc"]
                            doc_links.append(doc_message['url'])

        return doc_links
