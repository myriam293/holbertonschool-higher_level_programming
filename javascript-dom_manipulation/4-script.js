Okay so here are the instructions: 
Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:
The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list
Please test with this HTML file in your browser:
javiercito @ubuntu: ~/javascript-dom_manipulation$ cat 4-main.html
    < !DOCTYPE html >
        <html lang="en">
            <head>
                <title>Holberton School</title>
            </head>
            <body>
                <header>
                    First HTML page
                </header>
                <br />
                <div id="add_item">Add item</div>
                <br />
                <ul class="my_list">
                    <li>Item</li>
                </ul>
                <footer>
                    Holberton School - 2022
                </footer>
                <script type="text/javascript" src="4-script.js"></script>
            </body>
        </html>
javiercito @ubuntu: ~/javascript-dom_manipulation$
Repo:
* GitHub repository: holbertonschool - higher_level_programming
    * Directory: javascript - dom_manipulation
	•	File: 4 - script.js

And here is my code:

const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
    const nuevo = document.createElement('li');
    nuevo.textContent = 'Item';
    listClass.appendChild(nuevo);
});