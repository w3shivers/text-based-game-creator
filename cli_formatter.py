from rich.style import Style
from rich import print
from rich.console import Console
console = Console()

look = Style(color="red", blink=True, bold=True)
print("Danger, [#40361c]Will[/] Robinson!",)