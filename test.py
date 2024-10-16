import flet as ft

def main(page):
    # 初期のMarkdown内容
    markdown_content = """
    # あなたが言いたかったこと
    ## それはつまり
    **テストメッセージ**
    """

    # Markdownを表示するためのコンポーネント
    markdown_display = ft.Markdown("", selectable=True)

    def show_markdown(e):
        # ボタンが押されたときにMarkdown内容を更新
        print(markdown_content)
        markdown_display.content = markdown_content
        page.update()

    # ボタンを作成
    button = ft.ElevatedButton("Markdownを表示", on_click=show_markdown)

    # ページにボタンとMarkdownを追加
    page.add(button, markdown_display)
    page.update()

# アプリを実行
ft.app(target=main)
