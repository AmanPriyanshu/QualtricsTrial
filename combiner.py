import os

def combine_html_pages(file1_path, file2_path, output_path):
    print(file1_path, file2_path)
    with open(file1_path, 'r') as f:
        content1 = f.read()
    with open(file2_path, 'r') as f:
        content2 = f.read()
    content1 = content1.replace(
        'Proceed',
        '<button onclick="togglePages()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Proceed</button>'
    )
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Combined Pages</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.js"></script>
        <style>
            #page2 { display: none; }
        </style>
        <script>
            function togglePages() {
                document.getElementById('page1').style.display = 'none';
                document.getElementById('page2').style.display = 'block';
            }
        </script>
    </head>
    <body>
        <div id="page1">
            """
    template += content1
    template +="""        
        </div>
        <div id="page2">
            """
    template += content2
    template += """
        </div>
        <script>
            function togglePages() {{
                document.getElementById('page1').style.display = 'none';
                document.getElementById('page2').style.display = 'block';
            }}
        </script>
    </body>
    </html>
    """
    with open(output_path, 'w') as f:
        f.write(template)

files = sorted([f for f in os.listdir("New")])
intro_pages = [f for f in files if 'intro' in f]
option_pages = [f for f in files if 'option' in f]

combinations = []
for i in intro_pages:
    prefix_i = i[:-5]
    i = os.path.join("New", i)
    for o in option_pages:
        new_name = prefix_i+'_'+o
        o = os.path.join("New", o)
        combine_html_pages(i, o, new_name)