import flet as ft
import time
import random

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class Interjection():
    def __init__(self):
        self.message = ""

    def get_message(self):
        message_list = [
            "えーっと。",
            "あの...。",
            "考え中です。",
            "もう少し待ってください。"
        ]
        self.message = random.choice(message_list)
        return self.message

# アイコン、名前、チャットの再利用可能なチャットメッセージ
class ChatMessage(ft.Row):
    def __init__(self, message:Message, write_md=False):
        if write_md:
            md1 = f"""
            # あなたが言いたかったこと

            ## それはつまり

            **{message.text}**
            """

            messages = [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                    ft.Markdown(
                        md1,
                        selectable=True,
                        extension_set="gitHubWeb",
                        code_theme="atom-one-dark"
                    )
                ]
        else:
            messages = [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True)
                ]

        super().__init__()
        self.vertical_alignment = "start"
        self.controls = [
            # アイコン
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name)
            ),
            # 名前とメッセージのカラム
            ft.Column(
                messages,
                tight=True,
                spacing=5,
            )
        ]
    
    # ユーザ名の頭文字の取得
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()
    
    # ユーザ名に基づきハッシュを使いアイコンの色をランダムに決める
    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
    
        return colors_lookup[hash(user_name) % len(colors_lookup)]

def main(page: ft.Page):
    page.title = 'AIチャット'
    interj = Interjection()

    # 送られてきたメッセージをchatに追加
    def on_message(message: Message):
        m = ChatMessage(message)
        chat.controls.append(m)
        print(chat.controls)
        print(type(chat.controls))
        page.update()

    # 送られてきたメッセージをchatに追加
    def on_md_message(message: Message):
        m = ChatMessage(message, True)
        chat.controls.append(m)
        print(chat.controls)
        print(type(chat.controls))
        page.update()

    # 直近のメッセージを削除
    def delete_message():
        chat.controls.pop(-1)
        print(chat.controls)
        print(type(chat.controls))
        page.update()

    # メッセージの送信
    def send_message_click(e):
        if new_message.value != "":
            on_message(Message(user_name='user', text=new_message.value, message_type='human'))
            new_message.value = ''
            new_message.focus()
            page.update()

    # llm = Llama(
    #     model_path="LLMのファイルパス",
    #     # n_gpu_layers=-1, # コメントをはずしてGPUを使う
    #     n_ctx=2048
    # )
    def ai_chat(message):
        # chat_history = [
        #     {"role": "system", "content": "あなたは日本語を話す優秀なアシスタントです。回答には必ず日本語で答えてください。"},
        #     {
        #         "role": "user",
        #         "content": message}
        # ]
        output = f"あなたは{message}とおっしゃいましたね？"

        return output

    def message_creation(name, text, message_type, write_md=False):
        if write_md:
            on_md_message(Message(user_name=name, text=text, message_type=message_type))
        else:
            on_message(Message(user_name=name, text=text, message_type=message_type))

    def send_message_click(e):
        if new_message.value != "":
            message_creation('user', new_message.value, 'human') # 追加
            message_creation('AI', interj.get_message(), 'ai') # 追加
            send_message = new_message.value # Aiに送信するメッセージをsend_messageにコピー 追加
            new_message.value = '' # 入力のメッセージを空白にする 追加
            progress.visible = True # プログレスバーの表示 追加
            page.update() # 追加

            time.sleep(3)

            delete_message() # 考え中ですというセリフを削除

            ai_mes = ai_chat(send_message) # 追加
            message_creation('AI', ai_mes, 'ai', write_md=True) # 追加

            progress.visible = False # プログレスバーの非表示 追加
            new_message.focus()
            page.update()
    
    # スクロールをつける
    chat = ft.ListView(
        expand = True,
        spacing = 10,
        auto_scroll = True
    )
    
    # メッセージボックス
    new_message = ft.TextField(
        hint_text = "Write a message...",
        autocorrect = True,
        shift_enter = True,
        min_lines = 1,
        max_lines = 5,
        filled = True,
        expand = True,
        on_submit = send_message_click
    )

    # プログレスバー
    progress = ft.ProgressBar(
        color = ft.colors.PINK, # 進むバーの色
        bgcolor = ft.colors.GREY_200, # バーの背景色
        visible = False # 非表示にする
    )

    # ページに表示
    page.add(
        ft.Container(
            content = chat,
            border = ft.border.all(1, ft.colors.OUTLINE),
            border_radius = 5,
            padding = 10,
            expand = True,
        ),
        progress,
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    # icon = ft.icons.ATTACH_FILE,
                    icon = ft.icons.BACKUP_TABLE,
                    icon_color=ft.colors.GREEN_ACCENT_200,
                    tooltip = "Send file"
                    # on_click = send_message_click
                ),
                ft.IconButton(
                    icon = ft.icons.DESCRIPTION,
                    icon_color=ft.colors.BLUE,
                    tooltip = "Send file"
                    # on_click = send_message_click
                ),
                ft.IconButton(
                    icon = ft.icons.SEND_ROUNDED,
                    tooltip = "Send message",
                    on_click = send_message_click
                ),
            ]
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)