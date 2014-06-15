Online searcher for Sublime Text
==================================================

This plugin enables the user to search online right from the sublime text editor. User can search through input, right-clicking the selected text and through general key-bindings. 


You can also add your own custom domains, search engines and other documentations which are not included by default in this plugin


## Key Bindings

* On pressing `ctrl+alt+o` you will be prompted to input the search string 
* On pressing `ctrl+alt+i` search the default domain with the selected text


You can change the default key binding at `Preferences -> Package Settings -> Extended Tab Switcher -> Key Bindings User`


## Usage
* Press `ctrl+alt+o` 
* Enter the search string  in the input box with the format `domain:text` (e.g. `google: css opacity` or `php:in_array`)


Tip: If you have selected text to be searched the input box will be already pre-filled or your can simply right-click and click "Search online" and it will search with default configurations



## Configurations
User can overwrite the following configurations by adding flags in the User - Settings section which can be access by `Preferences -> Package Settings -> Extended Tab Switcher -> Settings - User`

* Default
  - google (e.g. `google: best css practices`)
  - stackOverflow  (e.g. `stackoverflow: jquery animate not working`)
  - github  (e.g. `github: noSQL databases`)
  - php  (e.g. `php: in_array`)
  - jquery  (e.g. `jquery: fadeIn`)
  - youtube  (e.g. `youtube: node.js tutorials`)
  - image  (e.g. `image: facebook icon`)



* Custom
  The above default configurations can be changes by pasting the new configurations into the settings at `Preferences -> Package Settings -> Extended Tab Switcher -> Settings - User`



## License

This projected is licensed under the terms of the MIT license.

```
The MIT License (MIT)

Copyright (c) [2014] [Rajesh Vaya <vaya.rajesh@gmail.com>]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



