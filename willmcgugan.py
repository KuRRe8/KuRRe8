from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🚴 [link=https://github.com/KuRRe8]KuRRe8", guide_style="bold cyan")
python_tree = tree.add("🐍 Python Proficient ", guide_style="green")
python_tree.add("🌟 ML/ DL")
python_tree.add("🌟 ROS2")
python_tree.add("🌟 PyQt")
cpp_tree = tree.add("➕ C/C++ Intermediate ", guide_style="green")
cpp_tree.add("⭐ Embedded")
cpp_tree.add("⭐ Qt/ MFC/ Win")
cpp_tree.add("⭐ Driver")
csharp_tree = tree.add("#️⃣ C# Intermediate ", guide_style="green")
matlab_tree = tree.add("📊 Matlab Intermediate ", guide_style="green")
js_tree = tree.add("🟨 JS Novice ", guide_style="green")

about = """\
I am a developer from China, focusing on CV and Robotics. I have years of coding experience, and good ability to operate hardware, since I originally worked as an embedded software engineer.

Glad to participate in any interesting deep learning work.

In addition to the Github main repository, I have also posted a lot of interesting content on [link=https://gist.github.com/KuRRe8]Github Gist[/link]. Welcome to take a look."""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
