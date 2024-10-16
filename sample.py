import flet as ft
import time
import random

md1 = """
# Markdown Example
Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.

## Titles

Setext-style

This is an H1
=============

This is an H2
-------------

Atx-style

# This is an H1

## This is an H2

###### This is an H6

Select the valid headers:

- [x] `# hello`
- [ ] `#hello`

## Links

[inline-style](https://www.google.com)

## Images

![Image from Flet assets](/icons/icon-192.png)

![Test image](https://picsum.photos/200/300)

## Tables

|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

## Styling

Style text as _italic_, __bold__, ~~strikethrough~~, or `inline code`.

- Use bulleted lists
- To better clarify
- Your points

## Code blocks

Formatted Dart code looks really pretty too:

```
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: ft.Markdown(data: markdownData),
    ),
  ));
}
```
"""

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
    
def func():
    global md1
    md1 = """
    # Markdown Example
    Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.

    ## Titles

    Setext-style

    This is an H1
    =============

    This is an H2
    -------------

    Atx-style

    # This is an H1

    ## This is an H2

    ###### This is an H6

    Select the valid headers:

    - [x] `# hello`
    - [ ] `#hello`

    ## Links

    [inline-style](https://www.google.com)

    ## Images

    ![Image from Flet assets](/icons/icon-192.png)

    ![Test image](https://picsum.photos/200/300)

    ## Tables

    |Syntax                                 |Result                               |
    |---------------------------------------|-------------------------------------|
    |`*italic 1*`                           |*italic 1*                           |
    |`_italic 2_`                           | _italic 2_                          |
    |`**bold 1**`                           |**bold 1**                           |
    |`__bold 2__`                           |__bold 2__                           |
    |`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
    |`***italic bold 1***`                  |***italic bold 1***                  |
    |`___italic bold 2___`                  |___italic bold 2___                  |
    |`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
    |`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

    ## Styling

    Style text as _italic_, __bold__, ~~strikethrough~~, or `inline code`.

    - Use bulleted lists
    - To better clarify
    - Your points

    ## Code blocks

    Formatted Dart code looks really pretty too:

    ```
    void main() {
    runApp(MaterialApp(
        home: Scaffold(
        body: ft.Markdown(data: markdownData),
        ),
    ));
    }
    ```
    """
    print(md1)


def main(page: ft.Page):

    # md1 = """
    # # aa
    # """
    func()

    # プログレスバー
    progress = ft.ProgressBar(
        color = ft.colors.PINK, # 進むバーの色
        bgcolor = ft.colors.GREY_200, # バーの背景色
        visible = False # 非表示にする
    )

    page.add(
        ft.Markdown(md1, selectable=True, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, code_theme="atom-one-dark")
    )

    # ページに表示
    page.add(
        progress,
        ft.Row(
            [
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
                )
            ]
        )
    )

    page.scroll = "auto"
    page.update()
    page.add(
        ft.Markdown(
            md1,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        )
    )

ft.app(main, view=ft.AppView.WEB_BROWSER)