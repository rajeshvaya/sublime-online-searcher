import sublime, sublime_plugin, webbrowser

# function called when input box is called
class OnlineSearchFromInputCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		search_text = ''
		s = OnlineSearcher()
		for selection in self.view.sel():
			search_text = self.view.substr(selection)

		sublime.active_window().show_input_panel('Search online for', search_text,s.search, None, None)
		# items = []
		# for itm in s.settings.get('domains'):
		# 	print itm
		# 	items.insert(0, itm["key"]+": "+search_text)

		# sublime.active_window().show_quick_panel(items, s.search, sublime.MONOSPACE_FONT);

# function called when selection search performed by list
class OnlineSearchFromListCommand(sublime_plugin.TextCommand):
	def process(self, choice):
		s = OnlineSearcher()
		search_text = ''

		for selection in self.view.sel():
			search_text = self.view.substr(selection)

		print s.domains[choice]
		search_text = s.domains[choice]["key"] + ": " + search_text

		s.search(search_text)

	def run(self, edit):
		
		s = OnlineSearcher()
		

		# sublime.active_window().show_input_panel('Search online for', search_text,s.search, None, None)
		items = []
		for itm in s.domains:
			items.append(itm["key"])

		sublime.active_window().show_quick_panel(items, self.process, sublime.MONOSPACE_FONT);
		
	

# function called when selected text is to be searched
class OnlineSearchFromSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		search_text = ''
		for selection in self.view.sel():
			search_text = self.view.substr(selection)

		# if nothing is selected then search on the active word
		if search_text == '':
			return


		s = OnlineSearcher()
		s.search(search_text)
			

# The online searcher class 
class OnlineSearcher(object):
	settings = []
	domains = []
	default_domain = []
	def __init__(self):
		self.settings = sublime.load_settings('OnlineSearch.sublime-settings')
		self.domains = self.settings.get("domains")

	def search(self, search):
		# nothing to do if emtpy string
		if search == '':
			return

		# clean the key and text to be searched 
		search_key = search[:search.find(":")].strip() # extract the key out of the search input
		search_string = search[search.find(":")+1:].strip() # exclude the ":" and trim the spaces
		
		for domain in self.domains:
			# save the default domain to search incase no key found
			if domain["key"] == "default":
				self.default_domain = domain

			# search for the specific key
			if domain["key"] == search_key or search_key == "all":
				url = domain["url"].replace('{{search_query}}', search_string.replace(' ', '%20'))
				self.default_domain = []
				webbrowser.open_new_tab(url)

		# search the default domain
		if self.default_domain:
			url = self.default_domain["url"].replace('{{search_query}}', search_string.replace(' ', '%20'))
			webbrowser.open_new_tab(url)


			


