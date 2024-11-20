def read_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def combine_html(page1_path, page2_path, output_path):
    page1_html = read_html(page1_path)
    page2_html = read_html(page2_path)
    suffix_of_combined = page1_html[:page1_html.index('</style>')]+'\n'
    suffix_of_combined += page2_html[page2_html.index('<style>')+len('<style>'):page2_html.index('</style>')]+'\n    </style>'
    suffix_of_combined += """</head>
<body class="bg-gray-50 min-h-screen">

    <!-- First Page Content -->
    <div id="page1">"""+'\n'
    suffix_of_combined += page1_html[page1_html.index('<!-- Main Content -->'):len('</footer>')+page1_html.index('</footer>')].replace('button class=', 'button id="proceed-button" class=')+'\n    </div>\n\n'+"""<!-- Second Page Content -->
    <div id="page2">\n"""
    suffix_of_combined += page2_html[page2_html.index('<body>')+len('<body>'):page2_html.index('</body>')]+'\n'+"""</div>

    <!-- Script to Handle Page Transition -->
    <script>
        document.getElementById('proceed-button').addEventListener('click', () => {
            document.getElementById('page1').style.display = 'none';
            document.getElementById('page2').style.display = 'block';
            // Optionally, scroll to top of the new page
            window.scrollTo(0, 0);
            // Optionally, update the document title
            document.title = "Data Sharing Preferences";
        });
    </script>

</body>
</html>"""
    with open(output_path, "w") as f:
        f.write(suffix_of_combined)

if __name__ == "__main__":
    combine_html("intro_baseline_non_technical.html", "option_high_level_with_all_contents.html", "py_combined.html")